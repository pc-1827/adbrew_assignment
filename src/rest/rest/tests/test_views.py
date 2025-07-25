from django.test import TestCase
from unittest.mock import patch, ANY 
from rest_framework.test import APIClient
from rest_framework import status
from bson.objectid import ObjectId

class TodoListViewTests(TestCase):

    def setUp(self):
        """Set up for the tests."""
        self.client = APIClient()
        self.todos_url = '/todos/'

    @patch('rest.views.list_todos')
    def test_get_todos(self, mock_list_todos):
        """Test getting all todos successfully."""
        # Arrange
        mock_list_todos.return_value = [
            {"_id": str(ObjectId()), "text": "Test todo 1"},
            {"_id": str(ObjectId()), "text": "Test todo 2"}
        ]
        
        # Act
        response = self.client.get(self.todos_url)
        
        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        mock_list_todos.assert_called_once()

    @patch('rest.views.list_todos')
    def test_get_todos_handles_error(self, mock_list_todos):
        """Test error handling when getting todos."""
        # Arrange
        mock_list_todos.side_effect = Exception("Database error")
        
        # Act
        response = self.client.get(self.todos_url)
        
        # Assert
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data["error"], "Failed to fetch todos")

    @patch('rest.views.create_todo')
    def test_create_todo(self, mock_create_todo):
        """Test creating a todo successfully."""
        # Arrange
        todo_id = str(ObjectId())
        mock_create_todo.return_value = {"id": todo_id, "text": "New todo"}
        
        # Act
        response = self.client.post(
            self.todos_url, 
            {"text": "New todo"}, 
            format='json'
        )
        
        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["text"], "New todo")
        self.assertEqual(response.data["id"], todo_id)
        mock_create_todo.assert_called_once_with(ANY, "New todo") 

    def test_create_todo_validates_missing_text(self):
        """Test validation for missing text field."""
        # Act
        response = self.client.post(
            self.todos_url, 
            {}, 
            format='json'
        )
        
        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "Todo text is required")

    @patch('rest.views.create_todo')
    def test_create_todo_handles_validation_error(self, mock_create_todo):
        """Test handling validation errors from the service."""
        # Arrange
        mock_create_todo.side_effect = ValueError("Todo text cannot be empty")
        
        # Act
        response = self.client.post(
            self.todos_url, 
            {"text": ""}, 
            format='json'
        )
        
        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"], "Todo text cannot be empty")

    @patch('rest.views.create_todo')
    def test_create_todo_handles_error(self, mock_create_todo):
        """Test error handling when creating a todo."""
        # Arrange
        mock_create_todo.side_effect = Exception("Database error")
        
        # Act
        response = self.client.post(
            self.todos_url, 
            {"text": "New todo"}, 
            format='json'
        )
        
        # Assert
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data["error"], "Failed to create todo")