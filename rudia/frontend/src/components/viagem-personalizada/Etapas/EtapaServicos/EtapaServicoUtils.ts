import { CategoriaTypeDTO } from "@/schemas/categoria-tag.schema";

export const HEADER_CONTEUDO_SERVICO: Record<
    number,
    { titulo: string; placeholder: string; categoria: CategoriaTypeDTO }
> = {
    2: {
        categoria: 'Hospedagem',
        titulo: 'Selecione onde deseja ficar',
        placeholder: 'Pesquise por pousada, hotel...',
    },
    3: {
        categoria: 'Lazer',
        titulo: 'Selecione como deseja se divertir',
        placeholder: 'Pesquise por passeios, parques...',
    },
    4: {
        categoria: 'Alimentação',
        titulo: 'Selecione o que deseja comer',
        placeholder: 'Pesquise por restaurantes, bares...',
    },
    5: {
        categoria: 'Transporte',
        titulo: 'Selecione como deseja se locomover',
        placeholder: 'Pesquise por ônibus, carro...',
    },
};