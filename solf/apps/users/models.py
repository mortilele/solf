from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class JWTUser(models.Model):
    class Meta:
        abstract = True

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        import jwt
        from solf.apps.common.utils.constants import JWTAlgorithm
        token = jwt.encode(
            {
                'id': self.pk,
            },
            settings.TOKEN_SECRET_KEY,
            algorithm=JWTAlgorithm.HS256.value
        )
        return token


class User(AbstractUser, JWTUser):
    pass
