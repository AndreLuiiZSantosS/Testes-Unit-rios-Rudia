import { fetchPadrao } from '@/api/UtilsApi';
import { ENDPOINTS } from '@/api/ApiConfig';
import {
    RegistroRudieroRequestDTO,
    RegistroRudieroResponseSchema,
} from '@/schemas/registro-rudiero.schema';

// Cadastro de Rudiero na aplicação
export const registroRudiero = (data: RegistroRudieroRequestDTO) => {
    return fetchPadrao({
        resource: ENDPOINTS.REGISTRO_RUDIERO,
        authorization: false,
        options: {
            method: 'POST',
            body: JSON.stringify(data),
        },
        zodSchema: RegistroRudieroResponseSchema,
    });
};
