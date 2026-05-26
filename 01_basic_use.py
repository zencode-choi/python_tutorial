from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int

try:
    user1 = User(username="tom", email="abc@def", age=38)
    print(user1)

    # validation error @ email and age
    user2 = User(username="tom", email=None, age="old")
    print(user2)
    # %%
except Exception as e:
    print(f"error {str(e)}")


