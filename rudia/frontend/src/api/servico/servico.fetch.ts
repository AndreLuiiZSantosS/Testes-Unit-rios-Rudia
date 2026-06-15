import { ENDPOINTS } from '@/api/ApiConfig';
import { fetchPadrao } from '@/api/UtilsApi';
import { CategoriaTypeDTO } from '@/schemas/categoria-tag.schema';
import {
    ServicoCompletoSchema,
    ServicosCategoriaResponseSchema,
} from '@/schemas/servico.schema';

export const obterServicoPorId = async (id: number) => {
    return await fetchPadrao({
        resource: `${ENDPOINTS.SERVICO_POR_ID}${id}`,
        authorization: false,
        options: {
            method: 'GET',
        },
        zodSchema: ServicoCompletoSchema,
    });
};

export interface FiltrosServico {
    categoria: CategoriaTypeDTO | number;
    destino: number;
    viajantes: number;
}

export const obterServicosPorCategoria = async ({
    ...filtros
}: FiltrosServico) => {
    return await fetchPadrao({
        resource: `${ENDPOINTS.SERVICOS_POR_CATEGORIA}${filtros.categoria}?destino=${filtros.destino}`,
        authorization: false,
        options: {
            method: 'GET',
        },
        zodSchema: ServicosCategoriaResponseSchema,
    });
};
