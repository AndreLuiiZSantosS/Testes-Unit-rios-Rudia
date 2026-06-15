// Apenas para Schemas que podem ser usados por mais de um modulo (Sem Especificidade)
import { z } from 'zod';

// Criação dos Schemas Zod
export const StatusTypeSchema = z.enum(['EA', 'AP', 'RP']);
export const StatusDisplaySchema = z.enum([
    'Em Análise',
    'Aprovada',
    'Reprovada',
]);

export const PropostaStatusSchema = z.object({
    status: StatusDisplaySchema,
    data_criacao: z.iso.datetime(),
    comentario_moderador: z.string().nullish(),
});

export const PaginatorSchema = z.object({
    page: z.number(),
    size: z.number(),
    total_pages: z.number(),
    total_items: z.number(),
    has_next: z.boolean(),
    has_previous: z.boolean(),
    next_page: z.number().nullish(),
    previous_page: z.number().nullish(),
});

export const AvaliacaoSchema = z.object({
    id: z.number(),
    nota: z.coerce.number(),
    comentario: z.string(),
    rudiero_username: z.string(),
    rudiero_nome: z.string(),
    rudiero_foto: z.string().nullish(),
    data_avaliacao: z.iso.datetime({ offset: true }),
});

// Quantidade de Avaliações para cada Tipo (⭐, ⭐, ⭐, ⭐, ⭐)
export const DistribuicaoAvaliacoesSchema = z.object({
    cinco_estrelas: z.number(),
    quatro_estrelas: z.number(),
    tres_estrelas: z.number(),
    dois_estrelas: z.number(),
    uma_estrela: z.number(),
});

export const ResumoAvalicoesSchema = z.object({
    media_geral: z.number(),
    total: z.number(),
    distribuicao: DistribuicaoAvaliacoesSchema,
});

export const VisibilidadeTypeSchema = z.enum(['PUBLICO', 'PRIVADO']);
export const VisibilidadeDisplaySchema = z.enum(['Público', 'Privado']);

// Exportações dos Tipos DTO
export type StatusTypeDTO = z.infer<typeof StatusTypeSchema>;
export type StatusDisplayDTO = z.infer<typeof StatusDisplaySchema>;

export type PropostaStatusDTO = z.infer<typeof PropostaStatusSchema>;

export type PaginatorDTO = z.infer<typeof PaginatorSchema>;

export type AvaliacaoDTO = z.infer<typeof AvaliacaoSchema>;
export type ResumoAvalicoesDTO = z.infer<typeof ResumoAvalicoesSchema>;
export type DistribuicaoAvaliacoesDTO = z.infer<
    typeof DistribuicaoAvaliacoesSchema
>;

export type VisibilidadeTypeDTO = z.infer<typeof VisibilidadeTypeSchema>;
export type VisibilidadeDisplayDTO = z.infer<typeof VisibilidadeDisplaySchema>;
