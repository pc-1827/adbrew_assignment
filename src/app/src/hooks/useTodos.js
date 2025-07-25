import { useState, useEffect, useCallback } from 'react';
import { getTodos, createTodo } from '../services/api';

export const useTodos = () => {
    const [todos, setTodos] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    // Fetch todos from API
    const fetchTodos = useCallback(async () => {
        try {
            setIsLoading(true);
            setError(null);
            const data = await getTodos();
            setTodos(data);
        } catch (err) {
            setError(err.message || 'Failed to fetch todos');
            console.error('Error fetching todos:', err);
        } finally {
            setIsLoading(false);
        }
    }, []);

    // Add a new todo
    const addTodo = useCallback(async (text) => {
        if (!text.trim()) {
            setError('Todo text cannot be empty');
            return false;
        }

        try {
            setIsLoading(true);
            await createTodo(text);
            await fetchTodos();
            return true;
        } catch (err) {
            setError(err.message || 'Failed to add todo');
            console.error('Error adding todo:', err);
            return false;
        } finally {
            setIsLoading(false);
        }
    }, [fetchTodos]);

    useEffect(() => {
        fetchTodos();
    }, [fetchTodos]);

    return {
        todos,
        isLoading,
        error,
        fetchTodos,
        addTodo,
        clearError: () => setError(null),
    };
};

export default useTodos;