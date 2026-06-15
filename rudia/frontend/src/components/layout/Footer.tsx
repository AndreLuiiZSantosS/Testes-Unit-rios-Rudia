import Image from "next/image";

export default function Footer() {
	return (
		<footer className="bg-[#1F6B3A] text-white rounded-t-2xl px-6 md:px-16 lg:px-60 pt-12 pb-8">
			{/* GRID SUPERIOR */}
			<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-10">
				{/* COLUNA 1 */}
				<div>
					<h3 className="font-semibold mb-3">Quem somos</h3>
					<ul className="space-y-2 text-sm opacity-90">
						<li>Nossa história</li>
						<li>Valores da empresa</li>
						<li>Trabalhe conosco</li>
						<li>Políticas</li>
					</ul>
				</div>

				{/* COLUNA 2 */}
				<div>
					<h3 className="font-semibold mb-3">Dúvidas</h3>
					<ul className="space-y-2 text-sm opacity-90">
						<li>Cancelamentos</li>
						<li>Torne-se um parceiro</li>
						<li>Criação de roteiros</li>
						<li>Publicações</li>
						<li>Viagens compartilhadas</li>
						<li>Denúncias de conteúdo</li>
					</ul>
				</div>

				{/* COLUNA 3 */}
				<div>
					<h3 className="font-semibold mb-3">Privacidade</h3>
					<ul className="space-y-2 text-sm opacity-90">
						<li>Criptografia</li>
						<li>Pagamento seguro</li>
						<li>Mensagens privadas</li>
					</ul>
				</div>

				{/* COLUNA 4 */}
				<div>
					<h3 className="font-semibold mb-3">Segurança</h3>
					<ul className="space-y-2 text-sm opacity-90">
						<li>Localização compartilhada</li>
						<li>Seguros de viagem</li>
						<li>Dicas de segurança</li>
					</ul>
				</div>

				{/* COLUNA 5 */}
				<div>
					<h3 className="font-semibold mb-3">Onde estamos</h3>
					<div className="flex items-center gap-4 mt-4">
						<div className="w-6 h-6 bg-gray-300 rounded-full"></div>
						<div className="w-6 h-6 bg-gray-300 rounded-full"></div>
						<div className="w-6 h-6 bg-gray-300 rounded-full"></div>
					</div>
				</div>
			</div>

			{/* LINHA INFERIOR */}
			<div className="mt-12 flex flex-col md:flex-row items-center justify-center gap-8">
				{/* Logo */}
				<Image
					src="/logo_rudia_branco.png"
					alt="Rudiá"
					width={90}
					height={90}
					className="opacity-90"
				/>

				{/* Texto */}
				<p className="text-sm opacity-80 max-w-xl">
					Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
					eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
					minim veniam
				</p>
			</div>
		</footer>
	);
}
