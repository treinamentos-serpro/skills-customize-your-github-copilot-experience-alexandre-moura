# Código Inicial para a Atividade de REST APIs com FastAPI
# Instale as dependências: pip install fastapi uvicorn
# Copie este arquivo para main.py e execute: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Banco de dados fictício em memória
books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "year": 2019},
    {"id": 2, "title": "Automate the Boring Stuff", "author": "Al Sweigart", "year": 2015},
]

# Tarefa 1: Primeiras Rotas GET
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de livros!"}

# Crie a rota GET /books que retorna a lista de livros


# Tarefa 2: Buscar por ID e Filtrar com Query Parameters
# Crie a rota GET /books/{book_id} e o parâmetro opcional author em GET /books


# Tarefa 3: Criar, Atualizar e Remover Livros
class BookCreate(BaseModel):
    title: str
    author: str
    year: int

# Crie as rotas POST /books, PUT /books/{book_id} e DELETE /books/{book_id}


# Tarefa 4 (Desafio): Validação de Dados
# Adicione restrições com Field e os parâmetros tags e summary nas rotas
