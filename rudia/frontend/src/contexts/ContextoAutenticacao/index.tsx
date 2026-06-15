'use client';

import {
    createContext,
    ReactNode,
    useContext,
    useEffect,
    useMemo,
    useState,
} from 'react';
import { IAutenticacaoContextType } from './types';
import {
    login,
    logout,
    obterUsuarioAtual,
    refreshToken,
} from '@/api/autenticacao/autenticacao.fetch';
import { UsuarioDTO } from '@/schemas/autenticacao.schema';
import { ApiError } from '@/api/ApiError';
import { encerrarSessao, obterTokens } from '@/api/autenticacao/utils';

const AutenticacaoContext = createContext<IAutenticacaoContextType | undefined>(
    undefined,
);

export const AutenticacaoProvider = ({ children }: { children: ReactNode }) => {
    const [usuario, setUsuario] = useState<UsuarioDTO | null>(null);
    const [carregando, setCarregando] = useState<boolean>(true);

    /*
        A cada renderização:
            Estado de usuário mudou?
            SIM -> existe usuário (TRUE) ou não existe usuário (FALSE)
            NÃO -> mantem o valor anteriormente guardado em cache
    */
    const estaAutenticado = useMemo(() => !!usuario, [usuario]);

    const autenticar: IAutenticacaoContextType['autenticar'] = async (data) => {
        try {
            const response = await login(data);
            setUsuario(response);
        } catch (err) {
            centralizarError(err);
        }
    };

    const desconectar: IAutenticacaoContextType['desconectar'] = async () => {
        try {
            await logout();
            setUsuario(null);
        } catch (err) {
            encerrarSessao();
        }
    };

    // Somente para DEBUG - Temporario
    const centralizarError = (err: unknown) => {
        if (err instanceof ApiError) {
            console.error(`Erro ${err.status}: ${err.message}`);
        } else {
            console.error('Erro desconhecido ou de rede:', err);
        }
    };

    useEffect(() => {
        const carregarUsuario = async () => {
            if (!obterTokens('ACCESS')) {
                setCarregando(false);
                return;
            }

            let usuarioAtual = null;

            try {
                usuarioAtual = await obterUsuarioAtual();
            } catch (err) {
                // Token Expirado
                if (err instanceof ApiError && err.status === 401) {
                    try {
                        await refreshToken();
                        usuarioAtual = await obterUsuarioAtual();
                    } catch {
                        console.error('Sessão expirado permanentemente');
                        await desconectar();
                    }
                }
            } finally {
                setUsuario(usuarioAtual);
                setCarregando(false);
            }
        };

        carregarUsuario();
    }, []);

    return (
        <AutenticacaoContext.Provider
            value={{
                usuario,
                estaAutenticado,
                carregando,

                autenticar,
                desconectar,
            }}
        >
            {children}
        </AutenticacaoContext.Provider>
    );
};

export const useAutenticacao = () => {
    const contexto = useContext(AutenticacaoContext);

    if (!contexto)
        throw new Error(
            'useAutenticacao deve ser usado dentro de AutenticacaoProvider',
        );

    return contexto;
};
