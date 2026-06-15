// Card.tsx
import {
	Card as ShadcnCard,
	CardContent,
	CardFooter,
	CardHeader,
	CardTitle,
} from "../ui/card";
import { Heart } from "lucide-react";

interface CardProps {
	imagem: string;
	titulo: string;
	usuario: {
		nome: string;
		avatar: string;
	};
	curtidas: number;
}

export const Card = ({ imagem, titulo, usuario, curtidas }: CardProps) => {
	return (
		<ShadcnCard className="w-full h-[280px] flex flex-col overflow-hidden transition-transform duration-200 hover:scale-102 cursor-pointer pt-0">
			{/* Imagem do roteiro - 3/5 da altura */}
			<div className="relative h-[70%] w-full overflow-hidden">
				<img
					src={imagem}
					alt={titulo}
					className="block h-full w-full object-cover"
				/>
			</div>

			{/* Conteúdo do card - 2/5 da altura */}
			<div className="h-[40%] flex flex-col justify-between px-3">
				<CardHeader className="p-0">
					<CardTitle className="text-base truncate">{titulo}</CardTitle>
				</CardHeader>

				<CardContent className="flex items-center gap-2 p-0 mb-2">
					<img
						src={usuario.avatar}
						alt={usuario.nome}
						className="w-7 h-7 rounded-full object-cover"
					/>
					<span className="text-sm font-medium truncate">{usuario.nome}</span>
				</CardContent>
				
				<CardFooter className="flex items-center p-0 gap-1">
					<Heart className="text-red-500" size={16} />
					<span className="text-xs">{curtidas}</span>
				</CardFooter>
			</div>
		</ShadcnCard>
	);
};
