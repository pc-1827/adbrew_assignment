import unittest
from unittest.mock import Mock, ANY 
from bson.objectid import ObjectId
from rest.services.todo_service import list_todos, create_todo

class TodoServiceTests(unittest.TestCase):

    def test_list_todos(self):
        """Test listing todos successfully."""
        # Arrange
        mock_db = Mock()
        mock_collection = Mock()
        mock_db.todos = mock_collection
        
        # Mock data with ObjectId
        todo_id = ObjectId()
        mock_todos = [{"_id": todo_id, "text": "Test todo"}]
        mock_collection.find.return_value = mock_todos
        
        # Act
        result = list_todos(mock_db)
        
        # Assert
        mock_collection.find.assert_called_once()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["text"], "Test todo")
        self.assertEqual(result[0]["_id"], str(todo_id))  

    def test_list_todos_handles_error(self):
        """Test list_todos raises exceptions properly."""
        # Arrange
        mock_db = Mock()
        mock_collection = Mock()
        mock_db.todos = mock_collection
        mock_collection.find.side_effect = Exception("Database error")
        
        # Act & Assert
        with self.assertRaises(Exception):
            list_todos(mock_db)

    def test_create_todo(self):
        """Test creating a todo successfully."""
        # Arrange
        mock_db = Mock()
        mock_collection = Mock()
        mock_db.todos = mock_collection
        
        # Mock the insert_one result
        todo_id = ObjectId()
        mock_result = Mock()
        mock_result.inserted_id = todo_id
        mock_collection.insert_one.return_value = mock_result
        
        # Act
        result = create_todo(mock_db, "New todo")
        
        # Assert
        mock_collection.insert_one.assert_called_once_with({
            "text": "New todo", 
            "created_at": ANY
        })
        self.assertEqual(result["text"], "New todo")
        self.assertEqual(result["id"], str(todo_id))
        self.assertIn("created_at", result)

    def test_create_todo_validates_empty_text(self):
        """Test create_todo validates empty text."""
        # Arrange
        mock_db = Mock()
        
        # Act & Assert
        with self.assertRaises(ValueError):
            create_todo(mock_db, "")
        
        with self.assertRaises(ValueError):
            create_todo(mock_db, None)

    def test_create_todo_handles_error(self):
        """Test create_todo raises exceptions properly."""
        # Arrange
        mock_db = Mock()
        mock_collection = Mock()
        mock_db.todos = mock_collection
        mock_collection.insert_one.side_effect = Exception("Database error")
        
        # Act & Assert
        with self.assertRaises(Exception):
            create_todo(mock_db, "New todo")