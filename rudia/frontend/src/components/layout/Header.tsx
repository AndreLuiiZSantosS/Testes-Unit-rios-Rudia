'use client';

import Logo from '@/components/common/Logo/Logo';
import { ActiveLink } from '@/components/common/ActiveLink/ActiveLink';
import { ImagemUsuario } from '@/components/common/ImagemUsuario/ImagemUsuario';
import { Button } from '@/components/ui/button';
import { usePathname, useRouter } from 'next/navigation';
import { useAutenticacao } from '@/contexts/ContextoAutenticacao';

export default function Header() {
    const pathname = usePathname();
    const isHome = pathname === '/';

    const { usuario } = useAutenticacao();
    const router = useRouter();

    return (
        <header
            className={`
			${
                isHome
                    ? 'absolute top-0 left-0 right-0 z-50'
                    : 'fixed top-0 left-0 right-0 z-50'
            }
			mx-4 md:mx-16 lg:mx-60 flex items-center justify-between m-auto mt-2 py-4 px-6 rounded-2xl
			bg-white shadow-md
		`}
        >
            {/* Esquerda — Logo */}
            <div className="flex">
                <Logo width={112} height={30} />
            </div>

            {/* Centro — Nav */}
            <div className="flex items-center gap-10">
                <nav className="flex items-center gap-5">
                    <ActiveLink href="/viagem-personalizada">
                        Criar Viagem
                    </ActiveLink>
                    <ActiveLink href="#">Descobrir</ActiveLink>
                    <ActiveLink href="#">Comunidade</ActiveLink>
                </nav>
            </div>

            {/* Direita — Usuário ou Botão de Login */}
            <div className="flex">
                {usuario ? (
                    <ImagemUsuario />
                ) : (
                    <Button
                        onClick={() => router.push('/login')}
                        className="bg-amber-600 hover:bg-amber-700 cursor-pointer"
                    >
                        Entrar
                    </Button>
                )}
            </div>
        </header>
    );
}
