from core.storage.Sqlite.initialize_database import initialize_database
import logging
import sqlite3
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def delete_task(task_id,path):
    conn = initialize_database(path)
    if conn.success:
        try:
            cursor = conn.data.cursor()
            cursor.execute("""
                DELETE FROM tasks
                WHERE id = ?;""", 
                (task_id,)
            )
            conn.data.commit()
            
            return OperationResult(
                success = True,
                data = {
                    "id": task_id
                }
            )
        except sqlite3.Error as e:
            logger.error(f"Error deleting task: {e}")
            
            return OperationResult(
                success = False,
                error = ErrorData(
                    error_boolean = True,
                    error_message = f"Error deleting task: {e}",
                    error_code = "error-deleting-task"
                )
            )
        finally:
            conn.data.close()
    else:
        return OperationResult(
            success= False,
            error = conn.error
            )