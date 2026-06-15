import { z } from 'zod';
import { URL_BASE_API } from './ApiConfig';
import { ApiError } from './ApiError';
import { obterTokens } from './autenticacao/utils';

interface FetchPadraoParams<T> {
    resource: string;
    authorization: boolean;
    options?: RequestInit;
    zodSchema?: z.ZodType<T>;
}

// Fetch de API padrão
export const fetchPadrao = async <T>({
    ...params
}: FetchPadraoParams<T>): Promise<T> => {
    const { resource, authorization, options, zodSchema: schema } = params;

    const response = await fetch(`${URL_BASE_API}${resource}`, {
        ...options,
        headers: obterHeaders(authorization, options),
    });

    const json = await response.json().catch(() => {});

    if (!response.ok) {
        // DEBUG
        console.error('Erro na API:', json);
        throw new ApiError(
            'Ocorreu um erro na requisição!',
            response.status,
            json,
        );
    }   

    if (schema) {
        return schema.parse(json);
    }

    return json as T;
};

// Obter o header da requisição
export const obterHeaders = (authorization: boolean, options?: RequestInit) => {
    const token = obterTokens('ACCESS');

    const headers = new Headers({
        'Content-Type': 'application/json',
        ...options?.headers,
    });

    if (authorization) {
        headers.set('Authorization', token ? `Bearer ${token}` : '');
    }

    return headers;
};
