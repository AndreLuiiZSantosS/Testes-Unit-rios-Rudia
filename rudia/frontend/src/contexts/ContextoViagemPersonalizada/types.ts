import { ViagemPersonalizadaStateDTO } from '@/schemas/viagem.schema';

export interface IViagemPersonalizadaContextType {
    state: ViagemPersonalizadaState;
    atualizarAtributo: <C extends keyof ViagemPersonalizadaStateDTO>(
        campo: C,
        valor: ViagemPersonalizadaStateDTO[C],
    ) => void;
    atualizarEtapa: (payload: number) => void;
    resetViagemPersonalizada: () => void;
}

export interface ViagemPersonalizadaState {
    etapa: number;
    viagem: ViagemPersonalizadaStateDTO;
}

export type AtualizarAtributoActionType<
    C extends keyof ViagemPersonalizadaStateDTO = keyof ViagemPersonalizadaStateDTO,
> = {
    type: 'ATUALIZAR_ATRIBUTO';
    payload: {
        campo: C;
        valor: ViagemPersonalizadaStateDTO[C];
    };
};

export type ViagemPersonalizadaAction =
    | AtualizarAtributoActionType
    | { type: 'ATUALIZAR_ETAPA'; payload: number }
    | { type: 'RESET_VIAGEM_PERSONALIZADA' }
    | { type: 'LOAD_CACHE'; payload: ViagemPersonalizadaState };
