import React from "react";
import { UploadCloud } from "lucide-react";

interface UploadFotosNegocioProps {
  value: string;
  onChange: (imagemCapaBase64: string) => void;
}

export default function UploadFotosNegocio({
  value,
  onChange,
}: UploadFotosNegocioProps) {
  const handleUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const arquivo = event.target.files?.[0];

    if (!arquivo) return;

    const base64 = await new Promise<string>((resolve, reject) => {
      const reader = new FileReader();

      reader.onload = () => resolve(String(reader.result || ""));
      reader.onerror = () => reject(new Error("Erro ao ler a imagem"));

      reader.readAsDataURL(arquivo);
    });

    onChange(base64);
  };

  return (
    <label className="border-2 border-dashed border-gray-200 rounded-lg p-8 flex flex-col items-center justify-center text-gray-400 cursor-pointer hover:bg-gray-50 transition-colors">
      <input
        type="file"
        accept="image/*"
        onChange={handleUpload}
        className="hidden"
      />
      <UploadCloud className="w-10 h-10 mb-2" />
      <p>Envie a imagem de capa do seu negocio</p>
      <div className="mt-2 text-xs text-gray-500">
        {value ? "Imagem selecionada" : "Clique para selecionar"}
      </div>
    </label>
  );
}
