import jwt
from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from drf_spectacular.authentication import OpenApiAuthenticationExtension

from . import codes, messages
from .constants import JWTAlgorithm


class JWTAuthentication(BaseAuthentication):
    """
    An authentication plugin that authenticates requests through a JSON web
    token provided in a request header.
    """

    def get_header(self, request):
        """
        Extracts the header containing the JSON web token from the given
        request.
        """
        header = request.META.get("HTTP_AUTHORIZATION")
        return header

    def get_raw_token(self, header):
        """
        Extracts an unvalidated JSON web token from the given "Authorization"
        header value.
        """
        from .exceptions import SolfAPIException
        prefix = header.split(" ")[0]
        if prefix != "Bearer":
            raise SolfAPIException(
                code=codes.AUTHENTICATION_ERROR,
                detail=messages.TOKEN_PREFIX_INVALID,
            )
        access_token = header.split(" ")[1]
        return access_token

    def get_payload(self, raw_token):
        """
        Decodes token to extract user payload.
        """
        payload = jwt.decode(
            raw_token,
            settings.TOKEN_SECRET_KEY,
            algorithms=JWTAlgorithm.list(),
        )
        return payload

    def get_user(self, payload):
        """
        Attempts to find and return a user using the given token.
        """
        from ...users.models import User
        user = User.objects.get(id=payload['id'])
        return user

    def authenticate(self, request):
        from .exceptions import SolfAPIException
        header = self.get_header(request)

        if not header:
            return None
        try:
            # header = 'Bearer xxxxxxxxxxxxxxxxxxxxxxxx'
            raw_token = self.get_raw_token(header)
            payload = self.get_payload(raw_token)
        except jwt.ExpiredSignatureError:
            raise SolfAPIException(
                code=codes.AUTHENTICATION_ERROR,
                detail=messages.TOKEN_EXPIRED
            )
        except IndexError:
            raise SolfAPIException(
                code=codes.AUTHENTICATION_ERROR,
                detail=messages.TOKEN_PREFIX_MISSING
            )
        except (jwt.InvalidSignatureError, jwt.exceptions.DecodeError):
            raise SolfAPIException(
                code=codes.AUTHENTICATION_ERROR,
                detail=messages.TOKEN_INVALID
            )

        user = self.get_user(payload)

        return user, raw_token


class JWTScheme(OpenApiAuthenticationExtension):
    target_class = "solf.apps.common.utils.authentication.JWTAuthentication"  # full import path OR class ref
    name = "JWTAuthentication"  # custom name for your auth scheme

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Value should be formatted: `<key>`. Without prefix",
        }
