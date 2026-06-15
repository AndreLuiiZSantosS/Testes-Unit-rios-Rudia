'use client';

import Header from '@/components/layout/Header';
import ConteudoEtapaAtual from '@/components/viagem-personalizada/Etapas';
import IndicadorEtapas from '@/components/viagem-personalizada/IndicadorEtapas';
import { ViagemPersonalizadaProvider } from '@/contexts/ContextoViagemPersonalizada';

export default function PaginaCriarViagemPersonalizada() {
    return (
        <ViagemPersonalizadaProvider>
            <div className="flex flex-col w-fit m-auto my-28">
                <Header />
                <IndicadorEtapas />
                {/* AQUI COLOCAR OS ERROS NA TELA PARA O USUÁRIO */}
                <ConteudoEtapaAtual />
            </div>
        </ViagemPersonalizadaProvider>
    );
}
