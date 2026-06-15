import { ENDPOINTS } from '@/api/ApiConfig';
import { fetchPadrao } from '@/api/UtilsApi';
import {
    LoginRequestDTO,
    LoginResponseSchema,
    RefreshResponseSchema,
    UsuarioSchema,
} from '@/schemas/autenticacao.schema';
import {
    encerrarSessao,
    guardarTokens,
    iniciarSessao,
    obterTokens,
} from './utils';

export const login = async (data: LoginRequestDTO) => {
    const response = await fetchPadrao({
        resource: ENDPOINTS.LOGIN,
        authorization: false,
        options: {
            method: 'POST',
            body: JSON.stringify(data),
        },
        zodSchema: LoginResponseSchema,
    });

    iniciarSessao(
        {
            id: response.user.id,
            username: response.user.username,
        },
        {
            access: response.access,
            refresh: response.refresh,
            usuarioId: response.user.id,
        },
    );

    return response.user;
};

export const logout = async () => {
    await fetchPadrao({
        resource: ENDPOINTS.LOGOUT,
        authorization: true,
        options: {
            method: 'POST',
            body: JSON.stringify({
                refresh: obterTokens('REFRESH'),
            }),
        },
    });

    encerrarSessao();
};

export const refreshToken = async () => {
    const response = await fetchPadrao({
        resource: ENDPOINTS.REFRESH,
        authorization: true,
        options: {
            method: 'GET',
            body: JSON.stringify({
                refresh: obterTokens('REFRESH'),
            }),
        },
        zodSchema: RefreshResponseSchema,
    });

    guardarTokens({
        access: response.access,
        refresh: response.refresh,
    });
};

export const obterUsuarioAtual = () => {
    return fetchPadrao({
        resource: ENDPOINTS.ME,
        authorization: true,
        options: {
            method: 'GET',
        },
        zodSchema: UsuarioSchema,
    });
};
