import sqlite3
import logging
from core.contracts.operation_result import OperationResult
from core.storage.Sqlite.initialize_database import initialize_database
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def move_task(task_id, new_page_id,path,update_date):
    conn = initialize_database(path)
    if conn.success:
        try:
            cursor = conn.data.cursor()
            cursor.execute("UPDATE tasks SET page_id = ?, updated_at = ? WHERE iid = ?;", (new_page_id, update_date, task_id))
            conn.data.commit()
            if cursor.rowcount > 0:
                return OperationResult(
                    success = True,
                    data = {
                        "iid": task_id,
                        "new_page_id": new_page_id,
                        "updated_at": update_date
                    }
                )
            else:
                return OperationResult(
                    success = False,
                    error = ErrorData(
                        error_boolean = True,
                        error_message = f"Task with id {task_id} not found",
                        error_code = "task-not-found"
                    )
                )
        except sqlite3.Error as e:
            logger.error(f"Error moving task: {e}")
            return OperationResult(
                success = False,
                error = ErrorData(
                    error_boolean = True,
                    error_message = f"Error moving task: {e}",
                    error_code = "error-moving-task"
                )
            )
        finally:
            conn.data.close()