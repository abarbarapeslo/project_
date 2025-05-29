from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# uvicorn main:app --reload  >> ((para rodar))

app = FastAPI()

templates = Jinja2Templates(directory="templates") #INFORMANDO PASTA TEMPLATES

#fazendo POST

class user(BaseModel):
    Nome: str
    Idade: int
    Localidade: str

# Lista de usuários
usuarios = [
    {"Nome": "Bárbara", "Idade": 22, "Localidade": "Rio de Janeiro"},
    {"Nome": "Estephany", "Idade": 23, "Localidade": "Rio de Janeiro"},
    {"Nome": "Befany", "Idade": 45, "Localidade": "Rio de Janeiro"},
]

# Criar rota para exibir dados
@app.get("/usuarios", response_class=HTMLResponse)
async def listar_usuarios(request: Request): #função assíncrona
    return templates.TemplateResponse("usuarios.html", {"request": request, "usuarios": usuarios})


@app.get("/api/usuarios")
async def listar_usuarios_api():
    return {"usuarios": usuarios}

#Criar Módulo/Rota para inserir usuarios
@app.post("/usuarios")
async def add_user(usuario : user): # <-- recebe os dados via JSON no corpo da requisição
    usuarios.append(usuario.dict()) # converte o modelo para dict e adiciona à lista
    return {"mensagem": "Usuário adicionado!", "usuario" : usuario}

#MODIFICANDO