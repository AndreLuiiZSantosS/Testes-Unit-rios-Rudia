import { ViagemPersonalizadaStateDTO } from '@/schemas/viagem.schema';
import {
    BusFront,
    FerrisWheel,
    Hotel,
    Luggage,
    Plane,
    Utensils,
} from 'lucide-react';

// ─── Tipos ───
export type CirculoStatus = 'concluida' | 'atual' | 'pendente';

export type LinhaStatus =
    | 'concluida'
    | 'concluida_atual'
    | 'pendente_atual'
    | 'pendente'
    | 'pendente_concluida';

export type ConfiguracaoEtapa = {
    id: number;
    icon: React.ReactNode;
    check: (v: ViagemPersonalizadaStateDTO) => boolean;
};

// ─── Classes Base ───
const CLASSES_BASE_CIRCULO =
    'flex justify-center items-center w-8 h-8 rounded-full text-white transition-all duration-300 ease-in-out';

const CLASSES_BASE_LINHA = 'h-1 w-8 md:w-16 lg:w-24';

export const CLASSES_BASE_ICONES = 'size-5';

// ─── Mapeamento de Estilos ───
export const CLASSES_CIRCULO: Record<CirculoStatus, string> = {
    concluida: `${CLASSES_BASE_CIRCULO} bg-green-800 scale-110`,
    atual: `${CLASSES_BASE_CIRCULO} bg-amber-600 scale-125`,
    pendente: `${CLASSES_BASE_CIRCULO} bg-muted-foreground scale-100`,
};

export const CLASSES_LINHA: Record<LinhaStatus, string> = {
    concluida: `${CLASSES_BASE_LINHA} bg-green-800`,
    concluida_atual: `${CLASSES_BASE_LINHA} bg-linear-to-r from-green-800 to-amber-600`,
    pendente_atual: `${CLASSES_BASE_LINHA} bg-linear-to-r from-muted-foreground to-amber-600`,
    pendente: `${CLASSES_BASE_LINHA} bg-muted-foreground`,
    pendente_concluida: `${CLASSES_BASE_LINHA} bg-linear-to-r from-muted-foreground to-green-800`,
};

// ─── Configuração das Etapas ───
export const ETAPAS: ConfiguracaoEtapa[] = [
    {
        id: 1,
        icon: <Luggage className={CLASSES_BASE_ICONES} />,
        check: (v) => !!v.cidade_destino && !!v.dias && !!v.viajantes_adultos,
    },
    {
        id: 2,
        icon: <Hotel className={CLASSES_BASE_ICONES} />,
        check: (v) => !!v.hospedagem,
    },
    {
        id: 3,
        icon: <FerrisWheel className={CLASSES_BASE_ICONES} />,
        check: (v) => v.lazer.length > 0,
    },
    {
        id: 4,
        icon: <Utensils className={CLASSES_BASE_ICONES} />,
        check: (v) => v.alimentacao.length > 0,
    },
    {
        id: 5,
        icon: <BusFront className={CLASSES_BASE_ICONES} />,
        check: (v) => !!v.transporte,
    },
    {
        id: 6,
        icon: <Plane className={CLASSES_BASE_ICONES} />,
        check: (v) => !!v.nome && !!v.descricao && !!v.visibilidade,
    },
];
