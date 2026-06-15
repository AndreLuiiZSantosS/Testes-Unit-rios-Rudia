import { z } from 'zod';

// Criar dinamicamente os Schemas Zod para listagem
export const criarListaSchema = <T extends z.ZodType>(schema: T) => {
    return z.object({
        count: z.number(),
        results: schema.array(),
    });
};
