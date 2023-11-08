from fastapi import FastAPI
from model.models import TodoCreate
from config.database import collection_name
from schema.schemas import list_of_todos
from bson import ObjectId



app = FastAPI()

@app.get('/')
async def get_todos():
    todos =list_of_todos(collection_name.find())
    return todos


@app.post('/create-to-do',response_model=TodoCreate)
async def post_todo(todo:TodoCreate):
    new_todo = todo.model_dump()
    collection_name.insert_one(new_todo)
    return new_todo

@app.patch("/update/{todo_id}")
async def update(todo_id:str,todo:TodoCreate):
    collection_name.find_one_and_update({"_id":ObjectId(todo_id)}, {"$set":dict(todo)})
    return "updated Successfully"

@app.delete("/delete/{todo_id}")
async def delete(todo_id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(todo_id)})
    return "deleted Successfully"