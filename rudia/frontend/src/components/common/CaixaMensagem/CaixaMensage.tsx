import { ReactNode } from 'react';
import { Check, X } from 'lucide-react';

interface CaixaMensagemProps {
    mensagens: string[];
    status: 'SUCESSO' | 'ERRO';
}

export default function CaixaMensagem({
    mensagens,
    status,
}: CaixaMensagemProps) {
    const formatoMensagem: Record<
        'SUCESSO' | 'ERRO',
        { icone: ReactNode; estilo: string }
    > = {
        SUCESSO: {
            icone: <Check className="w-5 h-5" />,
            estilo: 'text-green-700',
        },
        ERRO: {
            icone: <X className="w-5 h-5" />,
            estilo: 'text-red-700',
        },
    };

    return (
        <div
            className={`
                ${formatoMensagem[status].estilo}
                flex justify-center items-center gap-2 m-auto
            `}
        >
            {formatoMensagem[status].icone}
            {mensagens.map((mensagem, index) => (
                <p key={index}>{mensagem}</p>
            ))}
        </div>
    );
}
