from typing import Optional

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id:UUID
    title:str =Field(min_length=1)
    author:str =Field(min_length=1,max_length=100)
    description:Optional[str] = Field(title='Description of the book',
                           max_length=100,
                           min_length=1)
    rating:int =Field(gt=-1,lt=101)

    class Config:
        schema_extra = {
            "example":{
                "id":"1227e292-21d4-4d55-b2f6-f1b8d8b0567a",
                "title":"Computer Science Pro",
                "author":"CodingwithSaurabh",
                "description":"This is book related to Computer science",
                "rating":100
            }
        }


BOOKS = []


@app.get("/")
async def read_all_books(books_to_return:Optional[int]=None):
    if len(BOOKS) < 1:
        create_book_no_api()

    if books_to_return and len(BOOKS) >= books_to_return > 0 :
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i-1])
            i +=1
        return new_books
    return BOOKS

@app.post("/")
async def create_book(book:Book):
    BOOKS.append(book)
    return book

@app.get('/book/{book_id}')
async def read_book(book_id:UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise raise_item_cannot_be_found_exception()

@app.put("/{book_id}")
async def update_book(book_id:UUID,book:Book):
    counter = 0

    for x in BOOKS:
        counter +=1
        if x.id == book_id:
            BOOKS[counter-1] = book
            return BOOKS[counter-1]
    raise raise_item_cannot_be_found_exception()


@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID:{book_id} deleted'

    raise raise_item_cannot_be_found_exception()

def create_book_no_api():
    book_1 =Book(id='1227e292-21d4-4d55-b2f6-f1b8d8b0567a',
                 title="Title 1",
                 author="Author 1",
                 description = "description 1",
                 rating=70)
    book_2 = Book(id='1237e292-21d4-4d55-b2f6-f1b8d8b0567a',
                  title="Title 2",
                  author="Author 2",
                  description="description 2",
                  rating=80)
    book_3 = Book(id='1247e292-21d4-4d55-b2f6-f1b8d8b0567a',
                  title="Title 3",
                  author="Author 3",
                  description="description 3",
                  rating=90)
    book_4 = Book(id='1267e292-21d4-4d55-b2f6-f1b8d8b0567a',
                  title="Title 4",
                  author="Author 4",
                  description="description 4",
                  rating=80)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)


def raise_item_cannot_be_found_exception():
    return HTTPException (status_code=404,
                         detail="Book not Found",
                         headers={"X-Header-Error":"Nothing to be seen at the UUID"})





