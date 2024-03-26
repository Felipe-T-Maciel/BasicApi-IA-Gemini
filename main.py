import google.generativeai as ia
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

API_KEY = 'AIzaSyDXdK7r1MIldNMwshcRYIXStM8QnMA3HPs'
ia.configure(api_key=API_KEY)
model = ia.GenerativeModel('gemini-pro')

class Body(BaseModel):
    text: str

@app.post("/ia")
def getIA(body:Body):
    response = model.generate_content((body.text, " não formate o texto e resuma o texto"))
    return response.text