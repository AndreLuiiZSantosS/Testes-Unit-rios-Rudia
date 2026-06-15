'use client';

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { ServicoParcialDTO } from '@/schemas/servico.schema';
import { EstrelasAvaliacao } from '@/lib/EstrelasAvaliacao';
import { formatarPreco } from '@/lib/formatacao';
import Image from 'next/image';

interface CardServicoProps {
    servico: ServicoParcialDTO;
    onClick: (servicoId: number) => void;
    selecionado?: boolean;
    className?: string;
}

export default function CardServico({
    servico,
    onClick,
    selecionado = false,
    className,
}: CardServicoProps) {
    return (
        <Card
            onClick={() => onClick(servico.id)}
            onKeyDown={(evento) =>
                evento.key === 'Enter' && onClick(servico.id)
            }
            tabIndex={0}
            role="button"
            aria-label={`Abrir detalhes do serviço ${servico.nome}`}
            aria-pressed={selecionado}
            className={`
                w-[220px] h-fit p-0 gap-0 rounded-sm overflow-hidden cursor-pointer transition-transform duration-300 ease-in-out hover:-translate-y-1,
                ${selecionado && 'border-2 border-amber-600'},
                ${className},
            `}
        >
            <figure className="relative w-[220px] h-[180px]">
                <Image
                    src={servico.imagem_capa_url}
                    alt={`Imagem do serviço ${servico.nome}`}
                    fill
                    unoptimized
                    priority
                    className="object-cover"
                />
            </figure>
            <CardHeader className="my-5 px-4 h-8">
                <CardTitle className="text-foreground text-lg">
                    {servico.nome}
                </CardTitle>
            </CardHeader>
            <CardContent className="flex items-center justify-between px-4 py-4 text-sm">
                <div className="flex gap-0.5">
                    {EstrelasAvaliacao(servico.avaliacao_geral)}
                </div>
                <p>{formatarPreco(servico.preco_medio)}</p>
            </CardContent>
        </Card>
    );
}
