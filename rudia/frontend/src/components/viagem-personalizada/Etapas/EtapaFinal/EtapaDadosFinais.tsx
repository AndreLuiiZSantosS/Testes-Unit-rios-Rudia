'use client';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import ModalSucesso from './ModalSucesso';
import { useViagemPersonalizada } from '@/contexts/ContextoViagemPersonalizada';
import { VisibilidadeTypeDTO } from '@/schemas/geral.schema';
import { useState } from 'react';
import { Check, Lock, Unlock, X } from 'lucide-react';

export default function EtapaDadosFinais() {
    const {
        state: { viagem },
        atualizarAtributo,
        atualizarEtapa,
        resetViagemPersonalizada,
    } = useViagemPersonalizada();

    const { nome, descricao, visibilidade } = viagem;

    const VisibilidadeType: Record<VisibilidadeTypeDTO, VisibilidadeTypeDTO> = {
        PUBLICO: 'PUBLICO',
        PRIVADO: 'PRIVADO',
    };

    const [abrirModalSucesso, setAbrirModalSucesso] = useState(false);

    const handlerModalSucesso = (isOpen: boolean) => {
        if (!isOpen) {
            setAbrirModalSucesso(false);
            resetViagemPersonalizada();
        }

        setAbrirModalSucesso(isOpen);
    };

    const salvar = async () => {
        try {
            // Centralizar o fecth para a API
            alert(JSON.stringify(viagem));

            setAbrirModalSucesso(true);
        } catch (err) {
            // Centralizar a lógica de tratamento de erros
        }
    };

    const descartar = () => {
        atualizarEtapa(1);
        resetViagemPersonalizada();
    };

    return (
        <div className="mt-10 space-y-6">
            <h1 className="text-xl text-center">Salve a sua viagem!</h1>

            <div className="max-w-lg m-auto">
                <div className="flex flex-col gap-4">
                    <Input
                        placeholder="Nome da Viagem"
                        value={nome}
                        className="
                            px-4 py-5
                            border border-muted-foreground
                            focus-visible:outline-none focus-visible:ring-0 focus-visible:border-muted-foreground
                        "
                        onChange={(e) =>
                            atualizarAtributo('nome', e.target.value)
                        }
                        // disabled={carregando}
                    />

                    <Textarea
                        placeholder="Descrição da Viagem"
                        value={descricao}
                        className="
                            min-h-64
                            px-4 py-3
                            border border-muted-foreground
                            focus-visible:outline-none focus-visible:ring-0 focus-visible:border-muted-foreground
                        "
                        onChange={(e) =>
                            atualizarAtributo('descricao', e.target.value)
                        }
                        // disabled={carregando}
                    />
                </div>

                <div className="flex justify-between items-center mt-8">
                    <div className="flex items-center gap-4">
                        <span className="text-muted-foreground">
                            Visibilidade
                        </span>

                        <button
                            type="button"
                            className="border border-amber-600 w-16 h-9 rounded-full cursor-pointer"
                            onClick={() =>
                                atualizarAtributo(
                                    'visibilidade',
                                    VisibilidadeType[
                                        visibilidade ===
                                        VisibilidadeType.PRIVADO
                                            ? VisibilidadeType.PUBLICO
                                            : VisibilidadeType.PRIVADO
                                    ],
                                )
                            }
                            // disabled={carregando}
                        >
                            <div
                                className={`bg-amber-600 flex justify-center items-center w-7 h-7 rounded-full transition-transform
                                    ${visibilidade === VisibilidadeType.PRIVADO ? 'translate-x-1' : 'translate-x-7.5'}`}
                            >
                                {visibilidade === VisibilidadeType.PRIVADO ? (
                                    <Lock className="text-white font-bold size-4" />
                                ) : (
                                    <Unlock className="text-white font-bold size-4" />
                                )}
                            </div>
                        </button>
                    </div>

                    <div className="flex gap-2">
                        <Button
                            variant="outline"
                            className="text-green-800 border-green-800 hover:text-green-800 hover:border-green-800 cursor-pointer"
                            onClick={salvar}
                            // disabled={carregando}
                        >
                            <Check />
                            {/* {carregando ? 'Salvando...' : 'Salvar'} */}
                        </Button>

                        <Button
                            variant="outline"
                            className="text-accent-foreground border-accent-foreground hover:text-accent-foreground hover:border-accent-foreground cursor-pointer"
                            onClick={descartar}
                            // disabled={carregando}
                        >
                            <X /> Descartar
                        </Button>
                    </div>
                </div>
            </div>

            <ModalSucesso
                open={abrirModalSucesso}
                onOpenChange={handlerModalSucesso}
            />
        </div>
    );
}
