from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

# Создаем экземпляр приложения FastAPI
app = FastAPI()


# Определение базового маршрута

@app.get("/")
async def root():
    #return {"message": "Hello, FastAPI!"}
    return FileResponse('index.html')


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


class Item(BaseModel):
    name: str
    price: float


@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "Item deleted", "item_id": item_id}
