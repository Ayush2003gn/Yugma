from core.models.tag import Tag
from core.contracts.error_data import ErrorData
from core.contracts.operation_result import OperationResult
class TagManager:
    def __init__(self):
        self.tags = []

    def get_tag(self,tag):
        for tag in self.tags:
            if tag.tag_id == tag:
                return OperationResult(
                    success = True,
                    data = tag
                )           
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Tag not found",
                error_code="error-tag-not-found"
            )
        )
    def get_tag_id(self,tag):
        for tag in self.tags:
            if tag.tag == tag:
                return tag.tag_id
        return None
    
    def add_tag(self,tag):
        if self.gettag(tag.tag_id).success:
            return OperationResult(
                success = False,
                data = None,
                error=ErrorData(
                    error_boolean=True,
                    error_message=f"Tag already exists",
                    error_code="error-tag-already-exists"
                )
            )
        self.tags.append(tag)
        return OperationResult(
            success = True,
            data = tag
        )

    def remove_tag(self,tag_id):
        for tag in self.tags:
            if tag.tag_id == tag_id:
                self.tags.remove(tag)
                return OperationResult(
                    success = True,
                    data = tag
                )
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Tag not found",
                error_code="error-tag-not-found"
            )
        )
    
    def update_color(self,tag_id,color):
        for tag in self.tags:
            if tag.tag_id == tag_id:
                tag.update_color(color)
                return OperationResult(
                    success = True,
                    data = tag
                )
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Tag not found",
                error_code="error-tag-not-found"
            )
        )
    
    def update_description(self,tag_id,description):
        for tag in self.tags:
            if tag.tag_id == tag_id:
                tag.update_description(description)
                return OperationResult(
                    success = True,
                    data = tag
                )
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Tag not found",
                error_code="error-tag-not-found"
            )
        )
    