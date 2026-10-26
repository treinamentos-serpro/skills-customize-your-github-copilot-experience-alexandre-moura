# 📘 Atividade: REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, implementando rotas GET, POST, PUT e DELETE, validando dados com Pydantic e testando os endpoints pela documentação automática.

## 📝 Tarefas

### 🛠️ Primeiras Rotas GET

#### Descrição
Configure o ambiente e crie sua primeira API. Instale as dependências com `pip install fastapi uvicorn`, copie o arquivo `starter-code.py` para `main.py` e execute o servidor com `uvicorn main:app --reload`. Depois, acesse `http://127.0.0.1:8000/docs` para ver a documentação gerada automaticamente.

#### Requisitos
O programa concluído deve:

- Criar a aplicação com `app = FastAPI()`
- Implementar a rota `GET /` retornando uma mensagem de boas-vindas em JSON
- Implementar a rota `GET /books` retornando a lista de livros
- Exibir as duas rotas na página `/docs`

Exemplo de resposta de `GET /books`:

```json
[
  {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "year": 2019},
  {"id": 2, "title": "Automate the Boring Stuff", "author": "Al Sweigart", "year": 2015}
]
```


### 🛠️ Buscar por ID e Filtrar com Query Parameters

#### Descrição
Permita buscar um livro específico pelo seu identificador e filtrar a lista de livros pelo nome do autor. Use path parameters para o id e query parameters para o filtro.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` retornando apenas o livro com o id informado
- Retornar status `404` com a mensagem "Livro não encontrado" quando o id não existir (use `HTTPException`)
- Adicionar o parâmetro opcional `author` em `GET /books`, retornando somente os livros desse autor
- Quando `author` não for informado, retornar todos os livros

Exemplo de requisição:

```
GET /books?author=Al Sweigart
```


### 🛠️ Criar, Atualizar e Remover Livros

#### Descrição
Implemente as operações de escrita de uma API CRUD. Use um modelo Pydantic para validar os dados recebidos no corpo da requisição e altere a lista de livros conforme cada operação.

#### Requisitos
O programa concluído deve:

- Criar a classe `BookCreate` herdando de `BaseModel`, com os campos `title` (str), `author` (str) e `year` (int)
- Implementar `POST /books` que adiciona um novo livro com id automático e retorna status `201`
- Implementar `PUT /books/{book_id}` que substitui os dados de um livro existente
- Implementar `DELETE /books/{book_id}` que remove um livro e retorna uma mensagem de confirmação
- Retornar `404` nas rotas `PUT` e `DELETE` quando o livro não existir

Exemplo de corpo para `POST /books`:

```json
{
  "title": "Fluent Python",
  "author": "Luciano Ramalho",
  "year": 2015
}
```


### 🛠️ Desafio: Validação de Dados

#### Descrição
Torne sua API mais robusta. Use restrições do Pydantic para impedir dados inválidos e melhore a documentação dos endpoints para que outros desenvolvedores entendam como usá-la.

#### Requisitos
O programa concluído deve:

- Garantir que `title` e `author` tenham pelo menos 1 caractere (use `Field(min_length=1)`)
- Garantir que `year` esteja entre 1450 e 2026 (use `Field(ge=1450, le=2026)`)
- Retornar automaticamente status `422` quando os dados enviados forem inválidos, e testar esse caso pela página `/docs`
- Adicionar o parâmetro `tags=["books"]` nas rotas de livros para organizá-las na documentação
- Adicionar uma descrição (`summary`) em cada rota, visível na página `/docs`
