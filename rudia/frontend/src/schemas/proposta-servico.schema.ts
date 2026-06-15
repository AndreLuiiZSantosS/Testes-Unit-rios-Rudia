import { z } from "zod";
import { SiglaUFSchema } from "./cidade-estado.schema";

// Schema Zod para Requisições
export const DiaSemanaSchema = z.enum([
  "DOM",
  "SEG",
  "TER",
  "QUA",
  "QUI",
  "SEX",
  "SAB",
]);

export const CategoriaServicoSchema = z.object({
  id: z.number(),
  nome: z.string(),
});

export const TagServicoSchema = z.object({
  id: z.number(),
  nome: z.string(),
});

export const CidadeServicoSchema = z.object({
  id: z.number(),
  nome: z.string(),
  estado_sigla: SiglaUFSchema,
});

export const EnderecoServicoSchema = z.object({
  id: z.number().optional(),
  cep: z.string().regex(/^\d{8}$/, "CEP deve conter 8 digitos numericos"),
  logradouro: z.string(),
  numero: z.string(),
  complemento: z.string().nullish(),
});

export const HorarioFuncionamentoSchema = z.object({
  id: z.number().optional(),
  dia_semana: DiaSemanaSchema,
  dia_semana_display: z.string(),
  hora_abertura: z.string().regex(/^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$/),
  hora_fechamento: z.string().regex(/^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$/),
});

export const ParceiroServicoSchema = z.object({
  id: z.number(),
  username: z.string(),
  nome: z.string(),
  cnpj: z.string(),
});

export const AvaliacoesResumoSchema = z.object({
  media_geral: z.number(),
  total: z.number(),
  distribuicao: z.object({
    cinco_estrelas: z.number(),
    quatro_estrelas: z.number(),
    tres_estrelas: z.number(),
    dois_estrelas: z.number(),
    uma_estrela: z.number(),
  }),
});

export const ServicoLinksSchema = z
  .object({
    avaliacoes: z.string(),
    categoria: z.string(),
  })
  .optional();

export const ServicoSchema = z.object({
  id: z.number(),
  nome: z.string(),
  descricao: z.string(),
  capacidade_maxima: z.number().nullable(),
  preco_minimo: z.string(),
  preco_maximo: z.string(),
  preco_medio: z.number(),
  imagem_capa_url: z.string(),
  ativo: z.boolean(),
  data_admissao: z.string().nullish(),
  categoria: CategoriaServicoSchema,
  cidade: CidadeServicoSchema,
  parceiro: ParceiroServicoSchema,
  endereco: EnderecoServicoSchema,
  tags: TagServicoSchema.array(),
  horarios_funcionamento: HorarioFuncionamentoSchema.array(),
  avaliacoes_resumo: AvaliacoesResumoSchema,
  links: ServicoLinksSchema,
});

export const EnderecoCreateSchema = z.object({
  cep: z.string().regex(/^\d{8}$/, "CEP deve conter 8 digitos numericos"),
  logradouro: z.string().min(1),
  numero: z.string().min(1),
  complemento: z.string().optional(),
});

export const HorarioFuncionamentoCreateSchema = z.object({
  dia_semana: DiaSemanaSchema,
  hora_abertura: z.string().regex(/^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$/),
  hora_fechamento: z.string().regex(/^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$/),
});

export const PropostaServicoRequestSchema = z.object({
  nome: z.string().min(1),
  descricao: z.string().min(1),
  capacidade_maxima: z.number().nullable().optional(),
  preco_minimo: z.number(),
  preco_maximo: z.number(),
  imagem_capa: z.string().min(1),
  categoria: z.number(),
  cidade: z.number(),
  tags: z.array(z.number()),
  endereco: EnderecoCreateSchema,
  horarios_funcionamento: z.array(HorarioFuncionamentoCreateSchema).min(1),
});

// Schema Zod para Respostas
export const PropostaServicoResponseSchema = z
  .object({
    message: z.string().optional(),
    servico: ServicoSchema.optional(),
  })
  .passthrough();

// Exportações dos Tipos DTO
export type DiaSemanaDTO = z.infer<typeof DiaSemanaSchema>;

export type CategoriaServicoDTO = z.infer<typeof CategoriaServicoSchema>;
export type TagServicoDTO = z.infer<typeof TagServicoSchema>;
export type CidadeServicoDTO = z.infer<typeof CidadeServicoSchema>;
export type EnderecoServicoDTO = z.infer<typeof EnderecoServicoSchema>;
export type HorarioFuncionamentoDTO = z.infer<
  typeof HorarioFuncionamentoSchema
>;
export type ParceiroServicoDTO = z.infer<typeof ParceiroServicoSchema>;
export type ServicoDTO = z.infer<typeof ServicoSchema>;

export type PropostaServicoRequestDTO = z.infer<
  typeof PropostaServicoRequestSchema
>;
export type PropostaServicoResponseDTO = z.infer<
  typeof PropostaServicoResponseSchema
>;
