import React from "react";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { CidadeDTO } from "@/schemas/cidade-estado.schema";

interface CidadeAtuacaoFormProps {
  value: number;
  onChange: (value: number) => void;
  cidades: CidadeDTO[];
  carregando: boolean;
}

export default function CidadeAtuacaoForm({
  value,
  onChange,
  cidades,
  carregando,
}: CidadeAtuacaoFormProps) {
  const cidadesDisponiveis = Array.isArray(cidades) ? cidades : [];

  return (
    <div className="text-center">
      <Label className="text-lg font-semibold block mb-4">
        Cidade de atuacao do servico
      </Label>
      <Select
        value={value ? String(value) : ""}
        onValueChange={(selected) => onChange(Number(selected))}
      >
        <SelectTrigger className="w-full">
          <SelectValue placeholder="Selecione a cidade" />
        </SelectTrigger>
        <SelectContent>
          {carregando && (
            <SelectItem value="0" disabled>
              Carregando cidades...
            </SelectItem>
          )}
          {!carregando &&
            cidadesDisponiveis.map((cidade) => (
              <SelectItem key={cidade.id} value={String(cidade.id)}>
                {cidade.nome} - {cidade.estado.sigla}
              </SelectItem>
            ))}
        </SelectContent>
      </Select>
    </div>
  );
}
