from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from app.core.constants import TOKEN_TYPE

# Password hashing configuration
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)

def hash_password(password: str) -> str:
    """
    Hash a plain-text password before storing it in the database.

    Args:
        password: The user's plain-text password.

    Returns:
        A securely hashed password.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain-text password against a hashed password.

    Args:
        plain_password: The plain-text password to verify.
        hashed_password: The hashed password to verify against.

    Returns:
        True if the password matches, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    subject: str,
    expires_delta: timedelta | None = None,
    additional_claims: dict[str, Any] | None = None,
) -> str:
    """
    Create a signed JWT access token.

    Args:
        subject: The unique identifier of the user (usually the user ID).
        expires_delta: Optional custom expiration time.
        additional_claims: Optional extra claims to include in the token.

    Returns:
        A signed JWT access token.
    """

    # Set the expiration time
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    # Create the payload
    payload: dict[str, Any] = {
        "sub": str(subject),
        "exp": expire,
    }

    # Add any extra claims
    if additional_claims:
        payload.update(additional_claims)

    # Encode and sign the token
    encoded_jwt = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    return encoded_jwt

def decode_access_token(token: str) -> dict[str, Any]:
    """
    Decode and verify a JWT access token.

    Args:
        token: The JWT access token.

    Returns:
        The decoded payload.

    Raises:
        JWTError: If the token is invalid or expired.
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        return payload

    except JWTError as exc:
        raise JWTError("Invalid or expired token.") from exc
    
def get_current_user(token: str) -> dict[str, Any]:
    """
    Decode the current user's JWT token and return its payload.

    This is a temporary implementation.
    Once the User model and database layer are built,
    this function will return a User object instead
    of only the token payload.
    """
    return decode_access_token(token)

