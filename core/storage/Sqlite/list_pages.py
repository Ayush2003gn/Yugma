import sqlite3
import logging
from core.storage.Sqlite.initialize_database import initialize_database
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)



def list_pages(path):
    conn = initialize_database(path)
    if conn.success:
        try:
            cursor = conn.data.cursor()
            cursor.execute("""
                SELECT id, title, created_at, updated_at 
                FROM pages;"""
            )
            rows = cursor.fetchall()
            pages = []
            for row in rows:
                pages.append({
                    "id": row[0],
                    "title": row[1],
                    "created_at": row[2],
                    "updated_at": row[3]
                })
            
            return OperationResult(
                success = True,
                data = pages
            )
        except sqlite3.Error as e:
            logger.error(f"Error listing pages: {e}")
            
            return OperationResult(
                success = False,
                error = ErrorData(
                    error_boolean = True,
                    error_message = f"Error listing pages: {e}",
                    error_code = "error-listing-pages"
                )
            )
        finally:
            conn.data.close()
    else:
        return OperationResult(
            success= False,
            error = conn.error
            )