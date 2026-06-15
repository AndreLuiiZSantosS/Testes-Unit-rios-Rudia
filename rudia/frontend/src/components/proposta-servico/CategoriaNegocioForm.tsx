import React from "react";
import { Label } from "@/components/ui/label";
import { CategoriaDTO } from "@/schemas/categoria-tag.schema";
import {
  Select,
  SelectTrigger,
  SelectValue,
  SelectContent,
  SelectItem,
} from "@/components/ui/select";

interface CategoriaNegocioFormProps {
  value: number;
  onChange: (value: number) => void;
  categorias: CategoriaDTO[];
  carregando: boolean;
}

export default function CategoriaNegocioForm({
  value,
  onChange,
  categorias,
  carregando,
}: CategoriaNegocioFormProps) {
  return (
    <div className="text-center">
      <Label className="text-lg font-semibold block mb-4">
        Selecione a categoria do seu negócio
      </Label>
      <Select
        value={value ? String(value) : ""}
        onValueChange={(selected) => onChange(Number(selected))}
      >
        <SelectTrigger className="w-full">
          <SelectValue placeholder="Selecione a Categoria" />
        </SelectTrigger>
        <SelectContent>
          {carregando && (
            <SelectItem value="0" disabled>
              Carregando categorias...
            </SelectItem>
          )}
          {!carregando &&
            categorias.map((categoria) => (
              <SelectItem key={categoria.id} value={String(categoria.id)}>
                {categoria.nome}
              </SelectItem>
            ))}
        </SelectContent>
      </Select>
    </div>
  );
}
