import {
    FiltrosServico,
    obterServicosPorCategoria,
} from '@/api/servico/servico.fetch';
import { ServicosCategoriaResponseDTO } from '@/schemas/servico.schema';
import { useEffect, useMemo, useState } from 'react';
import { useCategoriasServico } from './useCategoriasServico';

export function useServicosPorCategoria(filtros: FiltrosServico) {
    const [servicos, setServicos] = useState<
        ServicosCategoriaResponseDTO | undefined
    >(undefined);
    const [carregando, setCarregando] = useState(true);
    const [erro, setErro] = useState<string | null>(null);

    const { categorias, carregando: carregandoCategorias } =
        useCategoriasServico();

    const { categoria, destino, viajantes } = filtros;
    const categoriaId = useMemo(() => {
        if (!categoria) return 0;
        return categorias.find((c) => c.nome === categoria)?.id ?? 0;
    }, [categorias, categoria]);

    useEffect(() => {
        if (carregandoCategorias) return;
        if (!categoriaId || !destino || !viajantes) return;

        async function carregarServicos() {
            try {
                setCarregando(true);
                setErro(null);
                setServicos(undefined);

                const resposta = await obterServicosPorCategoria({
                    categoria: categoriaId,
                    destino,
                    viajantes,
                });

                setServicos(resposta);
            } catch {
                setErro('Erro ao obter serviços');
            } finally {
                setCarregando(false);
            }
        }

        carregarServicos();
    }, [carregandoCategorias, categoriaId, destino, viajantes]);

    return { servicos, carregando, erro };
}
