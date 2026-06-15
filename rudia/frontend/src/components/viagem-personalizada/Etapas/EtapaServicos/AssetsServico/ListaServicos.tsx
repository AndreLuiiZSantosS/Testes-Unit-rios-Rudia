'use client';

import CardServico from './CardServico';
import { Spinner } from '@/components/ui/spinner';
import { ServicoParcialDTO } from '@/schemas/servico.schema';

interface ListaServicosProps {
    servicos: ServicoParcialDTO[] | undefined;
    carregando: boolean;
    estaSelecionado: (id: number) => boolean;
    onCardClick: (id: number) => void;
}

export default function ListaServicos({
    servicos,
    carregando,
    estaSelecionado,
    onCardClick,
}: ListaServicosProps) {
    if (carregando) {
        return <Spinner className="text-amber-600 size-10 w-full" />;
    }

    return (
        <>
            {servicos?.map((servico) => (
                <CardServico
                    key={servico.id}
                    servico={servico}
                    onClick={onCardClick}
                    selecionado={estaSelecionado(servico.id)}
                />
            ))}
        </>
    );
}
