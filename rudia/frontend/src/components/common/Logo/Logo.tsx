import Image from 'next/image';
import Link from 'next/link';

interface LogoProps {
    width: number;
    height: number;
}

export default function Logo({ width, height }: LogoProps) {
    return (
        <Link href="/">
            <Image
                src="/imagens/logo.png"
                alt="Logo do Rudiá"
                width={width}
                height={height}
                unoptimized
                priority
            />
        </Link>
    );
}
