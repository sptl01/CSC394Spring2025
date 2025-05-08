import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Tuple
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get the API key from the .env file
api_key = os.getenv("API_KEY")

app = FastAPI()


class Review(BaseModel):
    id: int
    book_id: int
    reviewer: str
    comment: str

#book_list = []
book_list: List[Tuple[int, str]] = [
    (1, "The C Programming Language"),
    (2, "Clean Code: A Handbook of Agile Software Craftsmanship"),
    (3, "Introduction to Algorithms"),
    (4, "Design Patterns: Elements of Reusable Object-Oriented Software"),
    (5, "Programming Pearls")
]
review_list: List[Review] = [
    Review(id=1, book_id=3, reviewer="SP", comment="Great intro to programming."),
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

@app.get("/suggestion")
async def suggest_book(book_id: int = 1):
    matched_reviews = [r.comment for r in review_list if r.book_id == book_id]
    if not matched_reviews:
        raise HTTPException(status_code=404, detail="No reviews found for that book.")

    prompt = build_prompt(matched_reviews)

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"suggestion": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def build_prompt(reviews: List[str]):
    joined = " ".join(reviews)
    prompt = (
        "Suggest a good computer science book based on these user reviews: " + joined +
        ". Only give the title and author."
    )
    return prompt

