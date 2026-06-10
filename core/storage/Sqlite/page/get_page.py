from core.storage.Sqlite.initialize_database import initialize_database
import logging
import sqlite3
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def get_page_id(page_id,path):
    conn = initialize_database(path)
    if conn.success:
        try:
            cursor = conn.data.cursor()
            cursor.execute("""
                SELECT id, title, created_at, updated_at
                FROM pages
                WHERE id = ?;""", 
                (page_id,)
            )
            row = cursor.fetchone()
            if row:
                return OperationResult(
                    success = True,
                    data = {
                        "id": row[0],
                        "title": row[1],
                        "created_at": row[2],
                        "updated_at": row[3]
                    }
                )
            else:
                return OperationResult(
                    success = False,
                    error = ErrorData(
                        error_boolean = True,
                        error_message = f"Page with id {page_id} not found",
                        error_code = "page-not-found"
                    )
                )
        except sqlite3.Error as e:
            logger.error(f"Error getting page: {e}")
            
            return OperationResult(
                success = False,
                error = ErrorData(
                    error_boolean = True,
                    error_message = f"Error getting page: {e}",
                    error_code = "error-getting-page"
                )
            )
        finally:
            conn.data.close()
    else:
        return OperationResult(
            success= False,
            error = conn.error
            )
    
def get_page_name(page_name,path):
    conn = initialize_database(path)
    if conn.success:
        try:
            cursor = conn.data.cursor()
            cursor.execute("""
                SELECT id, title, created_at, updated_at
                FROM pages
                WHERE title = ?;""", 
                (page_name,)
            )
            row = cursor.fetchone()
            if row:
                return OperationResult(
                    success = True,
                    data = {
                        "id": row[0],
                        "title": row[1],
                        "created_at": row[2],
                        "updated_at": row[3]
                    }
                )
            else:
                return OperationResult(
                    success = False,
                    error = ErrorData(
                        error_boolean = True,
                        error_message = f"Page with name {page_name} not found",
                        error_code = "page-not-found"
                    )
                )
        except sqlite3.Error as e:
            logger.error(f"Error getting page: {e}")
            
            return OperationResult(
                success = False,
                error = ErrorData(
                    error_boolean = True,
                    error_message = f"Error getting page: {e}",
                    error_code = "error-getting-page"
                )
            )
        finally:
            conn.data.close()
    else:
        return OperationResult(
            success= False,
            error = conn.error
            )
        