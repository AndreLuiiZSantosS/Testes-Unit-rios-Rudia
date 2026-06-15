import { obterCategoriasServico } from '@/api/servico/categoria.fetch';
import { CategoriaDTO } from '@/schemas/categoria-tag.schema';
import { useEffect, useState } from 'react';

export function useCategoriasServico() {
    const [categorias, setCategorias] = useState<CategoriaDTO[]>([]);
    const [carregando, setCarregando] = useState<boolean>(true);
    const [erro, setErro] = useState<string | null>(null);

    useEffect(() => {
        const carregarCategorias = async () => {
            try {
                setCarregando(true);
                setErro(null);
                setCategorias([]);

                const resposta = await obterCategoriasServico();
                const categorias = resposta.results;

                setCategorias(categorias);
            } catch (error) {
                setErro('Ocorreu um erro ao buscar as categorias de serviço');
            } finally {
                setCarregando(false);
            }
        };

        carregarCategorias();
    }, []);

    return { categorias, carregando, erro };
}
