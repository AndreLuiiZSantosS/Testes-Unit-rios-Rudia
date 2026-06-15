'use client';

import FormFieldPattern from '@/components/common/CamposFormularios/FormFieldPattern';
import Logo from '@/components/common/Logo/Logo';
import { Button } from '@/components/ui/button';
import { Form } from '@/components/ui/form';
import { useAutenticacao } from '@/contexts/ContextoAutenticacao';
import {
    LoginRequestDTO,
    LoginRequestSchema,
} from '@/schemas/autenticacao.schema';
import { zodResolver } from '@hookform/resolvers/zod';
import { EyeIcon, EyeOff, Mail } from 'lucide-react';
import Link from 'next/link';
import { useSearchParams, useRouter } from 'next/navigation';
import { ReactNode, useState } from 'react';
import { useForm } from 'react-hook-form';

interface FormularioLoginProps {
    className?: string;
}

export default function FormularioLogin({ ...props }: FormularioLoginProps) {
    const [senhaEscondida, setSenhaEscondida] = useState<
        'Escondida' | 'Visivel'
    >('Escondida');
    const [carregando, setCarregando] = useState<boolean>(false);

    const { autenticar } = useAutenticacao();

    const router = useRouter();
    const searchParams = useSearchParams();
    const redirectUrl = searchParams.get('redirect');

    const form = useForm<LoginRequestDTO>({
        resolver: zodResolver(LoginRequestSchema),
        defaultValues: { email: '', password: '' },
    });

    const logar = async (dados: LoginRequestDTO) => {
        setCarregando(true);
        await autenticar(dados);
        router.replace(redirectUrl ?? '/');
        setCarregando(false);
    };

    const textClass = 'text-xs';
    const iconClass = 'text-muted-foreground w-4 h-4';

    const senhaIcon: Record<string, { type: string; icon: ReactNode }> = {
        Escondida: {
            type: 'password',
            icon: (
                <EyeOff
                    className={iconClass}
                    onClick={() => setSenhaEscondida('Visivel')}
                />
            ),
        },
        Visivel: {
            type: 'text',
            icon: (
                <EyeIcon
                    className={iconClass}
                    onClick={() => setSenhaEscondida('Escondida')}
                />
            ),
        },
    };

    return (
        <div className={`flex flex-col h-full space-y-5 ${props.className}`}>
            <Form {...form}>
                {/* Cabeçalho do Formulário */}
                <div className="flex flex-col gap-6 mb-6">
                    <div className="m-auto">
                        <Logo width={150} height={75} />
                    </div>
                    <div className="flex flex-col gap-0.5 items-start">
                        <span className="text-3xl font-bold">Faça Login</span>
                        <p className="text-sm text-muted-foreground">
                            Bem-vindo de volta!
                        </p>
                    </div>
                </div>

                <form
                    onSubmit={form.handleSubmit(logar)}
                    className="space-y-4 flex flex-col"
                >
                    {/* Campo de E-mail */}
                    <FormFieldPattern
                        control={form.control}
                        field="email"
                        label={<p className={textClass}>E-mail</p>}
                        placeholder="Digite seu endereço de e-mail"
                        leftIcon={<Mail className={iconClass} />}
                        className={textClass}
                        loading={carregando}
                    />

                    {/* Campo de Senha */}
                    <FormFieldPattern
                        control={form.control}
                        field="password"
                        type={senhaIcon[senhaEscondida].type}
                        label={<p className={textClass}>Senha</p>}
                        placeholder="Digite sua senha"
                        rightIcon={senhaIcon[senhaEscondida].icon}
                        className={textClass}
                        loading={carregando}
                    />

                    {/* Trocar a Senha
                    <Link
                        href="#"
                        className="text-[12px] text-end text-amber-600"
                    >
                        Esqueceu a senha?
                    </Link> */}

                    {/* Botão de Submit */}
                    <Button
                        variant="default"
                        size="lg"
                        className="bg-amber-600 hover:bg-amber-700 my-5 py-5 cursor-pointer"
                        type="submit"
                        disabled={carregando}
                    >
                        {carregando ? 'Carregando...' : 'Entrar'}
                    </Button>

                    <p className="flex gap-1 text-xs">
                        <span>Não possui uma conta?</span>
                        <Link
                            href={carregando ? '#' : '/cadastro'}
                            className="text-amber-600"
                        >
                            Criar uma conta
                        </Link>
                    </p>
                </form>
            </Form>
        </div>
    );
}
