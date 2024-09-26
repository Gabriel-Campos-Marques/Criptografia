from fastapi import FastAPI, Request
import json
from model.criptograph import Criptograph

app = FastAPI()

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API FastAPI!"}

@app.post("/cript_image")
async def cript_image(request: Request):
    body = await request.body()
    json_body = json.loads(body)
    content = json_body.get("content", {})
    file64 = content.get('file64')
    return Criptograph.criptgraph_file(file64=file64)
    