
import { Star, StarHalf, Star as StarEmpty } from "lucide-react";

export const EstrelasAvaliacao = (nota: number) => {
    const estrelas = [];

    for (let i = 1; i <= 5; i++) {
        if (nota >= i) {
            estrelas.push(<Star key={i} size={15} className="fill-current text-yellow-400"/>)
        } else if (nota >= i - 0.5){
            estrelas.push(<StarHalf key={i} size={15} className="fill-current text-yellow-400"/>)
        } else {
            estrelas.push(<StarEmpty key={i} size={15} className="text-yellow-400"/>)
        }
    }

    return estrelas;
}