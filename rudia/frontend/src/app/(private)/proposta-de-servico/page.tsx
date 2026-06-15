'use client';

import React, { useEffect, useState } from 'react';
import { Button } from '@/components/ui/button';

import CategoriaNegocioForm from '@/components/proposta-servico/CategoriaNegocioForm';
import CidadeAtuacaoForm from '@/components/proposta-servico/CidadeAtuacaoForm';
import EnderecoEmpresaForm from '@/components/proposta-servico/EnderecoEmpresaForm';
import UploadFotosNegocio from '@/components/proposta-servico/UploadFotosNegocio';
import FaixaPrecoForm from '@/components/proposta-servico/FaixaPrecoForm';
import HorariosDiasSemanaForm from '@/components/proposta-servico/HorariosDiasSemanaForm';
import DescricaoForm from '@/components/proposta-servico/DescricaoForm';
import TagsForm from '@/components/proposta-servico/TagsForm';
import { registroPropostaServico } from '@/api/registro/proposta-servico.fetch';
import { obterTagsCategoria } from '@/api/servico/categoria.fetch';
import { useCategoriasServico } from '@/hooks/useCategoriasServico';
import { useCidades } from '@/hooks/useCidades';
import { TagDTO } from '@/schemas/categoria-tag.schema';
import {
    DiaSemanaDTO,
    PropostaServicoRequestDTO,
    PropostaServicoRequestSchema,
} from '@/schemas/proposta-servico.schema';
import Header from '@/components/layout/Header';

type EnderecoFormState = PropostaServicoRequestDTO['endereco'];

type FormularioPropostaServicoState = Omit<
    PropostaServicoRequestDTO,
    'horarios_funcionamento' | 'endereco'
> & {
    endereco: EnderecoFormState;
    horarios: {
        inicio: string;
        fim: string;
        dias: DiaSemanaDTO[];
    };
};

const initialState: FormularioPropostaServicoState = {
    nome: '',
    categoria: 0,
    cidade: 0,
    endereco: {
        cep: '',
        logradouro: '',
        numero: '',
        complemento: '',
    },
    imagem_capa: '',
    preco_minimo: 0,
    preco_maximo: 0,
    horarios: { inicio: '', fim: '', dias: [] },
    descricao: '',
    tags: [],
    capacidade_maxima: null,
};

