const TodoList = ({ todos, isLoading, error }) => {
    const sortedTodos = [...todos].sort((a, b) => {
        if (!a.created_at || !b.created_at) {
            return a._id > b._id ? -1 : 1;
        }
        return new Date(b.created_at) - new Date(a.created_at);
    });

    const formatDate = (dateString) => {
        if (!dateString) return '';
        const date = new Date(dateString);
        return date.toLocaleString();
    };

    return (
        <div className="todo-list-container">
            <h1>TODOs</h1>
            {isLoading && <p>Loading...</p>}
            {error && <p className="error">{error}</p>}
            {!isLoading && sortedTodos.length === 0 && <p>No todos found. Add one below!</p>}
            <ul>
                {sortedTodos.map((todo) => (
                    <li key={todo._id}>
                        <div className="todo-text">{todo.text}</div>
                        {todo.created_at && (
                            <div className="todo-date">
                                Created: {formatDate(todo.created_at)}
                            </div>
                        )}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TodoList;