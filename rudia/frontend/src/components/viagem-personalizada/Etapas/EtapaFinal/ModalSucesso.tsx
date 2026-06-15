'use client';

import React from 'react';
import { Button } from '@/components/ui/button';
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogFooter,
    DialogTitle,
} from '@/components/ui/dialog';
import { Check, House, PlusCircle } from 'lucide-react';
import { useRouter } from 'next/navigation';

interface ModalSucessoProps {
    open: boolean;
    onOpenChange: (open: boolean) => void;
}

export default function ModalSucesso({
    open,
    onOpenChange,
}: ModalSucessoProps) {
    const router = useRouter();

    return (
        <Dialog open={open} onOpenChange={onOpenChange}>
            <DialogContent className="gap-0">
                <DialogTitle className="text-green-700 mb-3">
                    Viagem salva com sucesso!
                </DialogTitle>

                <DialogDescription className="mb-7">
                    Sua viagem foi criada com sucesso. O que você deseja fazer
                    agora?
                </DialogDescription>

                <DialogFooter className="flex gap-2">
                    <Button
                        variant="default"
                        className="bg-blue-700 text-white border-none hover:bg-blue-600 cursor-pointer"
                        onClick={() => {
                            onOpenChange(false);
                            router.push('/');
                        }}
                    >
                        <House /> Home
                    </Button>

                    <Button
                        variant="default"
                        className="bg-amber-600 text-white border-none hover:bg-amber-500 cursor-pointer"
                        onClick={() => onOpenChange(false)}
                    >
                        <PlusCircle /> Nova Viagem
                    </Button>

                    <Button
                        variant="default"
                        className="bg-green-700 text-white border-none hover:bg-green-600 cursor-pointer"
                        onClick={() => {
                            onOpenChange(false);
                            router.push('/'); // TROCA FUTURAMENTE PARA A URL CORRETA
                        }}
                    >
                        <Check /> Ver Viagem
                    </Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    );
}
