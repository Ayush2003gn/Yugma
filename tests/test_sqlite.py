import core.storage.Sqlite.create_page as create_page
import core.storage.Sqlite.create_task as create_task
import core.storage.Sqlite.get_tasks as get_tasks
import core.storage.Sqlite.list_pages as list_pages
import core.storage.Sqlite.initialize_database as initialize_database
import os
import shutil
from pathlib import Path

def test_sqlite_operations():
    
    # Setup
    test_db_path = Path(os.getenv("APPDATA")) / "Yugma" / "test_data" if os.name == "nt" else Path.home() / ".Yugma" / "test_data"
    if test_db_path.exists():
        shutil.rmtree(test_db_path)
    test_db_path.parent.mkdir(parents=True, exist_ok=True)
    print("Path:", test_db_path)
    print("Exists:", test_db_path.exists())
    print("Parent exists:", test_db_path.parent.exists())
    print("Is dir:", test_db_path.is_dir())
    
    
    # Initialize database
    init_result = initialize_database.initialize_database(test_db_path)
    assert init_result.success is True
    init_result.data.close()
    
    # Create a page
    page_result = create_page.create_page("page1", "Test Page", "2024-01-01T00:00:00Z", "2024-01-01T00:00:00Z", test_db_path)
    assert page_result.success is True
    
    # List pages
    list_result = list_pages.list_pages(test_db_path)
    assert list_result.success is True
    assert len(list_result.data) == 1
    
    # Create a task for the page
    task_result = create_task.create_task("page1", "Test Task", "task1", "2024-01-01T00:00:00Z", "2024-01-01T00:00:00Z", test_db_path)
    assert task_result.success is True
    
    # Get tasks for the page
    get_tasks_result = get_tasks.get_tasks("page1", test_db_path)
    assert get_tasks_result.success, f"Getting tasks failed: {get_tasks_result.error.error_message}"
    assert len(get_tasks_result.data) == 1
    
    # Cleanup
    if os.path.exists(test_db_path):
        os.remove(os.path.join(test_db_path, "database.db"))