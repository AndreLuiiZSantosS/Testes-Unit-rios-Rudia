import Image from "next/image";
import Link from "next/link";

export default function BannerADoRudia() {
	return (
		<section className="mb-30 px-4 md:px-16 lg:px-60 my-8">
			<div className="relative bg-[#FFE4CC] rounded-2xl overflow-hidden px-5 md:px-10 py-20 lg:py-15">
				{/* A mais suave no mobile/tablet, normal no desktop */}
				<Image
					src="/imagens/AdoRudia.png"
					alt="A do Rudiá"
					width={260}
					height={260}
					className="
						block 
						absolute top-0 left-0 

						opacity-10
						sm:opacity-35
						lg:opacity-100

						sm:w-[220px] sm:h-auto 
						md:w-[250px] 
						lg:w-[180px] 
						transition-all
					"
				/>

				<div
					className="
						grid grid-cols-1 
						lg:grid-cols-[1fr_2fr_1fr] 
						items-center gap-6 relative
					"
				>
					{/* COLUNA 1 — espaço para o "A" */}
					<div className="hidden lg:flex"></div>

					{/* Texto central */}
					<div className="flex flex-col items-center text-center z-10">
						<h3 className="text-3xl sm:text-4xl font-semibold drop-shadow-md">
							Viaje da melhor forma!
						</h3>

						<p className="text-base sm:text-lg mt-3 max-w-md drop-shadow">
							Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
							eiusmod tempor incididunt ut labore et.
						</p>
					</div>

					{/* Botão */}
					<div className="flex justify-center lg:justify-end items-center w-full">
						<Link
							href="#"
							className="
								bg-orange-500 text-white font-medium 
								px-5 py-3 
								rounded-xl shadow 
								hover:bg-orange-600 transition 
								w-full sm:w-full lg:w-auto
								text-center
								text-lg
							"
						>
							Cadastre-se
						</Link>
					</div>
				</div>
			</div>
		</section>
	);
}
