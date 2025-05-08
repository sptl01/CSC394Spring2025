from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Review(BaseModel):
    id: int
    book_id: int
    reviewer: str
    comment: str

#book_list = []
book_list: List[str] = []
review_list: List[Review] = [
    Review(id=1, book_id=1, reviewer="SP", comment="Great intro to programming."),
]
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

@app.get("/reviews")
async def get_reviews():
    return {"reviews": review_list}
