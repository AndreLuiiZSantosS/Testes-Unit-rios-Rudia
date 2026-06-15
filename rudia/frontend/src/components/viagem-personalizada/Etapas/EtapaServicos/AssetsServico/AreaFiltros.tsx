'use client';

import BarraPesquisa from '@/components/common/BarraPesquisa/BarraPesquisa';
import { Button } from '@/components/ui/button';
import { ArrowUpDown, Filter } from 'lucide-react';
import { useState } from 'react';

interface AreaFiltrosProps {
    placeholder: string;
}

export default function AreaFiltros({ placeholder }: AreaFiltrosProps) {
    const [search, setSearch] = useState<string>('');
    // Centralizar a logica de filtragem nesse componente

    return (
        <div className="flex justify-center items-center gap-3">
            <BarraPesquisa placeholder={placeholder} value={search} onChange={setSearch} />
            <div>
                <Button
                    variant="ghost"
                    size="icon-lg"
                    className="cursor-pointer"
                    aria-label="Filtrar serviços"
                >
                    <Filter className="text-indigo-950 size-5" />
                </Button>
                <Button
                    variant="ghost"
                    size="icon-lg"
                    className="cursor-pointer"
                    aria-label="Ordenar serviços"
                >
                    <ArrowUpDown className="text-indigo-950 size-5" />
                </Button>
            </div>
        </div>
    );
}