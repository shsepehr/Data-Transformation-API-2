from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    age: int
    salary: float

@app.post("/transform")
def transform(data: InputData):
    return {
        "salary_per_age": data.salary / data.age
    }
