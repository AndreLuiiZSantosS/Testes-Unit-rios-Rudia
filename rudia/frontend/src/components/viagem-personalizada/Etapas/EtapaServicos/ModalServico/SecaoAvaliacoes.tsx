'use client';

import CardAvaliacao from './CardAvaliacao';
import { AvaliacaoDTO } from '@/schemas/geral.schema';

interface SecaoAvaliacoesProps {
    total: number;
    avaliacoes: AvaliacaoDTO[];
}

export default function SecaoAvaliacoes({
    total,
    avaliacoes,
}: SecaoAvaliacoesProps) {
    return (
        <section className="space-y-2.5">
            <h2 className="text-lg font-bold">Avaliações ({total})</h2>

            <div className="flex gap-3">
                {avaliacoes.length > 0 ? (
                    avaliacoes
                        .slice(0, 3)
                        .map((avaliacao) => (
                            <CardAvaliacao
                                key={avaliacao.id}
                                avaliacao={avaliacao}
                            />
                        ))
                ) : (
                    <p className="text-sm text-muted-foreground">
                        Este serviço ainda não possui avaliações.
                    </p>
                )}
            </div>
        </section>
    );
}
