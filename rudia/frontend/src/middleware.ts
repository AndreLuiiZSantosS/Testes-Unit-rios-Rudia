import type { NextRequest } from 'next/server';
import { NextResponse } from 'next/server';
import { sessaoEstaAtiva } from '@/api/autenticacao/utils';

export const ROTAS_PUBLICAS = ['/', '/login', '/cadastro'];

export function middleware(request: NextRequest) {
    // const session = sessaoEstaAtiva(request);
    // const pathname = request.nextUrl.pathname;
    // const ehRotaPublica = ROTAS_PUBLICAS.includes(pathname);

    // // 1️⃣ Tentou acessar rota privada sem login
    // if (!ehRotaPublica && !session) {
    //     const loginUrl = new URL('/login', request.url);
    //     // guarda a rota original
    //     loginUrl.searchParams.set('redirect', pathname);
    //     return NextResponse.redirect(loginUrl);
    // }

    // // 2️⃣ Tentou acessar login/cadastro estando logado
    // if (session && (pathname === '/login' || pathname === '/cadastro')) {
    //     return NextResponse.redirect(new URL('/', request.url));
    // }
    
    // return NextResponse.next();
}

export const config = {
    matcher: [
        '/((?!api|_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',
    ],
};
