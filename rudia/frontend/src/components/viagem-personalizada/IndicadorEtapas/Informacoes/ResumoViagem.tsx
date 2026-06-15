'use client';

import { useViagemPersonalizada } from '@/contexts/ContextoViagemPersonalizada';
import { useCidades } from '@/hooks/useCidades';
import { useMemo } from 'react';

export default function ResumoViagem() {
    const {
        state: { etapa, viagem },
    } = useViagemPersonalizada();

    const { cidades } = useCidades();

    const destino = useMemo(() => {
        return (
            cidades?.results.find(
                (cidade) => cidade.id === viagem.cidade_destino,
            )?.nome ?? 'Destino não selecionado'
        );
    }, [cidades, viagem.cidade_destino]);

    const totalViajantes = viagem.viajantes_adultos + viagem.viajantes_criancas;

    const labelViajantes = totalViajantes === 1 ? 'Rudiero' : 'Rudieros';

    const labelDias = !viagem.dias
        ? `0 dias`
        : viagem.dias > 1
          ? `${viagem.dias} dias`
          : `${viagem.dias} dia`;

    if (etapa === 1) {
        return (
            <p className="text-foreground text-sm">
                Planejando uma nova viagem
            </p>
        );
    }

    return (
        <p className="text-foreground text-sm">
            Viagem de <strong>{labelDias}</strong> para{' '}
            <strong>{destino}</strong> com{' '}
            <strong>
                {totalViajantes} {labelViajantes}
            </strong>
        </p>
    );
}
