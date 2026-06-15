import { z } from 'zod';

// Schema Zod para Requisições
export const LoginRequestSchema = z.object({
    email: z
        .string()
        .trim()
        .nonempty('Informe o seu E-mail para acessar a conta.')
        .email({
            pattern: z.regexes.html5Email,
            message:
                'O formato do E-mail digitado é inválido. Ex: nome@dominio.com',
        }),
    password: z
        .string()
        .trim()
        .nonempty('Informe sua Senha para acessar a conta.'),
});

// Schema Zod para Respostas
const UsuarioTypeSchema = z.enum([
    'RUDIERO',
    'PARCEIRO',
    'ADMINISTRADOR',
    'MODERADOR',
]);
const UsuarioDisplaySchema = z.enum([
    'Rudiero',
    'Parceiro',
    'Administrador',
    'Moderador',
]);

export const UsuarioSchema = z.object({
    id: z.number(),
    nome: z.string(),
    username: z.string(),
    email: z.string().email(),
    telefone: z.string().nullish(),
    foto_perfil: z.string().url().nullish(),
    url_instagram: z.string().url().nullish(),
    url_facebook: z.string().url().nullish(),
    url_x: z.string().url().nullish(),
    url_tiktok: z.string().url().nullish(),
    date_joined: z.iso.datetime({ offset: true }),
    last_login: z.iso.datetime({ offset: true }).nullish(),
    tipo_usuario: UsuarioTypeSchema,
    tipo_usuario_display: UsuarioDisplaySchema,
});

export const RefreshResponseSchema = z.object({
    access: z.string(),
    refresh: z.string(),
});

export const LoginResponseSchema = RefreshResponseSchema.extend({
    user: UsuarioSchema,
});

// Exportações dos Tipos DTO
export type UsuarioDTO = z.infer<typeof UsuarioSchema>;

export type LoginRequestDTO = z.infer<typeof LoginRequestSchema>;
export type LoginResponseDTO = z.infer<typeof LoginResponseSchema>;

export type RefreshResponseDTO = z.infer<typeof RefreshResponseSchema>;
