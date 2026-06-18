from core.contracts.operation_result import OperationResult
import uuid

def uuid_generator():
    return OperationResult(
        success = True,
        message = "uuid generated",
        data = str(uuid.uuid4())
    )