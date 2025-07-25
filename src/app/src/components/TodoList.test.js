import { render } from '@testing-library/react';
import TodoList from './TodoList';

describe('TodoList component', () => {
    test('renders loading state', () => {
        const { getByText } = render(<TodoList todos={[]} isLoading={true} error={null} />);
        expect(getByText(/loading/i)).toBeInTheDocument();
    });

    test('renders todos', () => {
        const todos = [
            { _id: '1', text: 'First todo' },
            { _id: '2', text: 'Second todo' }
        ];

        const { getByText } = render(<TodoList todos={todos} isLoading={false} error={null} />);

        expect(getByText('First todo')).toBeInTheDocument();
        expect(getByText('Second todo')).toBeInTheDocument();
    });
});