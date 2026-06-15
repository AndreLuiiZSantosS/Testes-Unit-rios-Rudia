import { z } from 'zod';
import { ServicoCompletoSchema } from './servico.schema';
import { UsuarioSchema } from './autenticacao.schema';
import { VisibilidadeTypeSchema } from './geral.schema';
import { CidadeParcialSchema } from './cidade-estado.schema';

// Schema Zod para Requisições
export const CriarViagemRequestSchema = z.object({
    nome: z
        .string()
        .trim()
        .min(
            5,
            'O nome da viagem está muito curto. Use no mínimo 5 caracteres.',
        )
        .max(
            150,
            'O nome da viagem está muito longo. Use no máximo 150 caracteres.',
        ),

    descricao: z
        .string()
        .trim()
        .min(
            10,
            'A descrição da viagem está muito curta. Use no mínimo 10 caracteres.',
        )
        .max(
            500,
            'A descrição da viagem está muito longa. Use no máximo 500 caracteres.',
        ),

    dias: z.coerce
        .number()
        .int('A quantidade de dias deve ser um valor inteiro.')
        .min(1, 'A viagem deve ter pelo menos 1 dia de duração.'),

    viajantes_adultos: z.coerce
        .number()
        .int('A quantidade de adultos deve ser um valor inteiro.')
        .min(1, 'Deve ter no mínimo 1 viajante adulto.'),

    viajantes_criancas: z.coerce
        .number()
        .int('A quantidade de crianças deve ser um valor inteiro.')
        .min(0, 'A quantidade de crianças não pode ser negativa.'),

    visibilidade: VisibilidadeTypeSchema,

    cidade_destino: z.coerce
        .number()
        .int()
        .min(1, 'Selecione uma cidade de destino válida.'),

    hospedagem: z.coerce
        .number()
        .int()
        .min(1, 'Selecione uma hospedagem válida.'),

    transporte: z.coerce
        .number()
        .int()
        .min(1, 'Selecione um meio de transporte válido.'),

    alimentacao: z
        .array(z.number().int())
        .nonempty('Selecione pelo menos uma opção de alimentação.'),

    lazer: z
        .array(z.number().int())
        .nonempty('Selecione pelo menos uma opção de lazer.'),
});

export const ViagemPersonalizadaStateSchema = CriarViagemRequestSchema.extend({
    dias: z.number().int().nullable(),
    cidade_destino: z.number().int().nullable(),
    hospedagem: z.number().int().nullable(),
    transporte: z.number().int().nullable(),
});

// Schema Zod para Respostas
export const ServicoViagemSchema = ServicoCompletoSchema.pick({
    id: true,
    nome: true,
    categoria: true,
    preco_medio: true,
    imagem_capa_url: true,
}).extend({
    parceiro: UsuarioSchema.pick({ id: true, username: true }),
});

export const ServicosViagemSchema = z.object({
    hospedagem: ServicoViagemSchema,
    transporte: ServicoViagemSchema,
    alimentacao: ServicoViagemSchema.array(),
    lazer: ServicoViagemSchema.array(),
});

export const ViagemSchema = z.object({
    id: z.number(),
    nome: z.string(),
    descricao: z.string(),
    dias: z.number(),
    orcamento_total: z.number(),
    viajantes_adultos: z.number(),
    viajantes_criancas: z.number(),
    total_viajantes: z.number(),
    visibilidade: VisibilidadeTypeSchema,
    data_criacao: z.iso.datetime(),
    rudiero: UsuarioSchema.pick({
        id: true,
        username: true,
        nome: true,
        email: true,
    }),
    cidade_destino: CidadeParcialSchema,
    servicos: ServicosViagemSchema,
});

export const ViagemResponseSchema = z.object({
    mensagem: z.string(),
    viagem: ViagemSchema,
});

// Exportações dos Tipos DTO
export type ServicoViagemDTO = z.infer<typeof ServicoViagemSchema>;
export type ServicosViagemDTO = z.infer<typeof ServicosViagemSchema>;

export type ViagemDTO = z.infer<typeof ViagemSchema>;

export type ViagemPersonalizadaStateDTO = z.infer<typeof ViagemPersonalizadaStateSchema>;

export type CriarViagemRequestDTO = z.infer<typeof CriarViagemRequestSchema>;
export type ViagemResponseDTO = z.infer<typeof ViagemResponseSchema>;
