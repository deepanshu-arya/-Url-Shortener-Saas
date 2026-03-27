from pydantic import BaseModel

class URLCreate(BaseModel):
    original_url: str

class UserCreate(BaseModel):
    username: str
    password: str