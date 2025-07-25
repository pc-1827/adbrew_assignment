# Todo App with React, Django, and MongoDB

This is a production-ready Todo application built with a modern microservices architecture using React, Django, and MongoDB. The application allows users to create and view todos through a clean, responsive interface.

## Project Architecture

The application is structured with three Docker containers:

### 1. Frontend (React)
- A modern React application built with hooks
- Runs on http://localhost:3000
- Located in app directory
- Features a form for creating new todos and a list view of all todos

### 2. Backend (Django REST API)
- Django REST API with a service-oriented architecture
- Runs on http://localhost:8000
- Located in rest directory
- Provides endpoints for creating and listing todos

### 3. Database (MongoDB)
- Document-based NoSQL database
- Runs on port 27017
- Data is persisted in db directory

### Communication Flow
- React frontend makes HTTP requests to the Django backend
- Django backend interacts with MongoDB for data persistence
- Frontend displays data fetched from the backend

## Technologies Used

- **Frontend**: React 17, React Hooks, Fetch API
- **Backend**: Django 3.0.5, Django REST Framework
- **Database**: MongoDB 4.4
- **Infrastructure**: Docker, docker-compose
- **Testing**: Jest, Django Test Framework

## Setup Instructions

### Prerequisites
- Docker and docker-compose installed on your machine
- Git for cloning the repository

### Steps to Run the Application

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Set the environment variable for the code path
   ```bash
   export ADBREW_CODEBASE_PATH="$(pwd)/src"
   ```

3. Build the Docker containers
   ```bash
   docker-compose build
   ```
   This will take some time as it builds all three containers.

4. Start the containers
   ```bash
   docker-compose up -d
   ```

5. Verify all containers are running
   ```bash
   docker ps
   ```
   You should see three containers running: `app`, `api`, and `mongo`.

6. Access the application
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/todos

### Environment Variables

The application uses the following environment variables:
- `ADBREW_CODEBASE_PATH`: Path to the source code directory
- `REACT_APP_API_URL`: URL of the backend API (default: http://localhost:8000)

## Project Structure

```
src/
├── app/                   # React frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── hooks/         # Custom React hooks
│   │   └── services/      # API service layer
├── rest/                  # Django backend
│   ├── rest/
│   │   ├── services/      # Business logic layer
│   │   ├── tests/         # Backend tests
│   │   └── views.py       # API endpoints
└── db/                    # MongoDB data directory
```

## API Documentation

### Endpoints

#### GET /todos/
Returns a list of all todos sorted by creation date (newest first).

**Response Example**:
```json
[
  {
    "_id": "60f1a7b3e6b3d3b3e8f1b3e7",
    "text": "Build a Todo App",
    "created_at": "2023-07-25T14:32:45.123Z"
  },
  {
    "_id": "60f1a7b3e6b3d3b3e8f1b3e6",
    "text": "Learn Docker",
    "created_at": "2023-07-24T09:15:22.567Z"
  }
]
```

#### POST /todos/
Creates a new todo with the current timestamp.

**Request Body**:
```json
{
  "text": "New Todo Item"
}
```

**Response Example**:
```json
{
  "id": "60f1a7b3e6b3d3b3e8f1b3e8",
  "text": "New Todo Item",
  "created_at": "2023-07-25T15:42:18.943Z"
}
```

The `created_at` field contains an ISO-formatted timestamp of when the todo was created. The frontend automatically displays todos in reverse chronological order, with the most recently created items appearing at the top of the list.

## Docker Commands Reference

### Container Management
- View container logs: `docker logs -f --tail=100 {container_name}`
- Enter a container: `docker exec -it {container_name} bash`
- Stop all containers: `docker-compose down`
- Restart a container: `docker restart {container_name}`

### Running Tests
- Frontend tests: `docker exec -it app bash -c "cd /src/app && yarn test"`
- Backend tests: `docker exec -it api bash -c "cd /src/rest && python manage.py test rest.tests"`

## Development Notes

### Code Quality Features
- **Frontend**:
  - Custom hooks for data fetching and state management
  - Component separation for better maintainability
  - Error handling and loading states
  - Modern React patterns with hooks

- **Backend**:
  - Service layer pattern for business logic
  - Dependency injection for better testability
  - Type hints for better code documentation
  - Comprehensive error handling