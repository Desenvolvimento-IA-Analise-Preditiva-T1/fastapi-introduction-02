from fastapi import FastAPI

# Importamos o roteador que criamos no outro arquivo (pessoal cuidado com a sequencia)
from order_routes import order_route

# Criamos a instância principal da aplicação
app = FastAPI(title="Minha API de E-commerce")

# Conectamos o roteador de pedidos na aplicação
app.include_router(order_route)

# uvicorn main:app --reload # Ele inicia e gerencia o nosso servidor local
