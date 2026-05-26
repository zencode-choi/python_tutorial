from datetime import datetime

















from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, ValidationError, field_validator


class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(..., alias="zip")


class Profile(BaseModel):
    bio: str = ""
    interests: List[str] = []


class User(BaseModel):
    uid: int
    username: str
    email: EmailStr
    addresses: List[Address] = []
    profile: Optional[Profile] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    @field_validator("username")
    def normalize_username(cls, v: str) -> str:
        return v.strip().lower()

    @field_validator("profile", mode="before")
    def ensure_profile(cls, v):
        if v is None:
            return Profile()
        return v


if __name__ == "__main__":
    raw = {
        "uid": "456",
        "username": "  Alice ",
        "email": "alice@example.com",
        "addresses": [{"street": "1 Main St", "city": "Townsville", "zip": "12345"}],
        "profile": {"bio": "  Developer ", "interests": ["python", "pydantic"]},
    }

    try:
        # model_validate coerces types and validates nested models
        user = User.model_validate(raw)
        print(user)
        print("username:", user.username)
        print("addresses:", user.addresses)
        # print("JSON:\n", user.model_dump_json(indent=2))

        # Create an updated copy without mutating the original
        updated = user.model_copy()
        updated.profile.bio = "Senior Developer"
        # print("updated bio:", updated.profile.bio)

    except ValidationError as e:
        print("Validation failed:\n", e)
