from fastapi import FastAPI
from banco_dados import generate_products

app = FastAPI()

products = generate_products()

@app.get('/')
def get_products():
    return {"Products": products}


