from pydantic import BaseModel


class Prompt(BaseModel):
    role: str
    content: str


class RequestBody(BaseModel):
    message: str
