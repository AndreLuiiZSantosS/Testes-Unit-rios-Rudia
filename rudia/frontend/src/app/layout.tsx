import './globals.css';
import { Inter } from 'next/font/google';
import { AutenticacaoProvider } from '@/contexts/ContextoAutenticacao';

const inter = Inter({
    weight: ['400', '500', '700'],
    subsets: ['latin'],
});

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="pt-BR">
            <body className={inter.className}>
                <div className="relative min-h-screen">
                    <AutenticacaoProvider>{children}</AutenticacaoProvider>
                </div>
            </body>
        </html>
    );
}
