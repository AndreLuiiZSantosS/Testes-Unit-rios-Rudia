'use client';

import { useViagemPersonalizada } from '@/contexts/ContextoViagemPersonalizada';

export function useNavegacaoEtapas() {
    const {
        state: { etapa },
        atualizarEtapa,
    } = useViagemPersonalizada();

    const avancar = (): string | null => {
        // Validar a etapa 1 antes de avançar
        if (etapa < 6) atualizarEtapa(etapa + 1);
        return null;
    };

    const voltar = () => {
        if (etapa > 1) atualizarEtapa(etapa - 1);
    };

    return {
        podeAvancar: etapa < 6,
        podeVoltar: etapa > 1,
        avancar,
        voltar,
    };
}