// RoteirosDaComunidade.tsx
import { Card } from "./Card";

export const SessaoDeCards = ({ titulo }: { titulo: string }) => {
	const roteiros = [
		{
			id: 1,
			titulo: "Praias de Natal",
			imagem: "/imagens/informativos/lazer.png",
			usuario: {
				nome: "João Silva",
				avatar: "https://i.pravatar.cc/150?u=joao",
			},
			curtidas: 12,
		},
		{
			id: 2,
			titulo: "Comida de Rua em SP",
			imagem: "/imagens/informativos/alimentacao.png",
			usuario: {
				nome: "Maria Costa",
				avatar: "https://i.pravatar.cc/150?u=maria",
			},
			curtidas: 8,
		},
		{
			id: 3,
			titulo: "Hospedagem em Foz",
			imagem: "/imagens/informativos/hospedagem.png",
			usuario: {
				nome: "Carlos Pereira",
				avatar: "https://i.pravatar.cc/150?u=carlos",
			},
			curtidas: 25,
		},
		{
			id: 4,
			titulo: "Transporte no Rio",
			imagem: "/imagens/informativos/transporte.png",
			usuario: {
				nome: "Ana Souza",
				avatar: "https://i.pravatar.cc/150?u=ana",
			},
			curtidas: 18,
		},
		{
			id: 5,
			titulo: "Passeio em Curitiba",
			imagem: "/imagens/informativos/lazer.png",
			usuario: {
				nome: "Pedro Martins",
				avatar: "https://i.pravatar.cc/150?u=pedro",
			},
			curtidas: 30,
		},
		{
			id: 6,
			titulo: "Sabores da Bahia",
			imagem: "/imagens/informativos/alimentacao.png",
			usuario: {
				nome: "Juliana Lima",
				avatar: "https://i.pravatar.cc/150?u=juliana",
			},
			curtidas: 42,
		},
		{
			id: 7,
			titulo: "Descanso em Minas",
			imagem: "/imagens/informativos/hospedagem.png",
			usuario: {
				nome: "Lucas Fernandes",
				avatar: "https://i.pravatar.cc/150?u=lucas",
			},
			curtidas: 5,
		},
		{
			id: 8,
			titulo: "Aventura na Amazônia",
			imagem: "/imagens/informativos/transporte.png",
			usuario: {
				nome: "Beatriz Alves",
				avatar: "https://i.pravatar.cc/150?u=beatriz",
			},
			curtidas: 55,
		},
	];

	const seisPrimeiros = roteiros.slice(0, 6);

	return (
		<div className="mb-30 px-4 md:px-16 lg:px-60">
			<h2 className="text-2xl font-semibold mb-4">{titulo}</h2>

			{/* Mobile e Tablet → só 6 cards */}
			<div className="grid grid-cols-1 md:grid-cols-3 gap-6 lg:hidden">
				{seisPrimeiros.map((r) => (
					<Card
						key={r.id}
						titulo={r.titulo}
						imagem={r.imagem}
						usuario={r.usuario}
						curtidas={r.curtidas}
					/>
				))}
			</div>

			{/* Desktop → todos os cards */}
			<div className="hidden lg:grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
				{roteiros.map((r) => (
					<Card
						key={r.id}
						titulo={r.titulo}
						imagem={r.imagem}
						usuario={r.usuario}
						curtidas={r.curtidas}
					/>
				))}
			</div>
		</div>
	);
};
