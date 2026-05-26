from datetime import datetime
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    uid: int
    username: str
    email: str
    verified_at: datetime | None = None
    bio: str = ""
    is_active: bool = True
    full_name: str | None = None


user = User(
    uid = 123,
    username="tom",
    email="abc@def"
)

print(user)
print(user.username)

print(user.bio)
user.bio = "Python Developer"
print(user.bio)

print(user.model_dump_json(indent=2))

