'use client';

import AreaFiltros from './AssetsServico/AreaFiltros';
import ListaServicos from './AssetsServico/ListaServicos';
import ModalCardServico from './ModalServico/ModalCardServico';
import { useViagemPersonalizada } from '@/contexts/ContextoViagemPersonalizada';
import { useServicosPorCategoria } from '@/hooks/useServicosPorCategoria';
import { useSelecaoServicosViagem } from '@/hooks/useSelecaoServicosViagem';
import { HEADER_CONTEUDO_SERVICO } from './EtapaServicoUtils';
import { useState } from 'react';

export default function EtapaCategoriaServico() {
    const [servicoSelecionado, setServicoSelecionado] = useState<number | null>(
        null,
    );

    const {
        state: { etapa, viagem },
    } = useViagemPersonalizada();

    const { cidade_destino, viajantes_adultos, viajantes_criancas } = viagem;
    const { titulo, placeholder, categoria } = HEADER_CONTEUDO_SERVICO[etapa];

    const { servicos, carregando: carregandoServicos } =
        useServicosPorCategoria({
            categoria: categoria,
            destino: cidade_destino ?? 0,
            viajantes: viajantes_adultos + viajantes_criancas,
        });

    const { estaSelecionado } = useSelecaoServicosViagem(categoria);

    return (
        <div className="flex flex-col mt-10 space-y-6">
            <h1 className="text-xl text-center">{titulo}</h1>

            <AreaFiltros placeholder={placeholder} />

            <div className="flex flex-wrap w-[220px] md:w-[460px] lg:w-[700px] m-auto mt-8 gap-5">
                <ListaServicos
                    servicos={servicos?.servicos}
                    carregando={carregandoServicos}
                    estaSelecionado={estaSelecionado}
                    onCardClick={setServicoSelecionado}
                />
            </div>

            <ModalCardServico
                servicoId={servicoSelecionado}
                onClose={() => setServicoSelecionado(null)}
            />
        </div>
    );
}
