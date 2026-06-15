'use client';

import { LinhaStatus, CLASSES_LINHA } from '../ProgressoUtils';

type ConectorEtapasProps = {
    status: LinhaStatus;
};

export default function ConectorEtapas({ status }: ConectorEtapasProps) {
    return <div className={CLASSES_LINHA[status]} />;
}
