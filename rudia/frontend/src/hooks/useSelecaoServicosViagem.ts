'use client';

import { useViagemPersonalizada } from '@/contexts/ContextoViagemPersonalizada';

export function useSelecaoServicosViagem(categoria: string) {
    const {
        state: { viagem },
        atualizarAtributo,
    } = useViagemPersonalizada();

    const estaSelecionado = (servicoId: number): boolean => {
        switch (categoria) {
            case 'Hospedagem':
                return viagem.hospedagem === servicoId;
            case 'Lazer':
                return viagem.lazer.includes(servicoId);
            case 'Alimentação':
                return viagem.alimentacao.includes(servicoId);
            case 'Transporte':
                return viagem.transporte === servicoId;
            default:
                return false;
        }
    };

    const selecionarServico = (servicoId: number) => {
        switch (categoria) {
            case 'Hospedagem':
                atualizarAtributo(
                    'hospedagem',
                    viagem.hospedagem === servicoId ? null : servicoId,
                );
                break;
            case 'Lazer':
                atualizarAtributo(
                    'lazer',
                    viagem.lazer.includes(servicoId)
                        ? viagem.lazer.filter((id) => id !== servicoId)
                        : [...viagem.lazer, servicoId],
                );
                break;
            case 'Alimentação':
                atualizarAtributo(
                    'alimentacao',
                    viagem.alimentacao.includes(servicoId)
                        ? viagem.alimentacao.filter((id) => id !== servicoId)
                        : [...viagem.alimentacao, servicoId],
                );
                break;
            case 'Transporte':
                atualizarAtributo(
                    'transporte',
                    viagem.transporte === servicoId ? null : servicoId,
                );
                break;
        }
    };

    return { estaSelecionado, selecionarServico, viagem };
}