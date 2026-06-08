from core.storage.Sqlite.initialize_database import initialize_database
import logging
import sqlite3
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)



def create_page(page_id,title, created_at, updated_at,path):
    conn = initialize_database(path)
    if conn.success:
        try:
            cursor = conn.data.cursor()
            cursor.execute("""
                INSERT INTO pages (id, title, created_at, updated_at)
                VALUES (?, ?, ?, ?);""", 
                (page_id, title, created_at, updated_at)
            )
            conn.data.commit()
            conn.data.close()
            return OperationResult(
                success = True,
                data = {
                    "id": page_id,
                    "title": title,
                    "created_at": created_at,
                    "updated_at": updated_at
                }
            )
        except sqlite3.Error as e:
            logger.error(f"Error creating page: {e}")
            conn.data.close()
            return OperationResult(
                success = False,
                error = ErrorData(
                    error_boolean = True,
                    error_message = f"Error creating page: {e}",
                    error_code = "error-creating-page"
                )
            )
    else:
        return OperationResult(
            success= False,
            error = conn.error
            )