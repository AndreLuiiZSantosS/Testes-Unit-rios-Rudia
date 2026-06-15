import { ENDPOINTS } from '@/api/ApiConfig';
import { fetchPadrao } from '@/api/UtilsApi';
import {
    CriarViagemRequestDTO,
    ViagemResponseSchema,
} from '@/schemas/viagem.schema';

export const criarViagem = (data: CriarViagemRequestDTO) => {
    return fetchPadrao({
        resource: ENDPOINTS.VIAGEM,
        authorization: true,
        options: {
            method: 'POST',
            body: JSON.stringify(data),
        },
        zodSchema: ViagemResponseSchema,
    });
};
