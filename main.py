from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Welcome note with a customized message
@app.get("/")
def read_root():
    return {"message": "Welcome to the API! Customized by RupaAccenture."}

# Comment: Define a Pydantic model for the new endpoint
class TextRequest(BaseModel):
    text: str

# Comment: Use the generate function to create a checksum
def generate(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

# Comment: Create a new FastAPI endpoint
@app.post("/generate-token/")
def generate_token(request: TextRequest):
    checksum = generate(request.text)
    return {"checksum": checksum}
