import React, { useMemo, useState } from "react";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { TagDTO } from "@/schemas/categoria-tag.schema";

interface TagsFormProps {
  tagsDisponiveis: TagDTO[];
  carregando: boolean;
  value: number[];
  onChange: (tags: number[]) => void;
}

export default function TagsForm({
  tagsDisponiveis,
  carregando,
  value,
  onChange,
}: TagsFormProps) {
  const toggleTag = (tagId: number) => {
    if (value.includes(tagId)) {
      onChange(value.filter((id) => id !== tagId));
      return;
    }

    onChange([...value, tagId]);
  };

  const removeTag = (tagId: number) => {
    onChange(value.filter((id) => id !== tagId));
  };

  const nomePorId = new Map(tagsDisponiveis.map((tag) => [tag.id, tag.nome]));

  const [query, setQuery] = useState("");

  const sugestoes = useMemo(() => {
    if (!query) return [];
    const q = query.toLowerCase();
    return tagsDisponiveis
      .filter((t) => !value.includes(t.id))
      .filter((t) => t.nome.toLowerCase().includes(q))
      .slice(0, 8);
  }, [query, tagsDisponiveis, value]);

  // ? Por que não integrar com o servidor aqui? Porque o backend pode
  // ? retornar uma lista parcial; integração ficará para a próxima versão.
  return (
    <div className="space-y-4 text-center">
      <Label className="text-lg font-semibold block">Tags</Label>

      {carregando && (
        <p className="text-xs text-gray-500">Carregando tags da categoria...</p>
      )}

      {!carregando && tagsDisponiveis.length === 0 && (
        <p className="text-xs text-gray-500">Nenhuma tag disponível.</p>
      )}

      {!carregando && tagsDisponiveis.length > 0 && (
        <div className="space-y-2">
          <Input
            placeholder="Pesquisar tags por nome (ex: espor)"
            value={query}
            onChange={(e) => setQuery(String(e.target.value))}
          />

          {sugestoes.length > 0 && (
            <div className="bg-white border rounded-md mt-1 max-h-40 overflow-auto text-left p-2">
              {sugestoes.map((s) => (
                <button
                  key={s.id}
                  type="button"
                  onClick={() => {
                    toggleTag(s.id);
                    setQuery("");
                  }}
                  className="w-full text-left px-2 py-1 hover:bg-zinc-50 text-sm"
                >
                  {s.nome}
                </button>
              ))}
            </div>
          )}

          <div className="flex flex-wrap gap-2 justify-center mt-2">
            {tagsDisponiveis.map((tag) => (
              <button
                key={tag.id}
                type="button"
                onClick={() => toggleTag(tag.id)}
                className={`px-3 py-1 rounded-xl border text-xs transition-colors cursor-pointer ${
                  value.includes(tag.id)
                    ? "bg-zinc-800 text-white border-zinc-800"
                    : "bg-white text-gray-700 border-gray-300"
                }`}
              >
                {tag.nome}
              </button>
            ))}
          </div>
        </div>
      )}

      {value.length > 0 && (
        <div className="flex flex-wrap gap-2 justify-center mt-2">
          {value.map((tagId) => (
            <span
              key={tagId}
              className="bg-zinc-800 text-white px-3 py-1 rounded-xl flex items-center gap-2 text-xs"
            >
              <span>{nomePorId.get(tagId) ?? `#${tagId}`}</span>
              {/* // Este botão remove apenas localmente. */}
              <button
                type="button"
                aria-label={`Remover tag ${tagId}`}
                onClick={() => removeTag(tagId)}
                className="ml-2 text-sm opacity-80 hover:opacity-100"
              >
                ×
              </button>
            </span>
          ))}
        </div>
      )}
    </div>
  );
}
