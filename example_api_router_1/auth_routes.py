# Importamos a ferramenta que permite criar rotas modulares fora do main.py
from fastapi import APIRouter

# Criamos o roteador:
# prefix="/auth" -> todas as rotas deste arquivo começarão com /auth
# tags=["auth"]  -> no Swagger (/docs), estas rotas ficarão agrupadas na seção "auth"
auth_route = APIRouter(prefix="/auth", tags=["auth"])

# Definimos que o endereço "/auth/" respondendo ao método GET executará esta função
@auth_route.get("/")
async def autenticar():
    """
    Docstring: este texto vira a descrição oficial da rota dentro do Swagger (/docs).
    """
    # O FastAPI converte automaticamente dicionários Python para o formato JSON
    return {"mensagem": "Você acessou a rota padrão de autenticação!", "autenticado": False}