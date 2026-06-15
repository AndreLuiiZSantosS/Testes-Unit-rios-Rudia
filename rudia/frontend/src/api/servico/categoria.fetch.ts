import { ENDPOINTS } from "@/api/ApiConfig";
import { fetchPadrao } from "@/api/UtilsApi";
import {
  ListaCategoriasResponseSchema,
  ListaTagsResponseSchema,
} from "@/schemas/categoria-tag.schema";

export const obterCategoriasServico = () => {
  return fetchPadrao({
    resource: ENDPOINTS.CATEGORIAS_SERVICO,
    authorization: false,
    options: {
      method: "GET",
    },
    zodSchema: ListaCategoriasResponseSchema,
  });
};

export const obterTagsCategoria = (id: number) => {
  return fetchPadrao({
    resource: `${ENDPOINTS.CATEGORIAS_SERVICO}${id}/tags/`,
    authorization: false,
    options: {
      method: "GET",
    },
    zodSchema: ListaTagsResponseSchema,
  });
};
