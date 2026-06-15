'use client';

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import Image from 'next/image';

interface CardInformativoProps {
    titulo: string;
    descricao: string;
    imagemUrl: string;
}

export default function CardInformativo({
    titulo,
    descricao,
    imagemUrl,
}: CardInformativoProps) {
    return (
        <Card
            className="
                w-[220px] h-[300px] p-0 gap-0 rounded-sm overflow-hidden cursor-default
                focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-primary
            "
        >
            {/* Imagem representativa do card */}
            <figure className="relative w-[220px] h-[180px]">
                <Image
                    src={imagemUrl}
                    alt={titulo}
                    fill
                    className="object-cover"
                />
            </figure>
            <CardHeader className="mt-4 px-4 h-8">
                <CardTitle className="text-foreground text-xl font-bold">
                    {titulo}
                </CardTitle>
            </CardHeader>
            <CardContent className="px-4 py-0">
                <p className="text-xs text-muted-foreground">{descricao}</p>
            </CardContent>
        </Card>
    );
}
