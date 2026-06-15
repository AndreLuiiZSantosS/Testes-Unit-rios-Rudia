import { z } from 'zod';
import { UsuarioSchema } from './autenticacao.schema';
import { PropostaStatusSchema } from './geral.schema';
import { RegistroRudieroRequestSchema } from './registro-rudiero.schema';

// Schema Zod para Requisições
export const PropostaParceriaRequestSchema = RegistroRudieroRequestSchema.pick({
    username: true,
    email: true,
    password: true,
    password_confirm: true,
}).extend({
    nome: z.string().trim().nonempty('O Nome da Empresa é obrigatório.'),
    cnpj: z.string().min(14, 'CNPJ inválido').max(18, 'CNPJ inválido'),
});

export const PropostaParceriaFormSchema = PropostaParceriaRequestSchema.omit({
    username: true,
});

// Schema Zod para Respostas
export const ParceiroSchema = UsuarioSchema.omit({
    tipo_usuario: true,
    tipo_usuario_display: true,
}).extend({
    cnpj: z.string(),
    ativo: z.boolean(),
    data_admissao: z.string().nullish(),
    proposta_status: PropostaStatusSchema,
});

export const PropostaParceriaResponseSchema = z.object({
    message: z.string(),
    parceiro: ParceiroSchema,
});

// Exportações dos Tipos DTO
export type ParceiroDTO = z.infer<typeof ParceiroSchema>;

export type PropostaParceriaRequestDTO = z.infer<
    typeof PropostaParceriaRequestSchema
>;
export type PropostaParceriaResponseDTO = z.infer<
    typeof PropostaParceriaResponseSchema
>;

export type PropostaParceriaFormDTO = z.infer<
    typeof PropostaParceriaFormSchema
>;
