'use client';

import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
} from '@/components/ui/select';
import { useViagemPersonalizada } from '@/contexts/ContextoViagemPersonalizada';
import { useCidades } from '@/hooks/useCidades';
import { CidadeDTO } from '@/schemas/cidade-estado.schema';
import { ReactNode } from 'react';
import { MapPin } from 'lucide-react';

export default function InputDestino() {
    const { cidades, carregando, erro } = useCidades();

    const {
        state: { viagem },
        atualizarAtributo,
    } = useViagemPersonalizada();

    const cidadeSelecionada = cidades?.results.find(
        (cidade) => cidade.id === viagem.cidade_destino,
    );

    const EstadoCampo: Record<
        'LOADING' | 'FAIL' | 'RENDERING',
        { componente: ReactNode; estilo: string }
    > = {
        LOADING: {
            componente: (
                <span className="text-sm text-muted-foreground">
                    Carregando...
                </span>
            ),
            estilo: 'text-muted-foreground',
        },

        FAIL: {
            componente: (
                <span className="text-sm text-red-600">
                    Erro ao carregar cidades
                </span>
            ),
            estilo: 'text-red-600',
        },

        RENDERING: {
            componente: (
                <span
                    className={`text-sm ${viagem.cidade_destino ? 'text-amber-600' : 'text-muted-foreground'}`}
                >
                    {cidadeSelecionada ? cidadeSelecionada.nome : 'Onde'}
                </span>
            ),
            estilo: 'text-amber-600',
        },
    };

    const estadoAtual = carregando ? 'LOADING' : erro ? 'FAIL' : 'RENDERING';
    const estiloAtual =
        estadoAtual === 'RENDERING' && viagem.cidade_destino
            ? estadoAtual
            : 'LOADING';

    return (
        <Select
            value={viagem.cidade_destino?.toString() ?? undefined}
            onValueChange={(cidadeId) =>
                atualizarAtributo('cidade_destino', parseInt(cidadeId))
            }
            disabled={carregando || !!erro}
        >
            <SelectTrigger className="bg-neutral-100 border-none focus-visible:ring-0 focus:outline-none cursor-pointer">
                <MapPin
                    className={`size-4 ${EstadoCampo[estiloAtual].estilo}`}
                />
                {EstadoCampo[estadoAtual].componente}
            </SelectTrigger>

            <SelectContent>
                <SelectItem value="Not Value">Selecione a Cidade</SelectItem>
                {cidades &&
                    cidades.results.map((cidade: CidadeDTO) => (
                        <SelectItem key={cidade.id} value={`${cidade.id}`}>
                            {cidade.nome}
                        </SelectItem>
                    ))}
            </SelectContent>
        </Select>
    );
}
