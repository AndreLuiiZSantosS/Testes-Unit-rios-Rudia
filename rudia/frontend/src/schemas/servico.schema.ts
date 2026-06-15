import { z } from 'zod';
import { UsuarioSchema } from './autenticacao.schema';
import { CategoriaParcialSchema, TagSchema } from './categoria-tag.schema';
import { CidadeParcialSchema, SiglaUFSchema } from './cidade-estado.schema';
import {
    AvaliacaoSchema,
    PaginatorSchema,
    ResumoAvalicoesSchema,
} from './geral.schema';

// Schema Zod para Requisições

// Schema Zod para Respostas
export const DiaSemanaTypeSchema = z.enum([
    'DOM',
    'SEG',
    'TER',
    'QUA',
    'QUI',
    'SEX',
    'SAB',
]);
export const DiaSemanaDisplaySchema = z.enum([
    'Domingo',
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-feira',
    'Sexta-feira',
    'Sábado',
]);

export const EnderecoSchema = z.object({
    id: z.number(),
    cep: z.string(),
    logradouro: z.string(),
    numero: z.string(),
    complemento: z.string().nullish(),
    endereco_completo: z.string(),
});

export const HorarioFuncionamentoSchema = z.object({
    id: z.number(),
    dia_semana: DiaSemanaTypeSchema,
    dia_semana_display: DiaSemanaDisplaySchema,
    hora_abertura: z.iso.time(),
    hora_fechamento: z.iso.time(),
});

export const ServicoRestFulLinksSchema = z.object({
    avaliacoes: z.string(),
    categoria: z.string(),
});

// Serviço por ID (Service By ID)
export const ServicoCompletoSchema = z.object({
    id: z.number(),
    nome: z.string(),
    descricao: z.string(),
    capacidade_maxima: z.number(),
    preco_minimo: z.coerce.number(),
    preco_maximo: z.coerce.number(),
    preco_medio: z.coerce.number(),
    imagem_capa_url: z.string().url(),
    ativo: z.boolean(),
    data_admissao: z.iso.datetime().nullish(),
    categoria: CategoriaParcialSchema,
    cidade: CidadeParcialSchema,
    parceiro: UsuarioSchema.pick({
        id: true,
        username: true,
        foto_perfil: true,
    }),
    endereco: EnderecoSchema,
    tags: TagSchema.array(),
    horarios_funcionamento: HorarioFuncionamentoSchema.array(),
    avaliacoes_resumo: ResumoAvalicoesSchema,
    ultimas_avaliacoes: AvaliacaoSchema.array(),
    links: ServicoRestFulLinksSchema,
});

// Serviços por Categoria (Services By Category)
export const ServicoParcialSchema = ServicoCompletoSchema.pick({
    id: true,
    nome: true,
    descricao: true,
    imagem_capa_url: true,
    preco_medio: true,
}).extend({
    avaliacao_geral: z.coerce.number(),
    categoria_nome: z.string(),
    cidade_nome: z.string(),
    cidade_estado: SiglaUFSchema,
});

export const FiltrosServicoSchema = z.object({
    destino: z.number().nullish(),
    viajantes: z.number().nullish(),
});

export const ServicosCategoriaResponseSchema = z.object({
    categoria: CategoriaParcialSchema,
    filtros_aplicados: FiltrosServicoSchema,
    paginacao: PaginatorSchema,
    servicos: ServicoParcialSchema.array(),
});

// Exportações dos Tipos DTO
export type DiaSemanaTypeDTO = z.infer<typeof DiaSemanaTypeSchema>;
export type DiaSemanaDisplayDTO = z.infer<typeof DiaSemanaDisplaySchema>;

export type ServicoCompletoDTO = z.infer<typeof ServicoCompletoSchema>;
export type ServicoParcialDTO = z.infer<typeof ServicoParcialSchema>;

export type EnderecoDTO = z.infer<typeof EnderecoSchema>;

export type HorarioFuncionamentoDTO = z.infer<
    typeof HorarioFuncionamentoSchema
>;

export type ServicoRestFulLinksDTO = z.infer<typeof ServicoRestFulLinksSchema>;
export type FiltrosServicoDTO = z.infer<typeof FiltrosServicoSchema>;

export type ServicosCategoriaResponseDTO = z.infer<
    typeof ServicosCategoriaResponseSchema
>;
