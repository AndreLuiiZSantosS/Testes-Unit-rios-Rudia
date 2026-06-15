export class ApiError extends Error {
    public readonly status: number;
    public readonly data: any;

    constructor(message: string, status: number, data: any = null) {
        super(message);
        this.name = 'ApiError';
        this.status = status;
        this.data = data;

        Object.setPrototypeOf(this, ApiError.prototype);

        if (Error.captureStackTrace) {
            Error.captureStackTrace(this, ApiError);
        }
    }
}
