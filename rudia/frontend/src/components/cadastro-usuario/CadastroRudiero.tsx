'use client';

import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Label } from '@/components/ui/label';
import { Input } from '@/components/ui/input';
import { UseFormReturn } from 'react-hook-form';
import { RegistroRudieroFormDTO } from '@/schemas/registro-rudiero.schema';

interface CadastroRudieroProps {
    voltar: () => void;
    handleSubmit: (data: RegistroRudieroFormDTO) => void;
    form: UseFormReturn<RegistroRudieroFormDTO>;
}

export default function CadastroRudiero({
    voltar,
    handleSubmit,
    form,
}: CadastroRudieroProps) {
    const maxBirthDateCalculate = () => {
        const today = new Date();
        const maxBirthDate = new Date(
            today.getFullYear() - 16,
            today.getMonth(),
            today.getDate(),
        );
        const maxBirthDateValue = [
            String(maxBirthDate.getFullYear()).padStart(4, '0'),
            String(maxBirthDate.getMonth() + 1).padStart(2, '0'),
            String(maxBirthDate.getDate()).padStart(2, '0'),
        ].join('-');

        return maxBirthDateValue;
    };

    return (
        <div className="flex grow items-center justify-center p-6 md:p-12 fade-in">
            <Card className="w-full max-w-md bg-white p-8 md:p-10 rounded-2xl shadow-xl border border-gray-100">
                <Button
                    variant="ghost"
                    onClick={voltar}
                    className="flex items-center text-sm text-gray-500 hover:text-[#E56C00] transition-colors mb-8"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="16"
                        height="16"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="mr-1"
                    >
                        <path d="m15 18-6-6 6-6" />
                    </svg>
                    Voltar
                </Button>

                <div>
                    <h2 className="text-3xl font-bold mb-2 text-[#1E4231]">
                        Cadastro Rudiero
                    </h2>
                    <p className="text-sm text-muted-foreground mb-8">
                        Preencha seus dados para começar a explorar.
                    </p>
                </div>

                <form
                    onSubmit={form.handleSubmit(handleSubmit)}
                    className="space-y-4"
                >
                    <div>
                        <Label className="block text-sm font-semibold mb-1.5 text-gray-700">
                            Nome completo
                        </Label>
                        <Input
                            {...form.register('nome')}
                            placeholder="Como devemos te chamar?"
                        />
                        {form.formState.errors.nome && (
                            <p className="text-red-500 text-xs mt-2 ml-1">
                                {form.formState.errors.nome.message}
                            </p>
                        )}
                    </div>
                    <div>
                        <Label className="block text-sm font-semibold mb-1.5 text-gray-700">
                            E-mail
                        </Label>
                        <Input
                            type="email"
                            {...form.register('email')}
                            placeholder="seu@email.com"
                        />
                        {form.formState.errors.email && (
                            <p className="text-red-500 text-xs mt-2 ml-1">
                                {form.formState.errors.email.message}
                            </p>
                        )}
                    </div>
                    <div>
                        <Label className="block text-sm font-semibold mb-1.5 text-gray-700">
                            Data de nascimento
                        </Label>
                        <Input
                            id="data-nascimento"
                            type="date"
                            {...form.register('data_nascimento')}
                            max={maxBirthDateCalculate()}
                        />
                        <p className="text-xs text-[#E56C00] font-medium mt-1 ml-1">
                            É necessário ter pelo menos 16 anos.
                        </p>
                        {form.formState.errors.data_nascimento && (
                            <p className="text-red-500 text-xs mt-2 ml-1">
                                {form.formState.errors.data_nascimento.message}
                            </p>
                        )}
                    </div>
                    <div>
                        <Label className="block text-sm font-semibold mb-1.5 text-gray-700">
                            Senha
                        </Label>
                        <Input
                            type="password"
                            {...form.register('password')}
                            placeholder="Crie uma senha forte"
                        />
                        {form.formState.errors.password && (
                            <p className="text-red-500 text-xs mt-2 ml-1">
                                {form.formState.errors.password.message}
                            </p>
                        )}
                    </div>
                    <div>
                        <Label className="block text-sm font-semibold mb-1.5 text-gray-700">
                            Senha
                        </Label>
                        <Input
                            type="password"
                            {...form.register('password_confirm')}
                            placeholder="Confirme sua senha"
                        />
                        {form.formState.errors.password_confirm && (
                            <p className="text-red-500 text-xs mt-2 ml-1">
                                {form.formState.errors.password_confirm.message}
                            </p>
                        )}
                    </div>
                    <Button
                        type="submit"
                        className="w-full bg-[#E56C00] hover:bg-[#CC6000] text-white font-semibold py-4 rounded-full transition-colors mt-6 shadow-md hover:shadow-lg cursor-pointer"
                    >
                        Concluir Cadastro
                    </Button>
                </form>
            </Card>
        </div>
    );
}
