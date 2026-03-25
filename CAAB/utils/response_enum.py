from enum import Enum

class StatusCode(int, Enum):
    SUCCESS = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    SERVER_ERROR = 500


class ResponseMessage(str, Enum):
    USER_CREATED = "New user created"
    USER_EXISTS = "User already exists"
    USER_NOT_FOUND = "Invalid user"
    ROLE_NOT_FOUND = "No access role assigned"
    ACCESS_DENIED = "Access denied"
    DEPARTMENT_NOT_FOUND = "Department not found"
    USERMENU_NOT_FOUND = "User menu not found"
    SERVER_ERROR = "Internal server error"