'use client';

import { Button } from '@/components/ui/button';
import ResumoViagem from './Informacoes/ResumoViagem';
import NavegacaoEtapas from './Navegacao/NavegacaoEtapas';
import { Trash2 } from 'lucide-react';
import { useViagemPersonalizada } from '@/contexts/ContextoViagemPersonalizada';

export default function IndicadorEtapas() {
    const { resetViagemPersonalizada } = useViagemPersonalizada();
    return (
        <div className="flex flex-col gap-5">
            {/* Resumo e Descarte da Viagem */}
            <div className="flex justify-between items-center">
                <ResumoViagem />
                <Button className='ml-2 cursor-pointer' variant="destructive" onClick={resetViagemPersonalizada}>
                    <Trash2 />
                    <span className='sm:hidden md:block'>Descartar Viagem</span>
                </Button>
            </div>

            {/* Barra de Progresso */}
            <NavegacaoEtapas />
        </div>
    );
}
