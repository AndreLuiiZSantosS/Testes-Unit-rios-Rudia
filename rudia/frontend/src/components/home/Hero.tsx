import React from 'react';
import Image from 'next/image';

export default function Hero() {
    return (
        <main className="mb-20 relative flex min-h-[534px] items-center justify-center">
            <div className="absolute inset-0 -z-10">
                <Image
                    src="/imagens/paisagem1.jpg"
                    alt="Paisagem litorânea do Rio Grande do Norte"
                    fill
                    priority
                    className="object-cover"
                />
                <div className="absolute inset-0" />
            </div>

            <section className="flex flex-col items-center gap-3 pt-52 pb-36 text-center text-white">
                <h1 className="text-3xl md:text-5xl font-bold">
                    Preparado para a sua próxima viagem?
                </h1>
                <h2 className="text-lg md:text-2xl">
                    Crie uma viagem perfeita e inesquecível!
                </h2>

                <div className="mt-6">
                    <button className="rounded-full bg-amber-600 px-6 py-3 text-base font-medium text-primary-foreground shadow-lg transition cursor-pointer">
                        Crie uma viagem rápida
                    </button>
                </div>
            </section>
        </main>
    );
}
