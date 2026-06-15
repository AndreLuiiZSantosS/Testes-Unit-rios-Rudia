"use client";

import React, { useState } from "react";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { obterEnderecoPorCep } from "@/api/cidade/cep.fetch";

interface Endereco {
  cep: string;
  logradouro: string;
  numero: string;
  complemento?: string;
}

interface EnderecoEmpresaFormProps {
  value: Endereco;
  onChange: (value: Endereco) => void;
}

export default function EnderecoEmpresaForm({
  value,
  onChange,
}: EnderecoEmpresaFormProps) {
  const [isLocked, setIsLocked] = useState(false);
  const [erroCep, setErroCep] = useState<string | null>(null);

  const handleCepBlur = async () => {
    const sanitizedCep = value.cep.replace(/\D/g, "");
    if (sanitizedCep.length !== 8) return;

    try {
      setErroCep(null);
      const endereco = await obterEnderecoPorCep(sanitizedCep);

      // Preenche o endereço e bloqueia campos
      onChange({
        ...value,
        logradouro: endereco.logradouro,
      });
      setIsLocked(true);
    } catch (error) {
      onChange({
        ...value,
        logradouro: "",
      });
      setIsLocked(false);
      setErroCep("Nao foi possivel consultar o CEP informado.");
    }
  };

  return (
    <>
      <div className="grid grid-cols-2 gap-4">
        <div className="space-y-2">
          <Label>CEP</Label>
          <Input
            placeholder="Digite o CEP"
            value={value.cep}
            onChange={(e) => onChange({ ...value, cep: e.target.value })}
            onBlur={handleCepBlur}
          />
        </div>
        <div className="space-y-2">
          <Label>Endereço</Label>
          <Input
            placeholder="Rua / Avenida"
            value={value.logradouro}
            onChange={(e) => onChange({ ...value, logradouro: e.target.value })}
            disabled={isLocked}
          />
        </div>
      </div>

      {erroCep && <p className="text-xs text-red-500">{erroCep}</p>}

      <div className="space-y-2">
        <Label>Complemento (Opcional)</Label>
        <Input
          placeholder="Apartamento, bloco, sala..."
          value={value.complemento || ""}
          onChange={(e) => onChange({ ...value, complemento: e.target.value })}
        />
      </div>

      <div className="space-y-2">
        <div className="space-y-2">
          <Label>Número</Label>
          <Input
            placeholder="Nº"
            value={value.numero}
            onChange={(e) => onChange({ ...value, numero: e.target.value })}
          />
        </div>
        <p className="text-xs text-gray-500">
          A rua pode ser preenchida automaticamente ao informar o CEP.
        </p>
      </div>
    </>
  );
}
