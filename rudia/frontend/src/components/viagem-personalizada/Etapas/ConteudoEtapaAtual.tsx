'use client';

import EtapaDadosIniciais from './EtapaInicial';
import EtapaCategoriaServico from './EtapaServicos';
import EtapaDadosFinais from './EtapaFinal';
import { useViagemPersonalizada } from '@/contexts/ContextoViagemPersonalizada';

export default function ConteudoEtapaAtual() {
    const {
        state: { etapa },
    } = useViagemPersonalizada();

    function renderizarEtapa(etapa: number) {
        switch (true) {
            case etapa === 1:
                return <EtapaDadosIniciais />;
            case etapa >= 2 && etapa <= 5:
                return <EtapaCategoriaServico />;
            case etapa === 6:
                return <EtapaDadosFinais />;
            default:
                return null;
        }
    }

    return <div className="w-full">{renderizarEtapa(etapa)}</div>;
}
