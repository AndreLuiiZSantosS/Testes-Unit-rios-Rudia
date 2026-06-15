import { obterServicoPorId } from '@/api/servico/servico.fetch';
import { ServicoCompletoDTO } from '@/schemas/servico.schema';
import { useEffect, useState } from 'react';

export function useServicoPorId(id: number | null) {
    const [servico, setServico] = useState<ServicoCompletoDTO | null>(null);
    const [carregando, setCarregando] = useState(true);
    const [erro, setErro] = useState<string | null>(null);

    useEffect(() => {
        if (!id) {
            setServico(null);
            setCarregando(false);
            setErro(null);
            return;
        }

        const carregarServico = async () => {
            try {
                setServico(null);
                setCarregando(true);
                setErro(null);

                const resposta = await obterServicoPorId(id);
                
                setServico(resposta);
            } catch (err) {
                console.error(err);
                setErro('Ocorreu um erro ao buscar o serviço');
            } finally {
                setCarregando(false);
            }
        };

        carregarServico();
    }, [id]);

    return { servico, carregando, erro };
}
