'use client';

import {
    createContext,
    ReactNode,
    useContext,
    useEffect,
    useReducer,
} from 'react';
import {
    IViagemPersonalizadaContextType,
    ViagemPersonalizadaState,
} from './types';
import { initialState, reducer } from './reducer';
import { ViagemPersonalizadaStateDTO } from '@/schemas/viagem.schema';

const ViagemPersonalizadaContext = createContext<
    IViagemPersonalizadaContextType | undefined
>(undefined);

export const ViagemPersonalizadaProvider = ({
    children,
}: {
    children: ReactNode;
}) => {
    const [state, dispatch] = useReducer(reducer, initialState);

    // Carregar o cache da viagem personalizada a cada refresh de tela
    useEffect(() => {
        if (typeof window === 'undefined') return;

        const cache = localStorage.getItem('viagem_personalizada');
        if (cache) {
            try {
                const dados: ViagemPersonalizadaState = JSON.parse(cache);
                if (dados) dispatch({ type: 'LOAD_CACHE', payload: dados });
            } catch (err) {
                console.error(`Error ao recarregar os dados em cache: ${err}`);
            }
        }
    }, []);

    // Salvar o cache da viagem personalizada a cada mudança de estado
    useEffect(() => {
        if (typeof window === 'undefined') return;
        localStorage.setItem('viagem_personalizada', JSON.stringify(state));
    }, [state]);

    const atualizarAtributo: IViagemPersonalizadaContextType['atualizarAtributo'] =
        <C extends keyof ViagemPersonalizadaStateDTO>(
            campo: C,
            valor: ViagemPersonalizadaStateDTO[C],
        ) =>
            dispatch({ type: 'ATUALIZAR_ATRIBUTO', payload: { campo, valor } });

    const atualizarEtapa: IViagemPersonalizadaContextType['atualizarEtapa'] = (
        payload: number,
    ) => dispatch({ type: 'ATUALIZAR_ETAPA', payload });

    const resetViagemPersonalizada: IViagemPersonalizadaContextType['resetViagemPersonalizada'] =
        () => dispatch({ type: 'RESET_VIAGEM_PERSONALIZADA' });

    return (
        <ViagemPersonalizadaContext.Provider
            value={{
                state,
                atualizarAtributo,
                atualizarEtapa,
                resetViagemPersonalizada,
            }}
        >
            {children}
        </ViagemPersonalizadaContext.Provider>
    );
};

export const useViagemPersonalizada = () => {
    const contexto = useContext(ViagemPersonalizadaContext);
    if (!contexto)
        throw new Error(
            'useViagemPersonalizada deve ser usado dentro de um <ViagemPersonalizadaProvider>',
        ); 

    return contexto;
};
