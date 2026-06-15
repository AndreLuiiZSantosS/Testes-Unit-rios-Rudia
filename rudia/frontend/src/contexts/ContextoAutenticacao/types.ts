import { LoginRequestDTO, UsuarioDTO } from '@/schemas/autenticacao.schema';

export interface IAutenticacaoContextType {
    // Valores
    usuario: UsuarioDTO | null;
    estaAutenticado: boolean;
    carregando: boolean;

    // Funções
    autenticar: (dados: LoginRequestDTO) => void;
    desconectar: () => void;
}
