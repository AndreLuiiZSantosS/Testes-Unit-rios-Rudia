import { ENDPOINTS } from "@/api/ApiConfig";
import { fetchPadrao } from "@/api/UtilsApi";
import {
  PropostaServicoRequestDTO,
  PropostaServicoResponseSchema,
} from "@/schemas/proposta-servico.schema";

export const registroPropostaServico = async (
  data: PropostaServicoRequestDTO,
) => {
  return await fetchPadrao({
    resource: ENDPOINTS.REGISTRO_SERVICO,
    authorization: true,
    options: {
      method: "POST",
      body: JSON.stringify(data),
    },
    zodSchema: PropostaServicoResponseSchema,
  });
};
