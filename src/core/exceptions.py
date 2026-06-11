"""
class exceptions for all ShopBeta exceptions
"""
from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class Xpenseiq(Exception):
    """Base class for all CircleGround exceptions."""
    message: str
    details: Optional[Any] = None


class EntityAlreadyExist(Xpenseiq):
    """Rasied when trying to create an entity that already exists."""
    def __init__(self, message="entity already exist", details=None):
        super().__init__(message=message, details=details)

class EntityNotFound(Xpenseiq):
    """Rasied when an entity is not found in dataase"""
    def __init__(self, message="entity not found", details=None):
        super().__init__(message=message, details=details)

class PermissionDenied(Xpenseiq):
    """Rasied when an unauthorized user is trying to access information"""
    def __init__(self, message="Permission denied", details=None):
        super().__init__(message=message, details=details)

     
class InvalidCredentialsError(Xpenseiq):
    """Raised when credenetials passed are invalid"""
    def __init__(self, message="Invalid Credentials", details=None):
        super().__init__(message=message, details=details)

class InvalidResetTokenError(Xpenseiq):
    def __init__(self, message="Invalid or expired reset token", details=None):
        super().__init__(message=message, details=details)

class DatabaseConnectionError(Xpenseiq):
    """Raised when there's a failure when trying to connect to database"""
    def __init__(self, message="failed to connect to database", details=None):
        super().__init__(message=message, details=details)
