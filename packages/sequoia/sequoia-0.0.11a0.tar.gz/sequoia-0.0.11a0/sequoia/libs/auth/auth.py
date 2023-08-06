import jwt
from dataclasses import dataclass
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime, timedelta
from sequoia.core.config import config

security = HTTPBearer()
secret = config.JWT_SECRET_KEY


def encode_token(user):
    payload = {
        "exp": datetime.utcnow() + timedelta(days=360, minutes=1),
        "iat": datetime.utcnow(),
        "userid": user["id"],
        "role": user["role"],
    }
    return jwt.encode(payload, secret, algorithm=config.JWT_ALGORITHM)


def decode_token(token):
    try:
        try:
            payload = jwt.decode(token, secret, algorithms=[
                config.JWT_ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Login expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@dataclass
class PermissionCheck():
    allow = ['public']

    def __init__(self,
                 auth: HTTPAuthorizationCredentials = Security(security)):

        tokendt = decode_token(auth.credentials)
        if tokendt["role"] in self.allow:
            return None
        else:
            raise HTTPException(status_code=401, detail="Permission Denied")


@dataclass
class Authenticated:
    @classmethod
    def user_id(cls, auth: HTTPAuthorizationCredentials = Security(security)):
        tokendt = decode_token(auth.credentials)
        return tokendt["userid"]


# class AUTH_ME(PermissionCheck):
#     allow = ["admin", "customer"]
