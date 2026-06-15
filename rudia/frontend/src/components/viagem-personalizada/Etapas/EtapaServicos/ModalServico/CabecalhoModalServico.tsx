'use client';

import { DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Tooltip, TooltipTrigger } from '@/components/ui/tooltip';
import { Button } from '@/components/ui/button';
import { ServicoCompletoDTO } from '@/schemas/servico.schema';
import { formatarPreco } from '@/lib/formatacao';
import { EstrelasAvaliacao } from '@/lib/EstrelasAvaliacao';
import { MapPin } from 'lucide-react';
import Image from 'next/image';

interface CabecalhoModalServicoProps {
    servico: ServicoCompletoDTO;
    selecionado: boolean;
    onSelecionar: () => void;
}

export default function CabecalhoModalServico({
    servico,
    selecionado,
    onSelecionar,
}: CabecalhoModalServicoProps) {
    return (
        <DialogHeader className="flex-row gap-4">
            <figure className="relative w-[200px]">
                <Image
                    src={servico.imagem_capa_url}
                    alt={`Imagem do serviço ${servico.nome}`}
                    fill
                    unoptimized
                    priority
                    className="object-cover"
                />
            </figure>

            <div className="space-y-2">
                <div className="flex items-center gap-3">
                    <DialogTitle className="text-2xl">
                        {servico.nome}
                    </DialogTitle>
                    <p className="text-sm font-normal">
                        {servico.categoria.nome}
                    </p>
                </div>

                <p className="flex gap-1 text-sm">
                    <MapPin className="size-5" aria-hidden="true" />
                    {servico.endereco.endereco_completo}
                </p>

                <p className="flex my-3 gap-0.5">
                    {EstrelasAvaliacao(servico.avaliacoes_resumo.media_geral)}
                </p>

                <ul className="flex items-center gap-2">
                    {servico.tags.map((tag) => (
                        <Tooltip key={tag.id}>
                            <TooltipTrigger asChild>
                                <li className="bg-zinc-100 p-1.5 text-xs rounded-lg cursor-pointer">
                                    {tag.nome}
                                </li>
                            </TooltipTrigger>
                        </Tooltip>
                    ))}
                </ul>

                <div className="flex items-center my-3 gap-2">
                    <p className="text-2xl font-bold">
                        {formatarPreco(servico.preco_medio)}
                    </p>
                    <p className="text-xs">Preço Médio</p>
                </div>

                <div className="flex items-center gap-2">
                    <Button
                        onClick={onSelecionar}
                        variant="default"
                        type="button"
                        size="sm"
                        className="text-xs text-white cursor-pointer border-0"
                        style={{
                            backgroundColor: selecionado
                                ? '#1D632E'
                                : '#E56C00',
                        }}
                    >
                        {selecionado ? 'Selecionado' : 'Selecionar'}
                    </Button>
                </div>
            </div>
        </DialogHeader>
    );
}
