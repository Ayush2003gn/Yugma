import sqlite3
import logging
from core.contracts.operation_result import OperationResult
from core.storage.Sqlite.initialize_database import initialize_database
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)


def get_tasks_id(page_id,path):
    conn = initialize_database(path)
    if conn.success:
        try:
            cursor = conn.data.cursor()
            cursor.execute("SELECT iid, task, created_at, updated_at FROM tasks WHERE page_id = ?;", (page_id,))
            rows = cursor.fetchall()
            tasks = []
            for row in rows:
                tasks.append({
                    "iid": row[0],
                    "task": row[1],
                    "created_at": row[2],
                    "updated_at": row[3]
                })
            return OperationResult(
                success = True,
                data = tasks
            )
        except sqlite3.Error as e:
            logger.error(f"Error getting tasks: {e}")
            return OperationResult(
                success = False,
                error = ErrorData(
                    error_boolean = True,
                    error_message = f"Error getting tasks: {e}",
                    error_code = "error-getting-tasks"
                )
            )
        finally:
            conn.data.close()
    else:
        return OperationResult(
            success= False,
            error = conn.error
            )

def get_tasks_name(page_name,path):
    conn = initialize_database(path)
    if conn.success:
        try:
            cursor = conn.data.cursor()
            cursor.execute("""
                SELECT t.iid, t.task, t.created_at, t.updated_at 
                FROM tasks t
                JOIN pages p ON t.page_id = p.id
                WHERE p.title = ?;""", 
                (page_name,)
            )
            rows = cursor.fetchall()
            tasks = []
            for row in rows:
                tasks.append({
                    "iid": row[0],
                    "task": row[1],
                    "created_at": row[2],
                    "updated_at": row[3]
                })
            return OperationResult(
                success = True,
                data = tasks
            )
        except sqlite3.Error as e:
            logger.error(f"Error getting tasks: {e}")
            return OperationResult(
                success = False,
                error = ErrorData(
                    error_boolean = True,
                    error_message = f"Error getting tasks: {e}",
                    error_code = "error-getting-tasks"
                )
            )
        finally:
            conn.data.close()
    else:
        return OperationResult(
            success= False,
            error = conn.error
            )