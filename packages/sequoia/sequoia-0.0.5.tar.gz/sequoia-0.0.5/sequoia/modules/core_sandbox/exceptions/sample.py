from http import HTTPStatus
from sequoia.core.exceptions.base import CustomException


class SampleError(CustomException):
    code = HTTPStatus.BAD_GATEWAY
    error_code = HTTPStatus.BAD_GATEWAY
    message = 'Sample ERRRRR Boss'
