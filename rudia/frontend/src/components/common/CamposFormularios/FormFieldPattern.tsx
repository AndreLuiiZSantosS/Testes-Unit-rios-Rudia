'use client';

import {
    FormControl,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import { cn } from '@/lib/utils';
import { ReactNode } from 'react';
import { Control, FieldValues, Path } from 'react-hook-form';

interface FormFieldPatternProps<T extends FieldValues> {
    control: Control<T>;
    field: Path<T>;
    placeholder: string;
    type?: string;
    label?: string | ReactNode;
    rightIcon?: ReactNode;
    leftIcon?: ReactNode;
    className?: string;
    loading?: boolean;
}

export default function FormFieldPattern<T extends FieldValues>({
    ...props
}: FormFieldPatternProps<T>) {
    return (
        <FormField
            control={props.control}
            name={props.field}
            render={({ field }) => (
                <FormItem>
                    {props.label && (
                        <FormLabel className="data-[error=true]:text-primary text-sm font-medium">
                            {props.label}
                        </FormLabel>
                    )}

                    <FormControl>
                        <div className="relative flex items-center">
                            {props.leftIcon && (
                                <span className="absolute left-3 text-muted-foreground">
                                    {props.leftIcon}
                                </span>
                            )}

                            <Input
                                {...field}
                                type={props.type}
                                placeholder={props.placeholder}
                                className={cn(
                                    'px-4 py-5 focus-visible:outline-none focus-visible:ring-0',
                                    props.rightIcon && 'pr-10',
                                    props.leftIcon && 'pl-10',
                                    props.className,
                                )}
                                disabled={props.loading}
                            />

                            {props.rightIcon && (
                                <span className="absolute right-3 cursor-pointer">
                                    {props.rightIcon}
                                </span>
                            )}
                        </div>
                    </FormControl>

                    <FormMessage className="text-xs text-red-700" />
                </FormItem>
            )}
        />
    );
}
