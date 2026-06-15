import { salvarViagemPersonalizada } from '@/api/viagem/viagem.fetch';
import { ViagemPOST } from '@/types/viagem';
import { useState } from 'react';

export function useSalvarViagem() {
    const [carregando, setCarregando] = useState(false);
    const [erro, setErro] = useState<string | null>(null);

    async function salvar(viagem: ViagemPOST) {
        setCarregando(true);
        setErro(null);

        try {
            const resposta = await salvarViagemPersonalizada(viagem);
            return resposta;
        } catch (error) {
            setErro('Erro ao salvar a viagem personalizada');
        } finally {
            setCarregando(false);
        }
    }

    return { salvar, carregando, erro };
}
