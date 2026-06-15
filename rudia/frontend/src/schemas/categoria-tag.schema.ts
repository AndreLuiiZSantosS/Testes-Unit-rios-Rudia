import { z } from 'zod';
import { criarListaSchema } from '@/lib/lista-schema';

// Schema Zod para Requisições

// Schema Zod para Respostas
export const CategoriaTypeSchema = z.enum([
    'Hospedagem',
    'Lazer',
    'Alimentação',
    'Transporte',
]);

export const TagSchema = z.object({
    id: z.number(),
    nome: z.string(),
});

export const CategoriaSchema = z.object({
    id: z.number(),
    nome: CategoriaTypeSchema,
    total_servicos: z.number(),
});

export const CategoriaParcialSchema = CategoriaSchema.omit({
    total_servicos: true,
});

export const ListaCategoriasResponseSchema = criarListaSchema(CategoriaSchema);

export const ListaTagsResponseSchema = criarListaSchema(TagSchema);

// Exportações dos Tipos DTO
export type CategoriaTypeDTO = z.infer<typeof CategoriaTypeSchema>;

export type CategoriaDTO = z.infer<typeof CategoriaSchema>;
export type CategoriaParcialDTO = z.infer<typeof CategoriaParcialSchema>;
export type TagDTO = z.infer<typeof TagSchema>;

export type ListaCategoriasResponseDTO = z.infer<
    typeof ListaCategoriasResponseSchema
>;
export type ListaTagResponseDTO = z.infer<typeof ListaTagsResponseSchema>;
