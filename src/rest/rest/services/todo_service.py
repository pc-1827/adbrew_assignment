from typing import Dict, List, Any
from pymongo.collection import Collection
from pymongo.database import Database
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def get_todos_collection(db: Database) -> Collection:
    return db.todos


def list_todos(db: Database) -> List[Dict[str, Any]]:
    try:
        collection = get_todos_collection(db)
        todos = list(collection.find())

        for todo in todos:
            todo['_id'] = str(todo['_id'])
            if 'created_at' in todo and isinstance(todo['created_at'], datetime):
                todo['created_at'] = todo['created_at'].isoformat()
            
        return todos
    except Exception as e:
        logger.error(f"Error fetching todos: {str(e)}")
        raise


def create_todo(db: Database, text: str) -> Dict[str, Any]:
    if not text:
        raise ValueError("Todo text cannot be empty")
        
    try:
        collection = get_todos_collection(db)
        now = datetime.utcnow()
        result = collection.insert_one({
            "text": text,
            "created_at": now
        })
        return {
            "id": str(result.inserted_id), 
            "text": text,
            "created_at": now.isoformat()
        }
    except Exception as e:
        logger.error(f"Error creating todo: {str(e)}")
        raise