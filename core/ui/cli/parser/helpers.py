from core.contracts.validation_result import ValidationResult, DateValidationResult
from core.contracts.error_data import ErrorData
from core.contracts.command_result import CommandResult
from core.contracts.date_data import DateData
from core.contracts.flags_data import FlagsData

def safe_get_value(argument: list, flag: str) -> ValidationResult:

    if flag not in argument:
        return ValidationResult(
            value=None,
            is_valid=False,
            used_default=False,
            error=ErrorData(
                error_boolean=True,
                error_message=f"missing-{flag.lstrip('-')}",
                error_code=f"error-missing-{flag.lstrip('-')}"
            )
        )
    
    index = argument.index(flag)

    if index + 1 >= len(argument):
        return ValidationResult(
            value=None, 
            is_valid=False, 
            used_default=False, 
            error=ErrorData(
                error_boolean=True,
                error_message="missing-value",
                error_code="error-missing-value"
            )
        )

    value = argument[index + 1]

    if value.startswith("-"):
        return ValidationResult(
            value=None, 
            is_valid=False, 
            used_default=False, 
            error=ErrorData(
                error_boolean=True,
                error_message="missing-value",
                error_code="error-missing-value"
            )
        )

    return ValidationResult(value=value, is_valid=True, used_default=False)

def safe_get_date(argument: list[str], date_type: str) -> DateValidationResult:

    if date_type == "--year":
        if date_type in argument:
            try:
                year=int(argument[argument.index(date_type) + 1])
            except (ValueError, IndexError):
                return DateValidationResult(
                    is_valid=False,
                    error=ErrorData(
                        error_boolean=True,
                        error_message=f"invalid-{date_type.lstrip('-')}",
                        error_code=f"error-invalid-{date_type.lstrip('-')}"
                    )
                )
            return DateValidationResult(
                is_valid=True,
                year=year
            )

    if date_type == "--month":
        if date_type in argument:
            try:
                month=int(argument[argument.index(date_type) + 1])
                year=int(argument[argument.index(date_type) + 2])
            except (ValueError, IndexError):
                return DateValidationResult(
                    is_valid=False,
                    error=ErrorData(
                        error_boolean=True,
                        error_message=f"invalid-{date_type.lstrip('-')}",
                        error_code=f"error-invalid-{date_type.lstrip('-')}"
                    )
                )
            return DateValidationResult(
                is_valid=True,
                year=year,
                month=month
            )

    if date_type == "--week":
        if date_type in argument:
            try:
                week=int(argument[argument.index(date_type) + 1])
                year=int(argument[argument.index(date_type) + 2])
            except (ValueError, IndexError):
                return DateValidationResult(
                    is_valid=False,
                    error=ErrorData(
                        error_boolean=True,
                        error_message=f"invalid-{date_type.lstrip('-')}",
                        error_code=f"error-invalid-{date_type.lstrip('-')}"
                    )
                )
            return DateValidationResult(
                is_valid=True,
                week=week,
                year=year
            )

    if date_type == "--day":
        if date_type in argument:
            try:
                day=int(argument[argument.index(date_type) + 1])
                month=int(argument[argument.index(date_type) + 2])
                year=int(argument[argument.index(date_type) + 3])
            except (ValueError, IndexError):
                return DateValidationResult(
                    is_valid=False,
                    error=ErrorData(
                        error_boolean=True,
                        error_message=f"invalid-{date_type.lstrip('-')}",
                        error_code=f"error-invalid-{date_type.lstrip('-')}"
                    )
                )
            return DateValidationResult(
                is_valid=True,
                day=day,
                month=month,
                year=year
            )

    return DateValidationResult(
        is_valid=False,
        error=ErrorData(
            error_boolean=True,
            error_message=f"missing-{date_type.lstrip('-')}",
            error_code=f"error-missing-{date_type.lstrip('-')}"
        )
    )


def validate_priority(priority) -> ValidationResult:

    if priority is None:
        return ValidationResult(value="medium", is_valid=True, used_default=True)

    priority = priority.lower()

    if priority not in ["low", "medium", "high"]:
        return ValidationResult(value="medium", is_valid=False, used_default=True)

    return ValidationResult(value=priority, is_valid=True, used_default=False)

def validate_status(status) -> ValidationResult:

    if status is None:
        return ValidationResult(value=False, is_valid=True, used_default=True)

    if status in ["--md", "--mark-done"]:
        return ValidationResult(value=True, is_valid=True, used_default=False)

    if status in ["--mu", "--mark-undone"]:
        return ValidationResult(value=False, is_valid=True, used_default=False)

    return ValidationResult(value=False, is_valid=False, used_default=True)

def validate_default(default) -> ValidationResult:

    if default is None:
        return ValidationResult(value=False, is_valid=True, used_default=True)

    if default in ["--d", "--default"]:
        return ValidationResult(value=True, is_valid=True, used_default=False)

    return ValidationResult(value=False, is_valid=False, used_default=True)
