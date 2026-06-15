import { ENDPOINTS } from '@/api/ApiConfig';
import { fetchPadrao } from '@/api/UtilsApi';
import {
    ListaCidadesResponseSchema,
    ListaEstadosResponseSchema,
} from '@/schemas/cidade-estado.schema';

export const obterCidades = () => {
    return fetchPadrao({
        resource: ENDPOINTS.CIDADES,
        authorization: false,
        options: {
            method: 'GET',
        },
        zodSchema: ListaCidadesResponseSchema,
    });
};

export const obterEstados = () => {
    return fetchPadrao({
        resource: ENDPOINTS.ESTADOS,
        authorization: false,
        options: {
            method: 'GET',
        },
        zodSchema: ListaEstadosResponseSchema,
    });
};
