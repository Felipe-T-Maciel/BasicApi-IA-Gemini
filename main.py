import google.generativeai as ia
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

API_KEY = 'AIzaSyAgNztT-4SvHysro8CP11XztH7fCCMwJtQ'
ia.configure(api_key=API_KEY)
model = ia.GenerativeModel('gemini-pro')

class Body(BaseModel):
    text: str

@app.post("/ia")
def post(body:Body):
    response = model.generate_content(("Essas comidas estao disponiveis no bife de hoje, diga apenas UMA combinação e quantidade de cada pegar para estar mais saudavel e fale sobre em que pode beneficiar na minha saude. comida = ", body.text, ". não formate o texto e resuma o texto"))
    return response.text