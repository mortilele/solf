from enum import Enum


class JWTAlgorithm(Enum):
    HS256 = "HS256"
    RS256 = "RS256"

    @staticmethod
    def list():
        return list(map(lambda a: a.value, JWTAlgorithm))
