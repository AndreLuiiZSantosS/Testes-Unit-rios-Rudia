// URL BASE DA API
export const URL_BASE_API =
    process.env.URL_BASE_API || 'http://127.0.0.1:8000/api';

// LOCAL STORAGE KEYS
export const ACCESS_TOKEN = process.env.ACCESS_TOKEN || 'access';
export const REFRESH_TOKEN = process.env.REFRESH_TOKEN || 'refresh';
export const USER_ID = process.env.USER_ID || 'user';
export const USER_SESSION = process.env.USER_SESSION || 'user_session';

// ENDPOINTS
export const ENDPOINTS = {
    LOGIN: '/usuarios/auth/login/',
    REGISTRO_RUDIERO: '/usuarios/rudieros/registro/',
    REGISTRO_PARCEIRO: '/usuarios/parceiros/registro/',
    REGISTRO_MODERADOR: '/usuarios/moderadores/registro/',
    REGISTRO_ADM: '/usuarios/administradores/registro/',
    LOGOUT: '/usuarios/auth/logout/',
    REFRESH: '/usuarios/auth/refresh/',
    ME: '/usuarios/auth/me/',

    CIDADES: '/localizacao/cidades/',
    ESTADOS: '/localizacao/estados/',

    SERVICO_POR_ID: '/servicos/',
    SERVICOS_POR_CATEGORIA: '/servicos/categoria/',
    CATEGORIAS_SERVICO: '/servicos/categorias/',
    REGISTRO_SERVICO: '/propostas-servico/',

    VIAGEM: '/viagens/',
};
