'use client';

import { useState } from 'react';
import { registroRudiero } from '@/api/registro/registro-rudiero.fetch';
import { registroPropostaParceria } from '@/api/registro/proposta-parceria.fetch';
import { useRouter } from 'next/navigation';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import SelecaoForm from './SelecaoForm';
import {
    RegistroRudieroFormDTO,
    RegistroRudieroFormSchema,
} from '@/schemas/registro-rudiero.schema';
import {
    PropostaParceriaFormDTO,
    PropostaParceriaFormSchema,
} from '@/schemas/proposta-parceria.schema';
import CadastroRudiero from './CadastroRudiero';
import CadastroParceiro from './CadastroParceiro';

export default function Cadastros() {
    const [tela, setTela] = useState<'SELECAO' | 'RUDIERO' | 'PARCEIRO'>(
        'SELECAO',
    );
    const router = useRouter();

    const rudieroForm = useForm<RegistroRudieroFormDTO>({
        resolver: zodResolver(RegistroRudieroFormSchema),
        defaultValues: {
            nome: '',
            email: '',
            data_nascimento: '',
            password: '',
            password_confirm: '',
        },
    }); 

    const parceiroForm = useForm<PropostaParceriaFormDTO>({
        resolver: zodResolver(PropostaParceriaFormSchema),
        defaultValues: {
            nome: '',
            email: '',
            cnpj: '',
            password: '',
            password_confirm: '',
        },
    });

    const gerarUsername = (email: string) => {
        const baseUsername = email.split('@')[0];
        const randomSuffix = Math.random().toString(36).substring(2, 8);
        return `${baseUsername}${randomSuffix}`;
    };

    const handleRudieroSubmit = async (data: RegistroRudieroFormDTO) => {
        try {
            // Ajustar dados para a API
            await registroRudiero({
                ...data,
                username: gerarUsername(data.email),
            });
            router.push('/login');
        } catch (error) {
            console.error(error);
        }
    };

    const handleParceiroSubmit = async (data: PropostaParceriaFormDTO) => {
        try {
            // Ajustar dados para a API
            await registroPropostaParceria({
                ...data,
                username: gerarUsername(data.email),
                cnpj: data.cnpj.replace(/\D/g, ''), // Remover formatação do CNPJ
            });
            router.push('/login');
        } catch (error) {
            console.error(error);
        }
    };

    const voltar = () => {
        rudieroForm.reset();
        parceiroForm.reset();
        setTela('SELECAO');
    };

    if (tela === 'RUDIERO')
        return CadastroRudiero({
            form: rudieroForm,
            handleSubmit: handleRudieroSubmit,
            voltar,
        });

    if (tela === 'PARCEIRO') {
        return CadastroParceiro({
            form: parceiroForm,
            handleSubmit: handleParceiroSubmit,
            voltar,
        });
    }

    return SelecaoForm({ setTela });
}
