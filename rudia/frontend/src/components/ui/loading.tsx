
import { Loader2 } from "lucide-react";
import { cn } from "@/lib/utils";

interface LoaderProps {
  text?: string;
  className?: string;
}

export function Loader({ text, className }: LoaderProps) {
  return (
    <div className={cn("flex flex-col justify-center items-center h-24 text-primary", className)}>
      <Loader2 className="w-6 h-6 animate-spin mb-1" />
      {text && <span className="text-sm text-muted-foreground">{text}</span>}
    </div>
  );
}