export default function FormularioDeServico() {
    const [step, setStep] = useState(1);
    const [formData, setFormData] =
        useState<FormularioPropostaServicoState>(initialState);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [success, setSuccess] = useState(false);
    const [tagsDisponiveis, setTagsDisponiveis] = useState<TagDTO[]>([]);
    const [carregandoTags, setCarregandoTags] = useState(false);
    const { categorias, carregando: carregandoCategorias } =
        useCategoriasServico();
    const { cidades, carregando: carregandoCidades } = useCidades();

    // Funções para atualizar campos específicos
    const setCategoria = (categoria: number) =>
        setFormData((prev) => ({ ...prev, categoria, tags: [] }));
    const setCidade = (cidade: number) =>
        setFormData((prev) => ({ ...prev, cidade }));
    const setEndereco = (endereco: EnderecoFormState) =>
        setFormData((prev) => ({ ...prev, endereco }));
    const setImagemCapa = (imagem_capa: string) =>
        setFormData((prev) => ({ ...prev, imagem_capa }));
    const setFaixaPreco = (faixaPreco: { min: string; max: string }) =>
        setFormData((prev) => ({
            ...prev,
            preco_minimo: Number(faixaPreco.min || 0),
            preco_maximo: Number(faixaPreco.max || 0),
        }));
    const setHorarios = (
        horarios: FormularioPropostaServicoState['horarios'],
    ) => setFormData((prev) => ({ ...prev, horarios }));
    const setDescricao = (descricao: string) =>
        setFormData((prev) => ({ ...prev, descricao }));
    const setTags = (tags: number[]) =>
        setFormData((prev) => ({ ...prev, tags }));
    const setNome = (nome: string) =>
        setFormData((prev) => ({ ...prev, nome }));
    const setCapacidadeMaxima = (capacidade: string) => {
        const valorNumerico = Number(capacidade);
        setFormData((prev) => ({
            ...prev,
            capacidade_maxima:
                Number.isFinite(valorNumerico) && valorNumerico > 0
                    ? valorNumerico
                    : null,
        }));
    };

    useEffect(() => {
        const carregarTags = async () => {
            if (formData.categoria <= 0) {
                setTagsDisponiveis([]);
                return;
            }

            try {
                setCarregandoTags(true);
                const resposta = await obterTagsCategoria(formData.categoria);
                setTagsDisponiveis(resposta.results);
            } catch {
                setTagsDisponiveis([]);
            } finally {
                setCarregandoTags(false);
            }
        };

        carregarTags();
    }, [formData.categoria]);

    // Dias da semana
    const toggleDay = (day: DiaSemanaDTO) => {
        setFormData((prev) => {
            const dias = prev.horarios.dias.includes(day)
                ? prev.horarios.dias.filter((d) => d !== day)
                : [...prev.horarios.dias, day];
            return { ...prev, horarios: { ...prev.horarios, dias } };
        });
    };

    // Envio do formulário
    const handleSubmit = async () => {
        setLoading(true);
        setError(null);
        setSuccess(false);

        try {
            const payload: PropostaServicoRequestDTO =
                PropostaServicoRequestSchema.parse({
                    ...formData,
                    endereco: {
                        cep: formData.endereco.cep,
                        logradouro: formData.endereco.logradouro,
                        numero: formData.endereco.numero,
                        complemento: formData.endereco.complemento,
                    },
                    horarios_funcionamento: formData.horarios.dias.map(
                        (dia) => ({
                            dia_semana: dia,
                            hora_abertura: formData.horarios.inicio,
                            hora_fechamento: formData.horarios.fim,
                        }),
                    ),
                });

            await registroPropostaServico(payload);
            setSuccess(true);
            setFormData(initialState);
            setStep(1);
        } catch (e: unknown) {
            if (e instanceof Error) {
                setError(e.message);
            } else {
                setError(
                    'Erro ao enviar proposta. Verifique os dados e tente novamente.',
                );
            }
        } finally {
            setLoading(false);
        }
    };

    const podeIrParaEtapa2 =
        formData.nome.trim().length > 0 &&
        formData.categoria > 0 &&
        formData.cidade > 0 &&
        formData.imagem_capa.length > 0 &&
        formData.endereco.cep.replace(/\D/g, '').length === 8 &&
        formData.endereco.logradouro.trim().length > 0 &&
        formData.endereco.numero.trim().length > 0;

    const faixaPrecoValue = {
        min: formData.preco_minimo > 0 ? String(formData.preco_minimo) : '',
        max: formData.preco_maximo > 0 ? String(formData.preco_maximo) : '',
    };

    const podeEnviarEtapa2 =
        formData.preco_minimo > 0 &&
        formData.preco_maximo > 0 &&
        formData.preco_maximo >= formData.preco_minimo &&
        formData.horarios.inicio.length > 0 &&
        formData.horarios.fim.length > 0 &&
        formData.horarios.dias.length > 0 &&
        formData.descricao.trim().length > 0;

    return (
        <>
            <Header />
            <div className="min-h-screen bg-[#f5f5f2] flex flex-col items-center py-25 px-4 font-sans">
                <div className="text-center mb-8">
                    <h1 className="text-2xl font-bold text-gray-900">
                        A Rudiá abre as portas para a sua empresa!
                    </h1>
                    <p className="text-sm text-gray-500 max-w-md mt-2">
                        Fale-nos um pouco sobre a sua empresa para que possamos
                        posicioná-la da melhor forma em nossa plataforma
                    </p>
                </div>

                <div className="bg-white rounded-2xl shadow-sm w-full max-w-2xl p-8 md:p-12">
                    <div className="relative flex items-center justify-between mb-8 w-full">
                        <div className="absolute h-0.5 w-full bg-gray-200 top-1/2 -translate-y-1/2 z-0" />
                        <div
                            className="absolute h-0.5 bg-orange-500 top-1/2 -translate-y-1/2 z-0 transition-all duration-300"
                            style={{ width: step === 1 ? '0%' : '100%' }}
                        />
                        <div
                            className={`w-4 h-4 rounded-full z-10 transition-colors duration-300 ${step >= 1 ? 'bg-orange-500' : 'bg-gray-300'}`}
                        />
                        <div
                            className={`w-4 h-4 rounded-full z-10 transition-colors duration-300 ${step === 2 ? 'bg-orange-500' : 'bg-gray-300'}`}
                        />
                    </div>

                    {step === 1 ? (
                        <div className="space-y-6">
                            <div className="space-y-2">
                                <label
                                    htmlFor="nome-estabelecimento"
                                    className="text-lg font-semibold block text-center"
                                >
                                    Nome do estabelecimento (Razao Social)
                                </label>
                                <input
                                    id="nome-estabelecimento"
                                    className="w-full border rounded-md px-3 py-2"
                                    placeholder="Digite o nome do servico"
                                    value={formData.nome}
                                    onChange={(event) =>
                                        setNome(event.target.value)
                                    }
                                />
                            </div>

                            <CategoriaNegocioForm
                                value={formData.categoria}
                                onChange={setCategoria}
                                categorias={categorias}
                                carregando={carregandoCategorias}
                            />

                            <CidadeAtuacaoForm
                                value={formData.cidade}
                                onChange={setCidade}
                                cidades={cidades ? cidades?.results : []}
                                carregando={carregandoCidades}
                            />

                            <EnderecoEmpresaForm
                                value={formData.endereco}
                                onChange={setEndereco}
                            />
                            <UploadFotosNegocio
                                value={formData.imagem_capa}
                                onChange={setImagemCapa}
                            />

                            <Button
                                onClick={() => setStep(2)}
                                disabled={!podeIrParaEtapa2}
                                className="w-full bg-green-600 hover:bg-green-700 text-white font-bold h-11 rounded-xl transition-all"
                            >
                                Continuar
                            </Button>
                        </div>
                    ) : (
                        <div className="space-y-6">
                            <FaixaPrecoForm
                                value={faixaPrecoValue}
                                onChange={setFaixaPreco}
                            />

                            <div className="space-y-2">
                                <label
                                    htmlFor="capacidade-maxima"
                                    className="text-lg font-semibold block text-center"
                                >
                                    Capacidade maxima (Opcional)
                                </label>
                                <input
                                    id="capacidade-maxima"
                                    type="number"
                                    className="w-full border rounded-md px-3 py-2"
                                    placeholder="Ex: 50"
                                    value={formData.capacidade_maxima ?? ''}
                                    onChange={(event) =>
                                        setCapacidadeMaxima(event.target.value)
                                    }
                                />
                            </div>

                            <HorariosDiasSemanaForm
                                selectedDays={formData.horarios.dias}
                                toggleDay={toggleDay}
                                value={formData.horarios}
                                onChange={setHorarios}
                            />
                            <DescricaoForm
                                value={formData.descricao}
                                onChange={setDescricao}
                            />
                            <TagsForm
                                tagsDisponiveis={tagsDisponiveis}
                                carregando={carregandoTags}
                                value={formData.tags}
                                onChange={setTags}
                            />
                            <div className="flex gap-4 w-full">
                                <Button
                                    variant="outline"
                                    onClick={() => setStep(1)}
                                    className="flex-1 border-gray-300 text-gray-700 font-bold h-11 rounded-xl hover:bg-gray-100 transition-all"
                                >
                                    Voltar
                                </Button>
                                <Button
                                    className="flex-2 bg-orange-500 hover:bg-orange-600 text-white font-bold h-11 rounded-xl transition-all"
                                    onClick={handleSubmit}
                                    disabled={loading || !podeEnviarEtapa2}
                                >
                                    {loading ? 'Enviando...' : 'Enviar'}
                                </Button>
                            </div>
                            {!podeEnviarEtapa2 && (
                                <p className="text-xs text-gray-500 text-center mt-2">
                                    Preencha descricao, faixa de preco e
                                    horarios para enviar.
                                </p>
                            )}
                            {error && (
                                <div className="text-red-500 text-center mt-2">
                                    {error}
                                </div>
                            )}
                            {success && (
                                <div className="text-green-600 text-center mt-2">
                                    Proposta enviada com sucesso!
                                </div>
                            )}
                        </div>
                    )}
                </div>
            </div>
        </>
    );
}
