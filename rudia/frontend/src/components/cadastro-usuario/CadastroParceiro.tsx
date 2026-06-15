'use client';

import { PropostaParceriaFormDTO } from '@/schemas/proposta-parceria.schema';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { UseFormReturn } from 'react-hook-form';
import { Label } from '@/components/ui/label';
import { Input } from '@/components/ui/input';
import { formatarCNPJ } from '@/lib/formatacao';

interface CadastroParceiroProps {
    voltar: () => void;
    handleSubmit: (data: PropostaParceriaFormDTO) => void;
    form: UseFormReturn<PropostaParceriaFormDTO>;
}

export default function CadastroParceiro({
    voltar,
    handleSubmit,
    form,
}: CadastroParceiroProps) {
    const handleCNPJChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const formatted = formatarCNPJ(e.target.value);
        form.setValue('cnpj', formatted, {
            shouldDirty: true,
            shouldValidate: true,
        });
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
                        Cadastro Parceiro
                    </h2>
                    <p className="text-sm text-muted-foreground mb-8">
                        Cadastre sua empresa e conecte-se com viajantes.
                    </p>
                </div>

                <form
                    onSubmit={form.handleSubmit(handleSubmit)}
                    className="space-y-4"
                >
                    <div>
                        <Label className="block text-sm font-semibold mb-1.5 text-gray-700">
                            Nome da Empresa / Responsável
                        </Label>
                        <Input
                            {...form.register('nome')}
                            placeholder="Nome do seu negócio"
                        />
                        {form.formState.errors.nome && (
                            <p className="text-red-500 text-xs mt-2 ml-1">
                                {form.formState.errors.nome.message}
                            </p>
                        )}
                    </div>
                    <div>
                        <Label className="block text-sm font-semibold mb-1.5 text-gray-700">
                            E-mail corporativo
                        </Label>
                        <Input
                            type="email"
                            {...form.register('email')}
                            placeholder="contato@suaempresa.com"
                        />
                        {form.formState.errors.email && (
                            <p className="text-red-500 text-xs mt-2 ml-1">
                                {form.formState.errors.email.message}
                            </p>
                        )}
                    </div>
                    <div>
                        <Label className="block text-sm font-semibold mb-1.5 text-gray-700">
                            CNPJ
                        </Label>
                        <Input
                            id="cnpj-input"
                            {...form.register('cnpj')}
                            onChange={handleCNPJChange}
                            value={form.watch('cnpj') ?? ''}
                            placeholder="00.000.000/0000-00"
                            maxLength={18}
                        />
                        {form.formState.errors.cnpj && (
                            <p className="text-red-500 text-xs mt-2 ml-1">
                                {form.formState.errors.cnpj.message}
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
                            Confirme a Senha
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
                        className="w-full bg-[#E56C00] hover:bg-[#CC6000] text-white font-semibold py-4 rounded-full transition-colors mt-6 shadow-md hover:shadow-lg"
                    >
                        Concluir Cadastro
                    </Button>
                </form>
            </Card>
        </div>
    );
}
