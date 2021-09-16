from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/forward")
async def forward():
    return {"action": "forward"}

@app.post("/backward")
async def backward():
    return {"action": "backward"}

@app.post("/leftward")
async def leftward():
    return {"action": "leftward"}

@app.post("/rightward")
async def rightward():
    return {"action": "rightward"}

@app.post("addcode")
async def addcode():
    return {"action": "addcode"}