from pydantic import BaseModel # Vamos definir os tipos dos nossos dados com um escopo mias limpo do que no POO

class Produc(BaseModel):
    name: str
    price: float


