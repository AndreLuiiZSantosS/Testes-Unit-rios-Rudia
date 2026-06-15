import { obterCidades } from '@/api/cidade/cidade.fetch';
import { ListaCidadesResponseDTO } from '@/schemas/cidade-estado.schema';
import { useEffect, useState } from 'react';

// Observação: no momento apenas uma função para obter todas as cidades, futuramente colocar filtros
export function useCidades() {
    const [cidades, setCidades] = useState<ListaCidadesResponseDTO | null>(null);
    const [carregando, setCarregando] = useState(true);
    const [erro, setErro] = useState<string | null>(null);

    useEffect(() => {
        const carregarCidades = async () => {
            try {
                const cache = localStorage.getItem('cidades');

                if (cache) {
                    setCidades(JSON.parse(cache));
                    return;
                }

                const resposta = await obterCidades();
                const cidades = resposta;

                localStorage.setItem('cidades', JSON.stringify(cidades));
                setCidades(cidades);
            } catch {
                setErro('Ocorreu um erro ao buscar as cidades');
            } finally {
                setCarregando(false);
            }
        };

        carregarCidades();
    }, []);

    return { cidades, carregando, erro };
}
