import CardInformativo from './CardInformativo';
import { INFO_VIAGEM_PERSONALIZADA } from './ConteudoInformativo';

export default function VitrineFuncionalidades() {
    return (
        <div className="flex flex-col justify-center items-center mt-8">
            <h2 className="text-indigo-950 text-2xl font-bold text-start w-full mb-4">
                Crie uma viagem e aproveite!
            </h2>
            <div className="flex flex-wrap w-[220px] md:w-[460px] lg:w-[700px] gap-5">
                {INFO_VIAGEM_PERSONALIZADA.map((card) => (
                    <CardInformativo
                        key={card.titulo}
                        titulo={card.titulo}
                        descricao={card.descricao}
                        imagemUrl={card.imagemUrl}
                    />
                ))}
            </div>
        </div>
    );
}
