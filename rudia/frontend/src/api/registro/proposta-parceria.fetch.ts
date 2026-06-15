import { ENDPOINTS } from '@/api/ApiConfig';
import { fetchPadrao } from '@/api/UtilsApi';
import {
    PropostaParceriaRequestDTO,
    PropostaParceriaResponseSchema,
} from '@/schemas/proposta-parceria.schema';

export const registroPropostaParceria = async (
    data: PropostaParceriaRequestDTO,
) => {
    return await fetchPadrao({
        resource: ENDPOINTS.REGISTRO_PARCEIRO,
        authorization: false,
        options: {
            method: 'POST',
            body: JSON.stringify(data),
        },
        zodSchema: PropostaParceriaResponseSchema,
    });
};
