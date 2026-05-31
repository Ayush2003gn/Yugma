import logging
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def page_action(token_return,task_app):
    if not token_return:
        logger.error("token_return was None")
        return OperationResult(
            success=False,
            error=ErrorData(
                error_boolean=True,
                error_message="something went wrong",
                error_code="error-no-return-value-from-token"
            )
        )
    if token_return.action == "add":
        addpage = task_app.add_page(token_return.page_name)
        if addpage.success is False:
            logger.warning(addpage.message)
            return addpage
        error_message = ""
        error_code = ""
        if token_return.flags.default is True:
            set_default = task_app.set_default(token_return.page_name)
            if set_default.success is False:
                logger.warning(set_default.message)
                error_message += f"default command failed: {set_default.error.error_message}"
                error_code += f"default-code-error:{set_default.error.error_code}"
        if error_message != "":
            error=ErrorData(
                error_boolean=True,
                error_message=error_message,
                error_code=error_code
                )
        else:
            error=ErrorData(
                error_boolean=False,
                error_message=None,
                error_code=None
                )

        return OperationResult(
            success=True,
            data=addpage.data,
            error=error
            )
    elif token_return.action == "remove":
        removepage = task_app.remove_page(token_return.page_name)
        if removepage.success is False:
            logger.warning(removepage.message)
            return removepage
        return OperationResult(
            success=True,
            message=f"Category : {token_return.page_name} is removed",
            error=ErrorData(
                error_boolean=False,
                error_message=None,
                error_code=None
                )
            )
    elif token_return.action == "set-default":
        set_default = task_app.set_default(token_return.page_name)
        if set_default.success is False:
            logger.warning(set_default.message)
            return set_default
        return OperationResult(
            success=True,
            message=f"Category : {token_return.page_name} is set as default",
            error=ErrorData(
                error_boolean=False,
                error_message=None,
                error_code=None
                )
            )
    elif token_return.action == None:
        return OperationResult(
            success=False,
            error=ErrorData(
                error_boolean=True,
                error_message=token_return.error.error_message,
                error_code=token_return.error.error_code
            )
        )