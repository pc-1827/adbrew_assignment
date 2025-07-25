from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import logging, os
from pymongo import MongoClient

from .services.todo_service import list_todos, create_todo

# Configure logger
logger = logging.getLogger(__name__)

# Create MongoDB connection
mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db_client = MongoClient(mongo_uri)
db = db_client['test_db']

class TodoListView(APIView):

    def get(self, request: Request) -> Response:
        try:
            todos = list_todos(db)
            return Response(todos, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error in TodoListView.get: {str(e)}")
            return Response(
                {"error": "Failed to fetch todos"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
    def post(self, request: Request) -> Response:
        try:
            todo_data = request.data
            
            if not todo_data or 'text' not in todo_data:
                return Response(
                    {"error": "Todo text is required"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            new_todo = create_todo(db, todo_data['text'])
            
            return Response(new_todo, status=status.HTTP_201_CREATED)
        except ValueError as e:
            logger.warning(f"Validation error: {str(e)}")
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Error in TodoListView.post: {str(e)}")
            return Response(
                {"error": "Failed to create todo"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

