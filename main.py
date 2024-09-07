from fastapi import FastAPI, HTTPException
from database import database, engine, metadata
from models import products, orders

app = FastAPI()

metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Endpoint para obtener el catálogo de productos disponibles
@app.get("/products/")
async def get_products():
    query = products.select().where(products.c.available == True)
    return await database.fetch_all(query)

# Endpoint para crear un nuevo producto
@app.post("/products/")
async def create_product(name: str, description: str, price: float, stock: int):
    query = products.insert().values(name=name, description=description, price=price, stock=stock)
    await database.execute(query)
    return {"message": "Producto creado exitosamente"}

# Endpoint para crear un pedido
@app.post("/orders/")
async def create_order(product_id: int, quantity: int):
    # Verificar si el producto existe y tiene stock suficiente
    query = products.select().where(products.c.id == product_id)
    product = await database.fetch_one(query)
    
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    if product["stock"] < quantity:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    total_price = product["price"] * quantity

    # Crear el pedido
    order_query = orders.insert().values(product_id=product_id, quantity=quantity, total_price=total_price)
    await database.execute(order_query)

    # Actualizar el stock del producto
    new_stock = product["stock"] - quantity
    update_query = products.update().where(products.c.id == product_id).values(
        stock=new_stock,
        available=(new_stock > 0)  # Marcar no disponible si el stock llega a 0
    )
    await database.execute(update_query)

    return {"message": "Pedido creado exitosamente"}

