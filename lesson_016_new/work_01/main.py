from fastapi import FastAPI, Form
from pydantic import BaseModel
from fastapi.responses import FileResponse
from navigate_strategy import navigate_info

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


@app.get("/hello/{name}")
async def say_hello(name: str):
    if name in navigate_info:
        file_path = navigate_info[name]  # Get the path from your dictionary
        # Important: Check if the file exists before trying to serve it
        try:
            with open(file_path, 'r'):
                pass  # Simple file existence check
            return FileResponse(file_path)  # Only serve if the file exists
        except FileNotFoundError:
            return {"error": f"HTML file '{file_path}' not found."}  # Handle file not found
    else:
        out = {"message": f"Hello {name}"}
        return out


@app.post("/hello/calculate")
def calculate(num1: int = Form(ge=0, lt=111111), num2: int = Form(ge=0, lt=111111)):
    print("num1 =", num1, "   num2 =", num2)
    return {"result": num1 + num2}
