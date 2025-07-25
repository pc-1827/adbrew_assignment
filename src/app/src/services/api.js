const API_BASE_URL = process.env.REACT_APP_API_URL;
// console.log('API BASE URL:', API_BASE_URL); 

export const getTodos = async () => {
    const response = await fetch(`${API_BASE_URL}/todos/`);

    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
    }

    return response.json();
};

export const createTodo = async (text) => {
    const response = await fetch(`${API_BASE_URL}/todos/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
    });

    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
    }

    return response.json();
};