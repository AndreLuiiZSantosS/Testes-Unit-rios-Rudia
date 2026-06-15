// Formatação para Datas no Formato ISO - AAAA-MM-DD
export const formatarDataISO = (data: Date | string | null) => {
    if (!data) return '';
    const d = new Date(data);
    return d.toISOString().split('T')[0];
};

// Formatação de Preço - R$ X,XX
export const formatarPreco = (preco: number | string) => {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL',
    }).format(Number(preco));
};

// Mascara de Formatação para os Dias da Viagem
export const formatarDias = (valor: number | null): string => {
    if (valor === null) return '';
    return valor.toString();
};

export const converterDias = (valor: string): number | null => {
    const apenasNumeros = valor.replace(/\D/g, '');

    if (!apenasNumeros) return null;

    const numero = Number(apenasNumeros);

    return Math.min(Math.max(numero, 1), 999);
};

// Formatação de CNPJ - 00.000.000/0000-00
export const formatarCNPJ = (value: string) => {
    let v = value.replace(/\D/g, '');
    if (v.length > 14) v = v.slice(0, 14);
    v = v.replace(/^(\d{2})(\d)/, '$1.$2');
    v = v.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
    v = v.replace(/\.(\d{3})(\d)/, '.$1/$2');
    v = v.replace(/(\d{4})(\d)/, '$1-$2');
    return v;
};
