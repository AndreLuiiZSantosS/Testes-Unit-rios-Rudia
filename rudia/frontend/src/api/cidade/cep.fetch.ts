interface ViaCepResponse {
  cep?: string;
  logradouro?: string;
  bairro?: string;
  localidade?: string;
  uf?: string;
  erro?: boolean;
}

export interface EnderecoViaCep {
  logradouro: string;
  bairro: string;
  localidade: string;
  uf: string;
}

export const obterEnderecoPorCep = async (
  cep: string,
): Promise<EnderecoViaCep> => {
  const sanitizedCep = cep.replace(/\D/g, "");

  if (sanitizedCep.length !== 8) {
    throw new Error("CEP invalido para consulta");
  }

  const response = await fetch(
    `https://viacep.com.br/ws/${sanitizedCep}/json/`,
  );

  if (!response.ok) {
    throw new Error("Erro ao consultar o CEP");
  }

  const data = (await response.json()) as ViaCepResponse;

  if (data.erro) {
    throw new Error("CEP nao encontrado");
  }

  return {
    logradouro: data.logradouro || "",
    bairro: data.bairro || "",
    localidade: data.localidade || "",
    uf: data.uf || "",
  };
};
