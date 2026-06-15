'use client';

import { CirculoStatus, CLASSES_CIRCULO } from '../ProgressoUtils';

type ItemEtapaProps = {
    icon: React.ReactNode;
    status: CirculoStatus;
};

export default function ItemEtapa({ icon, status }: ItemEtapaProps) {
    return <div className={CLASSES_CIRCULO[status]}>{icon}</div>;
}
