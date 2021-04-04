import logging
import traceback

from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from rest_framework.views import exception_handler

from .codes import BAD_REQUEST

logger = logging.getLogger(__name__)


def core_exception_handler(exc, context):
    response = exception_handler(exc, context)
    logger.error(
        "".join(
            traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
        )
    )
    if response:
        errors = []
        for field, value in response.data.items():
            if isinstance(value, list):
                value = value[0]
            errors.append(value)
        response.data = {}
        if hasattr(exc, "code"):
            response.data["code"] = exc.code
        else:
            if response.status_code == HTTP_401_UNAUTHORIZED:
                response.data["code"] = response.status_code
            else:
                response.data["code"] = BAD_REQUEST

        if hasattr(exc, "detail"):
            response.data["message"] = exc.detail

        if len(errors) > 0:
            if isinstance(errors[0], dict):
                for key in errors[0]:
                    response.data["message"] = "".join(errors[0][key]) + ": " + key
            else:
                if response.status_code == HTTP_400_BAD_REQUEST:
                    response.data["message"] = f"{field}: {errors[0]}"
                else:
                    response.data["message"] = errors[0]
    return response


class SolfAPIException(APIException):
    detail = None
    code = None

    def __init__(self, status_code=400, code=BAD_REQUEST, detail="API exception"):
        self.status_code = status_code
        self.code = code
        self.detail = detail
