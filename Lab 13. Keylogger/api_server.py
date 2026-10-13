from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TestData(BaseModel):
    data: str


@app.post("/logs")
def receive_test_data(item: TestData):
    with open("received_test.txt", "a") as file:
        file.write(item.data + "\n")

    return {"message": "Test data received"}
