export type InfoViagemPersonalizada = {
    titulo: string;
    descricao: string;
    imagemUrl: string;
};

export const INFO_VIAGEM_PERSONALIZADA: InfoViagemPersonalizada[] = [
    {
        titulo: 'Hospedagens',
        descricao:
            'Escolha entre hóteis, pousadas, casas, apartamentos, resorts e muito mais!',
        imagemUrl: '/imagens/informativos/hospedagem.png',
    },
    {
        titulo: 'Lazer',
        descricao:
            'Praias, cinemas, parques, trilhas; tudo de acordo com as suas preferências.',
        imagemUrl: '/imagens/informativos/lazer.png',
    },
    {
        titulo: 'Gastronomia',
        descricao:
            'Descubra seu próximo restaurante favorito: do barzinho regional à pizzaria italiana.',
        imagemUrl: '/imagens/informativos/alimentacao.png',
    },
    {
        titulo: 'Transporte',
        descricao:
            'Inclua seu meio de transporte no planejamento e tenha tudo à mão sempre!',
        imagemUrl: '/imagens/informativos/transporte.png',
    },
    {
        titulo: 'Pontos turísticos',
        descricao:
            'Desfrute o melhor de cada cidade! Veja centros históricos, museus e parques naturais.',
        imagemUrl: '/imagens/informativos/ponto_turistico.png',
    },
    {
        titulo: 'Comunidade',
        descricao:
            'Se junte com quem compartilha do mesmo amor por viajar que você; viajar é compartilhar!',
        imagemUrl: '/imagens/informativos/comunidade.png',
    },
];
