from pydantic import BaseModel
from bson import ObjectId


class TodoCreate(BaseModel):
    title:str = 'do homework'
    description:str = 'Now and ever'
    completed:bool = False
