import {
    ACCESS_TOKEN,
    REFRESH_TOKEN,
    USER_ID,
    USER_SESSION,
} from '@/api/ApiConfig';
import { NextRequest } from 'next/server';

export interface UserSession {
    id: number | string;
    username: string;
}

export interface AuthTokens {
    access: string;
    refresh: string;
    usuarioId?: number | string;
}

const SESSION_MAX_AGE_SECONDS = 7 * 24 * 60 * 60; // 7 dias

// Funções auxiliares (LocalStorage)
export const obterTokens = (type: 'ACCESS' | 'REFRESH') => {
    return localStorage.getItem(
        type === 'ACCESS' ? ACCESS_TOKEN : REFRESH_TOKEN,
    );
};

export const guardarTokens = (tokens: AuthTokens): void => {
    localStorage.setItem(ACCESS_TOKEN, tokens.access);
    localStorage.setItem(REFRESH_TOKEN, tokens.refresh);

    if (tokens.usuarioId)
        localStorage.setItem(USER_ID, tokens.usuarioId.toString());
};

export const removerTokens = (): void => {
    localStorage.removeItem(ACCESS_TOKEN);
    localStorage.removeItem(REFRESH_TOKEN);
    localStorage.removeItem(USER_ID);
};

// Funções auxiliares (Cookies)
const converterCookieSessao = (value?: string) => {
    try {
        if (!value) return null;

        // Decodificar e Obter o Usuário da Sessão
        const decoded = decodeURIComponent(value);
        const session = JSON.parse(decoded) satisfies UserSession;

        if (!session?.id || !session?.username) return null;
        return session;
    } catch {
        return null;
    }
};

export const obterCookieSessao = (request: NextRequest) => {
    const value = request.cookies.get(USER_SESSION)?.value;
    return converterCookieSessao(value);
};
export const sessaoEstaAtiva = (request: NextRequest) => {
    return Boolean(obterCookieSessao(request));
};

// Set e Delete (Cookies)
export const guardarCookieSessao = (user: UserSession) => {
    if (typeof document === 'undefined') return;
    const secure =
        typeof window !== 'undefined' && window.location.protocol === 'https:'
            ? '; secure'
            : '';
    const value = encodeURIComponent(JSON.stringify(user));
    document.cookie = `${USER_SESSION}=${value}; path=/; samesite=strict; max-age=${SESSION_MAX_AGE_SECONDS}${secure}`;
};

export const removerCookieSessao = () => {
    if (typeof document === 'undefined') return;
    const secure =
        typeof window !== 'undefined' && window.location.protocol === 'https:'
            ? '; secure'
            : '';
    document.cookie = `${USER_SESSION}=; path=/; samesite=strict; max-age=0${secure}`;
};

// Funções combinadas para login/logout
export const iniciarSessao = (user: UserSession, tokens: AuthTokens) => {
    guardarCookieSessao(user);
    guardarTokens(tokens);
};

export const encerrarSessao = () => {
    removerCookieSessao();
    removerTokens();
}
