import { useState } from 'react';

/**
 * Form for creating a new todo
 */
const TodoForm = ({ onSubmit, isLoading }) => {
    const [text, setText] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const success = await onSubmit(text);
        if (success) {
            setText(''); // Clear input on success
        }
    };

    return (
        <div className="todo-form-container">
            <h1>Create a ToDo</h1>
            <form onSubmit={handleSubmit}>
                <div className="form-row">
                    <div className="input-group">
                        <label htmlFor="todo">ToDo: </label>
                        <input
                            type="text"
                            id="todo"
                            value={text}
                            onChange={(e) => setText(e.target.value)}
                            disabled={isLoading}
                            placeholder="Enter your todo..."
                        />
                    </div>
                    <button type="submit" disabled={isLoading} className="add-btn">
                        {isLoading ? 'Adding...' : 'Add ToDo!'}
                    </button>
                </div>
            </form>
        </div>
    );
};

export default TodoForm;