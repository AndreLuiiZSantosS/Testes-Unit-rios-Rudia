'use client';

import { Card, CardContent, CardHeader } from '@/components/ui/card';
import { EstrelasAvaliacao } from '@/lib/EstrelasAvaliacao';
import { AvaliacaoDTO } from '@/schemas/geral.schema';

interface CardAvaliacaoProps {
    avaliacao: AvaliacaoDTO;
}

export default function CardAvaliacao({ avaliacao }: CardAvaliacaoProps) {
    return (
        <Card className="w-56 h-32 shrink-0 p-4 cursor-pointer gap-0 hover:-translate-y-1">
            <CardHeader className="flex items-center justify-start p-0 gap-2">
                <div
                    className="flex items-center justify-center bg-zinc-300 w-6 h-6 rounded-full overflow-hidden"
                    aria-hidden="true"
                />
                <h3 className="text-sm">{avaliacao.rudiero_nome}</h3>
            </CardHeader>
            <CardContent className="p-0 space-y-1 mt-3">
                <blockquote className="text-xs h-12 overflow-auto">
                    "{avaliacao.comentario}"
                </blockquote>
                <div
                    className="flex justify-end gap-0.5"
                    aria-label={`Nota: ${avaliacao.nota}`}
                >
                    {EstrelasAvaliacao(Number(avaliacao.nota))}
                </div>
            </CardContent>
        </Card>
    );
}
