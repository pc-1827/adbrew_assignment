import { getTodos, createTodo } from './api';

// Mock fetch
global.fetch = jest.fn();

describe('API Service', () => {
    beforeEach(() => {
        jest.resetAllMocks();
    });

    test('getTodos fetches todos successfully', async () => {
        // Setup
        const mockTodos = [{ _id: '1', text: 'Test todo' }];
        global.fetch.mockResolvedValueOnce({
            ok: true,
            json: async () => mockTodos
        });

        // Execute
        const result = await getTodos();

        // Verify
        expect(global.fetch).toHaveBeenCalledWith(expect.stringContaining('/todos/'));
        expect(result).toEqual(mockTodos);
    });

    test('createTodo creates a todo successfully', async () => {
        // Setup
        const newTodo = { id: '2', text: 'New todo' };
        global.fetch.mockResolvedValueOnce({
            ok: true,
            json: async () => newTodo
        });

        // Execute
        const result = await createTodo('New todo');

        // Verify
        expect(global.fetch).toHaveBeenCalledWith(
            expect.stringContaining('/todos/'),
            expect.objectContaining({
                method: 'POST',
                body: JSON.stringify({ text: 'New todo' })
            })
        );
        expect(result).toEqual(newTodo);
    });
});