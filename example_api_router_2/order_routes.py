# Importamos o APIRouter do FastAPI
from fastapi import APIRouter

# Criamos o roteador com prefixo "/pedidos" e tag visual para o Swagger
order_route = APIRouter(prefix="/pedidos", tags=["pedidos"])

# Rota GET com parâmetro de URL dinâmico: /pedidos/{id_pedido}
@order_route.get("/{id_pedido}")
async def buscar_pedido(id_pedido: int):
    """
    Busca os detalhes de um pedido específico pelo seu número identificador.
    """
    # O FastAPI garante que id_pedido é um número inteiro (int).
    # Se alguém digitar "/pedidos/banana", o FastAPI devolve erro 422 sozinho!
    return {
        "mensagem": f"Consultando os dados do pedido #{id_pedido}",
        "id_pedido": id_pedido,
        "status": "Em processamento"
    }

# Rota POST para simular a criação de um novo pedido
@order_route.post("/")
async def criar_pedido(pedido_dados: dict):
    """
    Recebe um dicionário JSON no corpo da requisição e simula a gravação do pedido.
    """
    # pedido_dados é o pacote lacrado que veio no corpo (Body) da requisição
    return {
        "mensagem": "Pedido registrado com sucesso!",
        "dados_recebidos": pedido_dados,
        "codigo_rastreio": "BR123456789XP"
    }
