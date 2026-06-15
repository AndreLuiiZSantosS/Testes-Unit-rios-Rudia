'use client';

import CabecalhoModalServico from './CabecalhoModalServico';
import SecaoAvaliacoes from './SecaoAvaliacoes';
import { Dialog, DialogContent, DialogTitle } from '@/components/ui/dialog';
import { useServicoPorId } from '@/hooks/useServicosPorId';
import { useSelecaoServicosViagem } from '@/hooks/useSelecaoServicosViagem';
import { useAvaliacoesServico } from '@/hooks/useAvaliacoesServico';

interface ModalCardServicoProps {
    servicoId: number | null;
    onClose: () => void;
}

export default function ModalCardServico({
    servicoId,
    onClose,
}: ModalCardServicoProps) {
    const { servico } = useServicoPorId(servicoId);

    const { estaSelecionado, selecionarServico } = useSelecaoServicosViagem(
        servico?.categoria.nome ?? '',
    );

    if (!servicoId) return null;

    return (
        <Dialog open={!!servicoId} onOpenChange={onClose}>
            <DialogContent className="modal">
                {!servico ? (
                    <div className="flex items-center justify-center w-full h-full">
                        <DialogTitle className="hidden">
                            Serviço não encontrado
                        </DialogTitle>
                        <p className="text-muted-foreground text-lg">
                            Nenhuma informação disponível
                        </p>
                    </div>
                ) : (
                    <>
                        <CabecalhoModalServico
                            servico={servico}
                            selecionado={estaSelecionado(servico.id)}
                            onSelecionar={() => selecionarServico(servico.id)}
                        />

                        <div className="space-y-4">
                            <section className="space-y-1.5">
                                <h2 className="text-lg font-bold">Descrição</h2>
                                <p className="text-sm">{servico.descricao}</p>
                            </section>

                            <SecaoAvaliacoes
                                total={servico.avaliacoes_resumo.total}
                                avaliacoes={servico.ultimas_avaliacoes}
                            />
                        </div>
                    </>
                )}
            </DialogContent>
        </Dialog>
    );
}
