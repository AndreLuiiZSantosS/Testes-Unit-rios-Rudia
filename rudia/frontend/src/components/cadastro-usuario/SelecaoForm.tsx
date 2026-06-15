'use client';

import Logo from '@/components/common/Logo/Logo';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { House, User } from 'lucide-react';

interface SelecaoFormProps {
    setTela: (tela: 'SELECAO' | 'PARCEIRO' | 'RUDIERO') => void;
}

export default function SelecaoForm({ setTela }: SelecaoFormProps) {
    return (
        <div className="bg-[#F6F4EE] min-h-screen flex flex-col font-sans text-gray-800">
            <div className="flex grow flex-col items-center justify-center p-6 md:p-12 fade-in">
                <div className="mb-10 flex justify-center text-5xl font-bold tracking-tighter">
                    <Logo width={240} height={80} />
                </div>

                <h1 className="text-3xl md:text-4xl font-bold mb-12 text-center text-[#1E4231]">
                    Qual tipo de perfil você gostaria de criar sua conta?
                </h1>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-4xl mb-12">
                    <Card
                        className="bg-white p-10 rounded-2xl border-2 border-transparent hover:border-amber-600 hover:shadow-xl transition-all duration-300 flex flex-col items-center text-center group cursor-pointer"
                        onClick={() => setTela('PARCEIRO')}
                    >
                        <div className="mb-6 p-5 bg-[#F6F4EE] rounded-full group-hover:bg-[#FFF0E5] transition-colors duration-300">
                            <House className="h-16 w-16 text-[#1E4231] group-hover:text-amber-600 transition-colors duration-300" />
                        </div>
                        <h2 className="text-2xl font-bold mb-3 text-[#1E4231]">
                            Parceiro
                        </h2>
                        <p className="text-sm text-gray-600 leading-relaxed mb-8">
                            Ofereça seus serviços e produtos na nossa plataforma
                            e alcance mais clientes.
                        </p>
                        <Button className="w-full bg-white border-2 border-amber-600 text-amber-600 font-semibold py-3 rounded-full hover:bg-amber-600 group-hover:bg-amber-600 group-hover:text-white transition-all duration-300 cursor-pointer">
                            Criar conta Parceiro
                        </Button>
                    </Card>

                    <Card
                        className="bg-white p-10 rounded-2xl border-2 border-transparent hover:border-amber-600 hover:shadow-xl transition-all duration-300 flex flex-col items-center text-center group cursor-pointer"
                        onClick={() => setTela('RUDIERO')}
                    >
                        <div className="mb-6 p-5 bg-[#F6F4EE] rounded-full group-hover:bg-[#FFF0E5] transition-colors duration-300">
                            <User className="h-16 w-16 text-[#1E4231] group-hover:text-amber-600 transition-colors duration-300" />
                        </div>
                        <h2 className="text-2xl font-bold mb-3 text-[#1E4231]">
                            Rudiero
                        </h2>
                        <p className="text-sm text-gray-600 leading-relaxed mb-8">
                            Crie roteiros, receba ofertas exclusivas e
                            compartilhe suas experiências com a comunidade.
                        </p>
                        <Button className="w-full bg-white border-2 border-amber-600 text-amber-600 font-semibold py-3 rounded-full hover:bg-amber-600 group-hover:bg-amber-600 group-hover:text-white transition-all duration-300 cursor-pointer">
                            Criar conta Rudiero
                        </Button>
                    </Card>
                </div>

                <div className="mt-auto text-xs text-gray-500 text-center">
                    Ao criar uma conta, você concorda com a nossa{' '}
                    <a
                        href="#"
                        className="font-medium hover:text-amber-600 transition-colors"
                    >
                        Política de privacidade
                    </a>{' '}
                    e os nossos{' '}
                    <a
                        href="#"
                        className="font-medium hover:text-amber-600 transition-colors"
                    >
                        Termos de uso
                    </a>
                    .
                </div>
            </div>
        </div>
    );
}
