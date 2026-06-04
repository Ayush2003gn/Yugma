import core.storage.path_manager as pathmanager
import core.storage.json_storage as jsonstorage
from core.contracts.operation_result import operationresult
from core.contracts.error_data import errordata
import logging
logger = logging.getLogger(__name__)

def load_page():
    data_page = {}
    try:
        for file in pathmanager.list_page_data_files():
            if jsonstorage.is_valid_json(file):
                data = jsonstorage.load_json(file)
            else:
                data = []
            page_name = pathmanager.get_page_name(file)
            data_page[page_name] = data
        return operationresult(
            success = True,
            data = data_page
        )
    except Exception as e:
        return operationresult(
            success = False,
            error = errordata(
                error_boolean = True,
                error_message = str(e),
                error_code = "error-reading-data"
            )
        )

def save_page(page_name,data):
    try:
        logger.info(f"Saving page {page_name}")

        jsonstorage.save_json(pathmanager.get_page_file(page_name),data)
        return operationresult(
            success = True
        )
    except Exception as e:
        return operationresult(
            success = False,
            error = errordata(
                error_boolean = True,
                error_message = str(e),
                error_code = "error-saving-data"
            )
        )

def delete_page(page_name):
    try:
        logger.info(f"Deleting page {page_name}")
        pathmanager.delete_file(pathmanager.get_page_file(page_name))
        return operationresult(
            success = True
        )
    except Exception as e:
        return operationresult(
            success = False,
            error = errordata(
                error_boolean = True,
                error_message = str(e),
                error_code = "error-deleting-data"
            )
        )

def list_pages():
    try:
        pages = []

        for file in pathmanager.list_page_data_files():
            pages.append(pathmanager.get_page_name(file))

        return operationresult(
            success=True,
            data=pages
        )
    except Exception as e:
        return operationresult(
            success = False,
            error = errordata(
                error_boolean = True,
                error_message = str(e),
                error_code = "error-listing-data"
            )
        )

def create_page(page_name):
    try:
        logger.info(f"Creating page {page_name}")
        pathmanager.create_file(pathmanager.get_page_file(page_name))
        return operationresult(
            success = True
        )
    except Exception as e:
        return operationresult(
            success = False,
            error = errordata(
                error_boolean = True,
                error_message = str(e),
                error_code = "error-creating-data"
            )
        )


def manifest_files_load_data():
    try:
        file = pathmanager.manifest_file()
        data = jsonstorage.load_json(file)
        return operationresult(
            success = True,
            data = data
        )
    except Exception as e:
        return operationresult(
            success = False,
            error = errordata(
                error_boolean = True,
                error_message = str(e),
                error_code = "error-reading-data"
            )
        )
        
def manifest_files_save_data(data_list):
    if type(data_list) is not list:
        logger.error("Data must be list")
        return operationresult(
            success = False,
            error = errordata(
                error_boolean = True,
                error_message = "Data must be list",
                error_code = "error-reading-data"
            )
        )
    try:
        data = {"pages" : data_list}
        file = pathmanager.manifest_file()
        jsonstorage.save_json(file,data)
        return operationresult(
            success = True
        )
    except Exception as e:
        return operationresult(
            success = False,
            error = errordata(
                error_boolean = True,
                error_message = str(e),
                error_code = "error-saving-data"
            )
        )