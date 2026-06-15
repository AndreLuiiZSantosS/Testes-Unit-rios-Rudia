'use client';

import Link, { LinkProps } from 'next/link';
import { usePathname } from 'next/navigation';
import { cn } from '@/lib/utils';

type ActiveLinkProps = LinkProps & {
    children: React.ReactNode;
};

export function ActiveLink({ children, href, ...rest }: ActiveLinkProps) {
    const pathname = usePathname();
    const isCurrentPath =
        pathname === href ||
        pathname === rest.as ||
        (rest.as && pathname?.startsWith(String(rest.as) + '/'));

    return (
        <Link
            href={href}
            className={cn(
                'text-sm font-medium transition-colors hover:text-orange-500',
                isCurrentPath
                    ? 'text-orange-500 font-bold'
                    : 'text-muted-foreground',
            )}
            {...rest}
        >
            {children}
        </Link>
    );
}
