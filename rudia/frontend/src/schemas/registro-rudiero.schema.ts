import { z } from 'zod';
import { UsuarioSchema } from './autenticacao.schema';

const usernameRegex = /^(?=(?:.*[A-Za-z]){3,})[A-Za-z0-9_]+$/;
const passwordRegex =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%&*_+.-])(?!.*\s).+$/;

// Schema Zod para Requisições
export const RegistroRudieroRequestSchema = z
    .object({
        username: z
            .string()
            .trim()
            .nonempty('O Username é obrigatório.')
            .min(6, 'O Username está muito curto. Use no mínimo 6 caracteres.')
            .max(
                150,
                'O Username está muito longo. Use no máximo 150 caracteres.',
            )
            .refine(
                (v) => usernameRegex.test(v),
                'O Username deve ter pelo menos 3 letras, e pode conter apenas letras e números (sem espaços ou caracteres especiais).',
            ),

        email: z.string().trim().nonempty('O E-mail é obrigatório.').email({
            pattern: z.regexes.html5Email,
            message:
                'O formato do E-mail digitado é inválido. Ex: nome@dominio.com',
        }),

        nome: z
            .string()
            .trim()
            .nonempty('O Nome Completo é obrigatório.')
            .refine(
                (fullName) => fullName.trim().split(' ').length >= 2,
                'Informe seu Nome e Sobrenome.',
            )
            .refine(
                (fullName) => /^[A-Za-zÀ-ú ]+$/.test(fullName),
                'O Nome Completo deve conter apenas letras e espaços.',
            ),

        password: z
            .string()
            .nonempty('A Senha é obrigatória.')
            .min(8, 'A Senha está muito curta. Use no mínimo 8 caracteres.')
            .max(120, 'A Senha está muito longa. Use no máximo 120 caracteres.')
            .refine(
                (v) => passwordRegex.test(v),
                'A Senha é fraca e/ou possui caracteres inválidos.',
            ),

        password_confirm: z
            .string()
            .nonempty('Confirme a senha digitando-a novamente.'),

        data_nascimento: z
            .string()
            .nonempty('A Data de Nascimento é obrigatória')
            .refine((value) => {
                const date = new Date(value);
                if (Number.isNaN(date.getTime())) {
                    return false;
                }
                const today = new Date();
                const adultDate = new Date(
                    today.getFullYear() - 16,
                    today.getMonth(),
                    today.getDate(),
                );
                return date <= adultDate;
            }, 'Você precisa ter 16 anos ou mais.'),
    })
    .refine((data) => data.password === data.password_confirm, {
        message: 'As Senhas digitadas não coincidem. Verifique a confirmação.',
        path: ['password_confirm'],
    });

export const RegistroRudieroFormSchema = RegistroRudieroRequestSchema.omit({
    username: true,
});

// Schema Zod para Respostas
export const GeneroTypeSchema = z.enum(['M', 'F', 'O', 'N']);
export const GeneroDisplaySchema = z.enum([
    'Masculino',
    'Feminino',
    'Outro',
    'Prefiro Não Informar',
]);

export const RudieroSchema = UsuarioSchema.omit({
    tipo_usuario: true,
    tipo_usuario_display: true,
}).extend({
    data_nascimento: z.iso.date(),
    genero: GeneroTypeSchema,
    genero_display: GeneroDisplaySchema,
});

export const RegistroRudieroResponseSchema = z.object({
    message: z.string(),
    rudiero: RudieroSchema,
});

// Exportações dos Tipos DTO
export type GeneroTypeDTO = z.infer<typeof GeneroTypeSchema>;
export type GeneroDisplayDTO = z.infer<typeof GeneroDisplaySchema>;

export type RudieroDTO = z.infer<typeof RudieroSchema>;

export type RegistroRudieroRequestDTO = z.infer<
    typeof RegistroRudieroRequestSchema
>;
export type RegistroRudieroResponseDTO = z.infer<
    typeof RegistroRudieroResponseSchema
>;

export type RegistroRudieroFormDTO = z.infer<typeof RegistroRudieroFormSchema>;
