import { Input } from "@/components/ui/input";
import { Search } from "lucide-react";

interface BarraPesquisaProps {
    placeholder?: string;
    value?: string;
    onChange?: (value: string) => void;
}

export default function BarraPesquisa({ placeholder, value, onChange }: BarraPesquisaProps) {
    return (
        <div className="relative flex items-center w-fit">
            <Search className="absolute text-muted-foreground size-5 left-2"/>
            <Input
                type="text" 
                placeholder={placeholder || "Pesquise aqui..."}
                value={value}
                onChange={(evento) => onChange && onChange(evento.target.value)}
                className="
                    border-indigo-950 
                    w-sm md:w-md lg:w-lg h-10 pl-8 rounded-sm
                    focus-visible:outline-none focus-visible:ring-0 focus-visible:border-indigo-950
                "
            />
        </div>
    )
}