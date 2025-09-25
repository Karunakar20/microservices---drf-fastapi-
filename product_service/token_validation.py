from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

JWT_SECRET = "your-drf-secret"  # Use the same as DRF
JWT_ALGORITHM = "HS256"         # Must match DRF

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

bearer_scheme = HTTPBearer()

async def require_jwt(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):
    return decode_jwt(credentials.credentials)
