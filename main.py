from fastapi import FastAPI

app = FastAPI()

book_list = []

@app.get("/book")
async def get_strings():
    return {"book": book_list}

@app.post("/book")
async def add_string(name: str = ""):
    book_list.append(name)
    return {"book": book_list}

@app.delete("/book")
async def delete_string(index: int = 0):
    book_list.pop(index)
    return {"book": book_list}
