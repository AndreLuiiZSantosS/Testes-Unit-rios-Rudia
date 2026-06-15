import InputDestino from './Inputs/InputDestino';
import InputDuracao from './Inputs/InputDuracao';
import InputViajantes from './Inputs/InputViajantes';

export default function FormularioDadosIniciais() {
    return (
        <div className="flex flex-col items-center gap-3">
            <p className="text-muted-foreground text-sm">
                Preencha os dados básicos da sua viagem
            </p>
            <div className="flex items-center p-1.5 gap-1.5 border-2 border-amber-600 rounded-md text-xs">
                <InputDestino />
                <InputDuracao />
                <InputViajantes />
            </div>
        </div>
    );
}
