import TestimonialCard from "./TestimonialCard";

const testimonials = [
	{
		id: 1,
		username: "Username",
		time: "há 2 dias",
		text: "Descobrindo um pouco da vida noturna de Pipa. Experiência incrível!",
		image: "/imagens/informativos/comunidade.png",
		likes: 124,
	},
	{
		id: 2,
		username: "Username",
		time: "há 5 dias",
		text: "Experimentando um pouco do frio da serra de Martins. Ótima opção nesse inverno!",
		image: "/imagens/informativos/comunidade.png",
		likes: 185,
	},
];

export default function TestimonialsSection() {
	return (
		<section className="mb-30 w-full px-4 lg:px-60 md:px-8">
			<div className="flex justify-between items-center mb-6">
				<h2 className="text-2xl font-bold text-[#0f1c40]">
					O que estão dizendo
				</h2>

				<button className="flex items-center gap-1 text-sm font-medium text-[#0f1c40]">
					Ver mais →
				</button>
			</div>

			<div className="grid grid-cols-1 md:grid-cols-2 gap-6">
				{testimonials.map((item) => (
					<TestimonialCard key={item.id} data={item} />
				))}
			</div>
		</section>
	);
}
