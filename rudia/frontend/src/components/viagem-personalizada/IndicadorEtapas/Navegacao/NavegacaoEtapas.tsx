'use client';

import { Button } from '@/components/ui/button';
import ItemEtapa from './ItemEtapa';
import ConectorEtapas from './ConectorEtapas';
import {
    ETAPAS,
    CLASSES_BASE_ICONES,
    CirculoStatus,
    LinhaStatus,
} from '../ProgressoUtils';
import { useViagemPersonalizada } from '@/contexts/ContextoViagemPersonalizada';
import { useNavegacaoEtapas } from '@/hooks/useNavegacaoViagemPersonalizada';
import { Fragment } from 'react';
import { ArrowLeft, ArrowRight } from 'lucide-react';

export default function NavegacaoEtapas() {
    const {
        state: { etapa, viagem },
    } = useViagemPersonalizada();

    const { podeAvancar, podeVoltar, avancar, voltar } = useNavegacaoEtapas();

    const resolverStatusCirculo = (
        id: number,
        concluida: boolean,
    ): CirculoStatus => {
        if (etapa === id) return 'atual';
        if (etapa > id && concluida) return 'concluida';
        return 'pendente';
    };

    const resolverStatusLinha = (
        id: number,
        concluida: boolean,
        proximaConcluida: boolean,
    ): LinhaStatus => {
        const proximaEtapa = id + 1;

        if (etapa === proximaEtapa) {
            return concluida ? 'concluida_atual' : 'pendente_atual';
        }

        if (etapa > proximaEtapa) {
            return concluida
                ? 'concluida'
                : proximaConcluida
                  ? 'pendente_concluida'
                  : 'pendente';
        }

        return 'pendente';
    };

    return (
        <div className="flex justify-center items-center gap-2">
            <Button
                variant="ghost"
                size="icon-sm"
                className="hover:bg-transparent cursor-pointer"
                onClick={voltar}
                disabled={!podeVoltar}
            >
                <ArrowLeft className={CLASSES_BASE_ICONES} />
            </Button>

            <div className="flex justify-center items-center">
                {ETAPAS.map((item, index) => {
                    const isUltima = index === ETAPAS.length - 1;
                    const concluida = item.check(viagem);

                    return (
                        <Fragment key={item.id}>
                            <ItemEtapa
                                icon={item.icon}
                                status={resolverStatusCirculo(
                                    item.id,
                                    concluida,
                                )}
                            />
                            {!isUltima && (
                                <ConectorEtapas
                                    status={resolverStatusLinha(
                                        item.id,
                                        concluida,
                                        ETAPAS[index + 1].check(viagem),
                                    )}
                                />
                            )}
                        </Fragment>
                    );
                })}
            </div>

            <Button
                variant="ghost"
                size="icon-sm"
                className="hover:bg-transparent cursor-pointer"
                onClick={avancar}
                disabled={!podeAvancar}
            >
                <ArrowRight className={CLASSES_BASE_ICONES} />
            </Button>
        </div>
    );
}
