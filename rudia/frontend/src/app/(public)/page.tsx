'use client';

import Header from '@/components/layout/Header';
import Footer from '@/components/layout/Footer';
import Hero from '@/components/home/Hero';
import BannerADoRudia from '@/components/home/BannerADoRudia';
import TestimonialsSection from '@/components/home/Testimonials/TestimonialsSection';
import { SessaoDeCards } from '@/components/common/RoteirosDaComunidade';

export default function Home() {
    return (
        <>
            <Header />
            <Hero />
            <SessaoDeCards titulo="Roteiros da Comunidade" />
            <BannerADoRudia />
            <SessaoDeCards titulo="Lugares mais famosos" />
            <TestimonialsSection />
            <Footer />
        </>
    );
}
