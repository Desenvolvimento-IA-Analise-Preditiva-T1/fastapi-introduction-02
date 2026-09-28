from product import Produc


def generate_products():
    list_products = []

    for x in range(20):
        p = Produc(name = f"Product {x}", price = 2.45 * x)
        list_products.append(p)

    return list_products
