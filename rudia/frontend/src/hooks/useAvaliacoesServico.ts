'use client';

import { AvaliacaoDTO } from '@/schemas/geral.schema';
import { useEffect, useState } from 'react';

export function useAvaliacoesServico(
    servicoId: number | null,
    avaliacoesUrl: string | undefined,
) {
    const [avaliacoes, setAvaliacoes] = useState<AvaliacaoDTO[]>([]);
    const [carregando, setCarregando] = useState(false);
    const [erro, setErro] = useState<string | null>(null);

    useEffect(() => {
        if (!servicoId || !avaliacoesUrl) return;

        async function carregarAvaliacoes() {
            try {
                setCarregando(true);
                setErro(null);
                setAvaliacoes([]);

                const resposta = await fetch(avaliacoesUrl!, {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json' },
                });
                const dados = await resposta.json();
                setAvaliacoes(dados);
            } catch {
                setErro('Erro ao carregar avaliações.');
            } finally {
                setCarregando(false);
            }
        }

        carregarAvaliacoes();
    }, [servicoId, avaliacoesUrl]);

    return { avaliacoes, carregando, erro };
}
