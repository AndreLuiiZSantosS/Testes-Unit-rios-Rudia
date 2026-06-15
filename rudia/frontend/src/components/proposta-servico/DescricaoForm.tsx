import React from "react";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";

interface DescricaoFormProps {
  value: string;
  onChange: (value: string) => void;
}

export default function DescricaoForm({ value, onChange }: DescricaoFormProps) {
  return (
    <div className="space-y-2">
      <Label className="text-lg font-semibold block text-center">
        Descrição
      </Label>
      <div className="px-2">
        <Textarea
          placeholder="Forneça uma descrição do seu negócio"
          className="min-h-[100px] resize-none"
          value={value}
          onChange={e => onChange(e.target.value)}
        />
      </div>
    </div>
  );
}
