# Importamos a classe principal da aplicação
from fastapi import FastAPI

# Importamos as instâncias dos roteadores criados nos outros arquivos
from auth_routes import auth_route
from order_routes import order_route

# Instanciamos o aplicativo FastAPI
app = FastAPI()

# Plugamos os roteadores dentro da aplicação central
app.include_router(auth_route)
app.include_router(order_route)

# uvicorn main:app --reload