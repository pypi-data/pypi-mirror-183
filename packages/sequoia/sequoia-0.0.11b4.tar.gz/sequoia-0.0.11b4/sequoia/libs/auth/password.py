from passlib.context import CryptContext
from sequoia.core.exceptions import ForbiddenException
from .auth import encode_token


class Password:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_token(self, plain_password, data_user: dict):
        n = self.pwd_context.verify(plain_password, data_user["password"])
        if n:
            s = encode_token(data_user)
            return s
        else:
            raise ForbiddenException
