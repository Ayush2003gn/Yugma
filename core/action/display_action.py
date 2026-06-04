import logging
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def display_action(token_return,task_app):
    if token_return is None:

        logger.error("token_return was None")

        return OperationResult(
            success=False,
            error=ErrorData(
                error_boolean=True,
                error_message="something went wrong",
                error_code="error-no-return-value-from-token"
            )
        )

    if token_return.action == "display-all":

        return task_app.display_all(token_return.page_name)
    
    elif token_return.action == "display-analysis":

        return task_app.display_analysis(token_return.page_name)
    
    elif token_return.action == "display-by-year":

        if token_return.date.year is None or token_return.date.year.isdigit() is False:
            return OperationResult(
                success=False,
                error=ErrorData(
                    error_boolean=True,
                    error_message="No year provided",
                    error_code="error-no-return-value-from-token"
                )
            )
        
        return task_app.display_by_year(token_return.date.year,token_return.page_name)
    
    elif token_return.action == "display-by-month":

        if token_return.date.month is None or token_return.date.month.isdigit() is False:
            return OperationResult(
                success=False,
                error=ErrorData(
                    error_boolean=True,
                    error_message="No month provided",
                    error_code="error-no-return-value-from-token"
                )
            )
        
        if token_return.date.year is None or token_return.date.year.isdigit() is False:
            return OperationResult(
                success=False,
                error=ErrorData(
                    error_boolean=True,
                    error_message="No year provided",
                    error_code="error-no-return-value-from-token"
                )
            )
        
        return task_app.display_by_month(token_return.date.month,token_return.page_name)
    
    elif token_return.action == "display-by-day":

        if token_return.date.day is None or token_return.date.day.isdigit() is False:
            return OperationResult(
                success=False,
                error=ErrorData(
                    error_boolean=True,
                    error_message="No date provided",
                    error_code="error-no-return-value-from-token"
                )
            )
        if token_return.date.month is None or token_return.date.month.isdigit() is False:
            return OperationResult(
                success=False,
                error=ErrorData(
                    error_boolean=True,
                    error_message="No month provided",
                    error_code="error-no-return-value-from-token"
                )
            )
        
        if token_return.date.year is None or token_return.date.year.isdigit() is False:
            return OperationResult(
                success=False,
                error=ErrorData(
                    error_boolean=True,
                    error_message="No year provided",
                    error_code="error-no-return-value-from-token"
                )
            )
        return task_app.display_by_day(token_return.date.date,token_return.page_name)
    
    elif token_return.action == "display-by-week":

        if token_return.date.week is None or token_return.date.week.isdigit() is False:
            return OperationResult(
                success=False,
                error=ErrorData(
                    error_boolean=True,
                    error_message="No week provided",
                    error_code="error-no-return-value-from-token"
                )
            )
        return task_app.display_by_week(token_return.date.weekday,token_return.page_name)
    
    elif token_return.action == "display-done":

        return task_app.display_done(token_return.page_name)
    
    elif token_return.action == "display-pending":

        return task_app.display_pending(token_return.page_name)
    
    elif token_return.action == None:

        return OperationResult(
            success=False,
            error=ErrorData(
                error_boolean=True,
                error_message="No action provided",
                error_code="error-no-return-value-from-token"
            )
    )   

def cmd_none():
    return OperationResult(
        success=False,
        error=ErrorData(
            error_boolean=True, 
            error_message="No command provided by user", 
            error_code="error-no-command"
        )
) 

def cmd_invalid(token_return):
    return OperationResult(
        success=False,
        error=token_return.error
    )

def cmd_exit():
    return OperationResult(
        success=True,
        message="exit",
        error=ErrorData(
            error_boolean=False,
            error_message="exit",
            error_code="exit"
        )
    )