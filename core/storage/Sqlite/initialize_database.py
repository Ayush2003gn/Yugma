import sqlite3
import logging
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)
import os

def initialize_database(path):

    try:
        os.makedirs(path, exist_ok=True)
        
        db_path = os.path.join(path, "database.db")
        conn = sqlite3.connect(db_path)
        
    except sqlite3.Error as e:
        logger.error(f"Error connecting to database: {e}")
        return OperationResult(
            success = False,
            error = ErrorData(
                error_boolean = True,
                error_message = f"Error connecting to database: {e}",
                error_code = "error-connecting-database"
            )
        )

    conn.execute("""
    CREATE TABLE IF NOT EXISTS pages(
        id TEXT PRIMARY KEY,
        title TEXT UNIQUE NOT NULL,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        iid TEXT PRIMARY KEY,
        page_id TEXT NOT NULL,
        task TEXT NOT NULL,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL,
        priority TEXT NOT NULL
        status INTEGER NOT NULL
        FOREIGN KEY(page_id) REFERENCES pages(id)
    )
    """)

    conn.commit()
    return OperationResult(
        success = True,
        data = conn
    )