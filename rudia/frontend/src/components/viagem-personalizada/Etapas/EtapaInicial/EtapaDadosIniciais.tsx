'use client';

import FormularioDadosIniciais from './FormularioDadosIniciais';
import VitrineFuncionalidades from './Vitrine/VitrineFuncionalidades';

export default function EtapaDadosIniciais() {
    return (
        <div className="flex flex-col items-center mt-10 space-y-6">
            <FormularioDadosIniciais />
            <VitrineFuncionalidades />
        </div>
    );
}
