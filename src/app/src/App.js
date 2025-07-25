import './App.css';
import TodoList from './components/TodoList';
import TodoForm from './components/TodoForm';
import { useTodos } from './hooks/useTodos';

export function App() {
  const { todos, isLoading, error, addTodo, fetchTodos, clearError } = useTodos();

  return (
    <div className="App">
      <div className="container">
        <TodoList
          todos={todos}
          isLoading={isLoading}
          error={error}
        />
        {error && (
          <div className="retry-container">
            <button onClick={() => { clearError(); fetchTodos(); }} className="retry-btn">
              Retry
            </button>
          </div>
        )}
        <TodoForm
          onSubmit={addTodo}
          isLoading={isLoading}
        />
      </div>
    </div>
  );
}

export default App;
