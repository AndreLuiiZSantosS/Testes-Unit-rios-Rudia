import { ViagemPersonalizadaState, ViagemPersonalizadaAction } from './types';

export const initialState: ViagemPersonalizadaState = {
    etapa: 1,
    viagem: {
        nome: '',
        descricao: '',
        dias: null,
        viajantes_adultos: 0,
        viajantes_criancas: 0,
        visibilidade: 'PRIVADO',
        cidade_destino: null,
        hospedagem: null,
        transporte: null,
        alimentacao: [],
        lazer: [],
    },
};

export const reducer = (
    state: ViagemPersonalizadaState,
    action: ViagemPersonalizadaAction,
): ViagemPersonalizadaState => {
    switch (action.type) {
        case 'ATUALIZAR_ATRIBUTO':
            return {
                ...state,
                viagem: {
                    ...state.viagem,
                    [action.payload.campo]: action.payload.valor,
                },
            };
        case 'ATUALIZAR_ETAPA':
            return { ...state, etapa: action.payload };
        case 'RESET_VIAGEM_PERSONALIZADA':
            return initialState;
        case 'LOAD_CACHE':
            return action.payload;
        default:
            return state;
    }
};
