import React from "react";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { DiaSemanaDTO } from "@/schemas/proposta-servico.schema";

interface Horarios {
  inicio: string;
  fim: string;
  dias: DiaSemanaDTO[];
}

interface HorariosDiasSemanaFormProps {
  value: Horarios;
  onChange: (value: Horarios) => void;
  selectedDays: DiaSemanaDTO[];
  toggleDay: (day: DiaSemanaDTO) => void;
}

const horariosDisponiveis = Array.from({ length: 24 }, (_, hour) => {
  const hourString = String(hour).padStart(2, "0");
  return `${hourString}:00:00`;
});

const diasSemana: Array<{ value: DiaSemanaDTO; label: string }> = [
  { value: "DOM", label: "Dom" },
  { value: "SEG", label: "Seg" },
  { value: "TER", label: "Ter" },
  { value: "QUA", label: "Qua" },
  { value: "QUI", label: "Qui" },
  { value: "SEX", label: "Sex" },
  { value: "SAB", label: "Sab" },
];

export default function HorariosDiasSemanaForm({
  value,
  onChange,
  selectedDays,
  toggleDay,
}: HorariosDiasSemanaFormProps) {
  return (
    <div className="text-center space-y-4">
      <Label className="text-lg font-semibold block">
        Horários e Dias da Semana
      </Label>
      <div className="grid grid-cols-2 gap-4">
        <Select
          value={value.inicio}
          onValueChange={(v) => onChange({ ...value, inicio: v })}
        >
          <SelectTrigger className="w-full">
            <SelectValue placeholder="00:00 h" />
          </SelectTrigger>
          <SelectContent>
            {horariosDisponiveis.map((horario) => (
              <SelectItem key={horario} value={horario}>
                {horario}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
        <Select
          value={value.fim}
          onValueChange={(v) => onChange({ ...value, fim: v })}
        >
          <SelectTrigger className="w-full">
            <SelectValue placeholder="00:00 h" />
          </SelectTrigger>
          <SelectContent>
            {horariosDisponiveis.map((horario) => (
              <SelectItem key={horario} value={horario}>
                {horario}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>
      <div className="flex justify-between gap-1">
        {diasSemana.map((day) => (
          <button
            key={day.value}
            type="button"
            onClick={() => toggleDay(day.value)}
            className={`px-3 py-1 text-xs border rounded-full transition-colors cursor-pointer ${
              selectedDays.includes(day.value)
                ? "bg-zinc-800 text-white border-zinc-800"
                : "bg-white text-gray-500 border-gray-300"
            }`}
          >
            {day.label}
          </button>
        ))}
      </div>
    </div>
  );
}
