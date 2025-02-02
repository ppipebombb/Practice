from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# pydantic = data validation
# basemodel = bikin kerangka model (like a panutan) to be refered like a skema
from typing import Optional, List
# typing = helps with making sure which data type needed to be passed. for documentation purposes
# Optional = tells it that it's an optional parameter and it doesnt need to pass it hwen its called

app = FastAPI(title="Todo API")

class Todo(BaseModel): # the todo will consists of this structure
    name : str
    due_date : str
    desc : str

store_todo = [] # just a simple db

@app.get('/')
async def home():
    return {'hi':'Hello World'}

@app.post('/todo/') # post = to make, create new
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo
# todo = request body parameter
# Todo = pydantic model that ensures the incoming data follows a predefined structure. it follows the basemodel structure (name, due_date, desc)
# so this funct minta data untuk isi name, due_date, desc

@app.get ('/todo/{id}') # retrieve a todo using its id
async def get_todo(id: int):
    if id < 0 or id >= (store_todo): # index check, to check if there is a todo stored with that id
        raise HTTPException(status_code=404, detail="Todo not found")
    return store_todo[id]

@app.get ('/todo/', response_model=List[Todo]) # get = pull data, to retrieve
async def get_all_todos():
    return store_todo # returns the entire store_todo's list
# response_model = tells FastAPI that the response should be a list of Todo objects

@app.put('/update/{id}') # put = update
async def update_todo(id:int, todo: Todo):
    if id < 0 or id >= len(store_todo): # index check, to check if there is a todo stored with that id
        raise HTTPException(status_code=404, detail="Todo not found")
    store_todo[id] = todo  # update the todo
    return {"message": "Todo updated successfully", "todo": todo}
    
@app.delete('/todo/{id}')
async def delete_todo(id:int):
    if id < 0 or id >= len(store_todo): # index check, to check if there is a todo stored with that id
        raise HTTPException(status_code=404, detail="Todo not found")    
    delete_todo = store_todo.pop(id)  # remove the todo with that id
    return {"message": "Todo deleted successfully", "todo": delete_todo}
    