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
    oCript = Criptograph()
    result = oCript.criptgraph_file(file64=file64)
    return result

@app.post("/descript_image")
async def descript_image(request: Request):
    body = await request.body()
    json_body = json.loads(body)
    content = json_body.get("content", {})
    file64 = content.get('file64')
    key = content.get('key')
    oCript = Criptograph()
    result = oCript.descriptgraph_file(file64=file64, sKey=key)
    return result

@app.post("/steganography_file")
async def steganography_file(request: Request):
    body = await request.body()
    json_body = json.loads(body)
    content = json_body.get("content", {})
    file64 = content.get('file64')
    sMessage = content.get('message')
    oCript = Criptograph()
    result = oCript.steganography_file(file64=file64, sMessage=sMessage)
    return result

@app.post("/steganography_reveal")
async def steganography_file(request: Request):
    body = await request.body()
    json_body = json.loads(body)
    content = json_body.get("content", {})
    file64 = content.get('file64')
    oCript = Criptograph()
    result = oCript.steganography_reveal(file64=file64)
    return result
    