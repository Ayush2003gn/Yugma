import tempfile
import os
from core import storage


def test_ensure_datafile():
    with tempfile.TemporaryDirectory() as temp_dir:
        path = os.path.join(temp_dir, "test.json")

        storage.ensure_datafile(path)

        assert os.path.exists(path)


def test_export_and_import_json():
    with tempfile.TemporaryDirectory() as temp_dir:
        path = os.path.join(temp_dir, "test.json")

        data = [
            {
                "Task": "Study",
                "Id": "1",
                "Done": False,
                "Date Created": "2026-01-01T00:00:00",
                "Date Modified": "2026-01-01T00:00:00",
                "Priority": "High"
            }
        ]

        storage.exporting_data(path, data)

        loaded = storage.json_to_py(path)

        assert loaded == data