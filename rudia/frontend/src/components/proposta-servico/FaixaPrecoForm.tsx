import React from "react";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";

interface FaixaPrecoFormProps {
  value: { min: string; max: string };
  onChange: (value: { min: string; max: string }) => void;
}

export default function FaixaPrecoForm({ value, onChange }: FaixaPrecoFormProps) {
  return (
    <div className="text-center space-y-4">
      <Label className="text-lg font-semibold block">Faixa de Preço</Label>
      <p className="text-xs text-gray-500">
        Defina um preço mínimo e máximo para os serviços
      </p>
      <div className="grid grid-cols-2 gap-4">
        <Input
          placeholder="Preço mínimo (R$)"
          value={value.min}
          onChange={e => onChange({ ...value, min: e.target.value })}
        />
        <Input
          placeholder="Preço máximo (R$)"
          value={value.max}
          onChange={e => onChange({ ...value, max: e.target.value })}
        />
      </div>
    </div>
  );
}
