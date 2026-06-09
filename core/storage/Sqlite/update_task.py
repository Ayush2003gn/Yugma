from core.storage.Sqlite.initialize_database import initialize_database
import logging
import sqlite3
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def update_task(task_id, title, updated_at,path):
    conn = initialize_database(path)
    if conn.success:
        try:
            cursor = conn.data.cursor()
            cursor.execute("""
                UPDATE tasks
                SET title = ?, updated_at = ?
                WHERE id = ?;""", 
                (title, updated_at, task_id)
            )
            conn.data.commit()
            
            return OperationResult(
                success = True,
                data = {
                    "id": task_id,
                    "title": title,
                    "updated_at": updated_at
                }
            )
        except sqlite3.Error as e:
            logger.error(f"Error updating task: {e}")
            
            return OperationResult(
                success = False,
                error = ErrorData(
                    error_boolean = True,
                    error_message = f"Error updating task: {e}",
                    error_code = "error-updating-task"
                )
            )
        finally:
            conn.data.close()
    else:
        return OperationResult(
            success= False,
            error = conn.error
            )