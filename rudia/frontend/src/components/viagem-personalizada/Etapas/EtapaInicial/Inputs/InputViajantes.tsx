'use client';

import { Button } from '@/components/ui/button';
import { useViagemPersonalizada } from '@/contexts/ContextoViagemPersonalizada';
import { useClickOutside } from '@/hooks/useClickOutside';
import { useRef, useState } from 'react';
import { Minus, Plus, UsersRound } from 'lucide-react';

export default function InputViajantes() {
    const {
        state: { viagem },
        atualizarAtributo,
    } = useViagemPersonalizada();

    const [dropdownAberto, setDropdownAberto] = useState<boolean>(false);

    const viajantes = viagem.viajantes_adultos + viagem.viajantes_criancas;

    // Fechar o dropdown ao clicar fora dele
    const close = useRef<HTMLDivElement | null>(null);
    useClickOutside(close, () => setDropdownAberto(false));

    const rotulo = (nome: string, restricao: string) => {
        return (
            <div>
                <h2 className="text-sm font-bold">{nome}</h2>
                <span className="text-xs text-muted-foreground">
                    {restricao}
                </span>
            </div>
        );
    };

    const controle = (valor: number, setValor: (valor: number) => void) => {
        return (
            <div className="flex items-center space-x-3">
                {/* Diminuir o Valor */}
                <Button
                    variant="outline"
                    size="icon-sm"
                    className="rounded-full cursor-pointer"
                    onClick={() =>
                        valor - 1 <= 0 ? setValor(0) : setValor(valor - 1)
                    }
                    disabled={valor === 0}
                >
                    <Minus />
                </Button>

                {/* Valor */}
                <span>{valor}</span>

                {/* Aumentar o Valor */}
                <Button
                    variant="outline"
                    size="icon-sm"
                    className="rounded-full cursor-pointer"
                    onClick={() => setValor(valor + 1)}
                >
                    <Plus />
                </Button>
            </div>
        );
    };

    return (
        <div ref={close} className="relative">
            {/* TRIGGER - Ativa o dropdown */}
            <div
                className="bg-neutral-100 text-muted-foreground flex items-center px-4 rounded-md"
                onClick={() => setDropdownAberto(!dropdownAberto)}
            >
                <div
                    className={`flex items-center h-9 cursor-pointer ${
                        viajantes === 0
                            ? 'text-muted-foreground'
                            : 'text-amber-600'
                    }`}
                >
                    <UsersRound className="size-4" />
                    <span className="ml-2 text-sm">
                        {viajantes === 0
                            ? 'Quem'
                            : `${viajantes} ${
                                  viajantes === 1 ? 'rudiero' : 'rudieros'
                              }`}
                    </span>
                </div>
            </div>

            {/* DROPDOWN - Conteúdo do dropdown */}
            <div
                className={`
                absolute -right-2 z-10
                bg-white 
                w-64 mt-4 p-4 
                border shadow-md rounded-md 
                transition-all duration-300 ease-in-out 
                ${
                    dropdownAberto
                        ? 'opacity-100 scale-100 pointer-events-auto'
                        : 'opacity-0 scale-95 pointer-events-none'
                } 
            `}
            >
                <div className="flex flex-col items-center gap-4">
                    <div className="flex justify-between items-center w-full">
                        {rotulo('Adultos', '16 anos ou mais')}
                        {controle(viagem.viajantes_adultos, (valor) =>
                            atualizarAtributo('viajantes_adultos', valor),
                        )}
                    </div>

                    {/* Borda de separação */}
                    <div className="w-full border"></div>

                    <div className="flex justify-between items-center w-full">
                        {rotulo('Crianças', '0 a 15 anos')}
                        {controle(viagem.viajantes_criancas, (valor) =>
                            atualizarAtributo('viajantes_criancas', valor),
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
