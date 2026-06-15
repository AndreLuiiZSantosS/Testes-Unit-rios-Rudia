interface TestimonialData {
    id: number;
    username: string;
    time: string;
    text: string;
    image: string;
    likes: number;
}

export default function TestimonialCard({ data }: { data: TestimonialData }) {
    const { username, time, text, image, likes } = data;

    return (
        <div className="bg-white rounded-xl shadow-md p-5 flex flex-col gap-3">
            {/* Header */}
            <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-gray-300" />
                <div className="flex flex-col leading-4">
                    <span className="font-semibold text-[#0f1c40]">
                        {username}
                    </span>
                    <span className="text-xs text-gray-500">{time}</span>
                </div>
            </div>

            {/* Texto */}
            <p className="text-sm text-[#0f1c40]">{text}</p>

            {/* Imagem */}
            <div className="w-full overflow-hidden rounded-lg">
                <img
                    src={image}
                    alt="Publicação"
                    className="w-full h-60 object-cover"
                />
            </div>

            {/* Likes */}
            <div className="flex items-center gap-1 text-[#0f1c40] mt-1">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="#7b3aed"
                    viewBox="0 0 24 24"
                    className="w-5 h-5"
                >
                    <path
                        d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 
          4.42 3 7.5 3c1.74 0 3.41 1 4.5 2.09C13.09 4 
          14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 
          3.78-3.4 6.86-8.55 11.54L12 21.35z"
                    />
                </svg>
                <span className="text-sm font-medium">{likes}</span>
            </div>
        </div>
    );
}
