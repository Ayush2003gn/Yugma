import core.storage.manager as StorageManager

def test_create_page():

    result = StorageManager.create_page(
        "test_page"
    )
    StorageManager.delete_page("test_page")
    

    assert result.success is True