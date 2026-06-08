import sqlite3
import logging
from core.storage.Sqlite.initialize_database import initialize_database
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)


def create_task(page_id, task,iid,created_at,updated_at,path,):
    conn = initialize_database(path)
    if conn.success:
        try:
            cursor = conn.data.cursor()
            cursor.execute("INSERT INTO tasks (iid, page_id, task, created_at, updated_at) VALUES (?, ?, ?, ?, ?);", (iid, page_id, task, created_at, updated_at))
            conn.data.commit()
            conn.data.close()
            return OperationResult(
                success = True,
                data = {
                    "iid": iid,
                    "page_id": page_id,
                    "task": task,
                    "created_at": created_at,
                    "updated_at": updated_at
                }
            )
        except sqlite3.Error as e:
            conn.data.close()
            logger.error(f"Error creating task: {e}")
            return OperationResult(
                success = False,
                error = ErrorData(
                    error_boolean = True,
                    error_message = f"Error creating task: {e}",
                    error_code = "error-creating-task"
                )
            )
       
    else:
        return OperationResult(
            success= False,
            error = conn.error
            )