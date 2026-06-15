'use client';

import { Input } from '@/components/ui/input';
import { useViagemPersonalizada } from '@/contexts/ContextoViagemPersonalizada';
import { Calendar } from 'lucide-react';
import { converterDias, formatarDias } from '@/lib/formatacao';

export default function InputDuracao() {
    const {
        state: { viagem },
        atualizarAtributo,
    } = useViagemPersonalizada();

    return (
        <div
            className={`bg-neutral-100 ${viagem.dias ? 'text-amber-600' : 'text-muted-foreground'} flex items-center px-4 rounded-md`}
        >
            <Calendar className="size-4 shrink-0" />

            <div className='flex items-center gap-1'>
                <Input
                    type="string"
                    inputMode="numeric"
                    pattern="[0-9]*"
                    placeholder="Duração"
                    className={`bg-transparent field-sizing-content px-0 pl-2 text-sm border-none rounded-none shadow-none focus-visible:ring-0 focus:outline-none`}
                    value={formatarDias(viagem.dias)}
                    onChange={(e) =>
                        atualizarAtributo('dias', converterDias(e.target.value))
                    }
                />
                {viagem.dias && (
                    <span className="text-sm">
                        {viagem.dias > 1 ? 'dias' : 'dia'}
                    </span>
                )}
            </div>
        </div>
    );
}
