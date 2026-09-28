from fastapi import APIRouter

# Definimos o prefixo "/pedidos" e agrupamos na seção "pedidos" do Swagger
order_route = APIRouter(prefix="/pedidos", tags=["pedidos"])

# Esta rota responderá na URL completa: http://127.0.0.1:8000/pedidos/
@order_route.get("/")
async def pedidos():
    """
    Essa é a rota de pedidos padrão do nosso sistema.
    """
    return {"mensagem": "Você acessou a rota de pedidos"}