from core.models.tag import Tag
from core.contracts.error_data import ErrorData
from core.contracts.operation_result import OperationResult
import logging
logger = logging.getLogger(__name__)
class TagManager:
    def __init__(self):
        self.tags = []

    def get_tag(self,tag):
        for tag in self.tags:
            if tag.tag == tag:
                logger.debug(f"Tag found: {tag.tag}")
                return OperationResult(
                    success = True,
                    data = tag
                )
        logger.debug(f"Tag not found: {tag}")           
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
                logger.debug(f"Tag found: {tag.tag}")
                return OperationResult(
                    success = True,
                    data = tag.tag_id
                )
        logger.debug(f"Tag not found: {tag}")
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Tag not found",
                error_code="error-tag-not-found"
            )
        )
    
    def add_tag(self,tag):
        if self.get_tag(tag.tag_id).success:
            logger.debug(f"Tag already exists: {tag.tag}")
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
        logger.debug(f"Tag added: {tag.tag}")
        return OperationResult(
            success = True,
            data = tag
        )

    def remove_tag(self,tag_id):
        for tag in self.tags:
            if tag.tag_id == tag_id:
                logger.debug(f"Tag removed: {tag.tag}")
                self.tags.remove(tag)
                return OperationResult(
                    success = True,
                    data = tag
                )
        logger.debug(f"Tag not found: {tag_id}")
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
                logger.debug(f"Tag color updated: {tag.tag} to {color}")
                tag.update_color(color)
                return OperationResult(
                    success = True,
                    data = tag
                )
        logger.debug(f"Tag not found: {tag_id}")
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
                logger.debug(f"Tag description updated: {tag.tag} to {description}")
                tag.update_description(description)
                return OperationResult(
                    success = True,
                    data = tag
                )
        logger.debug(f"Tag not found: {tag_id}")
        return OperationResult(
            success = False,
            data = None,
            error=ErrorData(
                error_boolean=True,
                error_message=f"Tag not found",
                error_code="error-tag-not-found"
            )
        )
    