import { z } from 'zod';
import { criarListaSchema } from '@/lib/lista-schema';

// Schema Zod para Requisições

// Schema Zod para Respostas
export const SiglaUFSchema = z.enum([
    'AC', 'AL', 'AP', 'AM', 'BA',
    'CE', 'DF', 'ES', 'GO', 'MA',
    'MT', 'MS', 'MG', 'PA', 'PB',
    'PR', 'PE', 'PI', 'RJ', 'RN',
    'RS', 'RO', 'RR', 'SC', 'SP',
    'SE', 'TO',
]);

export const EstadoSchema = z.object({
    id: z.number(),
    nome: z.string(),
    sigla: SiglaUFSchema,
    total_cidades: z.number(),
});

export const CidadeSchema = z.object({
    id: z.number(),
    nome: z.string(),
    estado: EstadoSchema.omit({ total_cidades: true }),
    total_imagens: z.number(),
});

export const CidadeParcialSchema = CidadeSchema.pick({
    id: true,
    nome: true,
}).extend({ estado_sigla: SiglaUFSchema });

export const ListaCidadesResponseSchema = criarListaSchema(CidadeSchema);

export const ListaEstadosResponseSchema = criarListaSchema(EstadoSchema);

// Exportações dos Tipos DTO
export type SiglaUFDTO = z.infer<typeof SiglaUFSchema>;

export type CidadeDTO = z.infer<typeof CidadeSchema>;
export type CidadeParcialDTO = z.infer<typeof CidadeParcialSchema>;
export type EstadoDTO = z.infer<typeof EstadoSchema>;

export type ListaCidadesResponseDTO = z.infer<
    typeof ListaCidadesResponseSchema
>;
export type ListaEstadosResponseDTO = z.infer<
    typeof ListaEstadosResponseSchema
>;
