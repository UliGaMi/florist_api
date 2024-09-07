from fastapi import FastAPI, HTTPException
from models import products, orders, ProductCreate, OrderCreate
from database import database, engine, metadata

app = FastAPI()

# Crear todas las tablas en la base de datos
metadata.create_all(engine)

# Conectar a la base de datos al iniciar la app
@app.on_event("startup")
async def startup():
    await database.connect()

# Desconectar de la base de datos al cerrar la app
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
async def create_product(product: ProductCreate):
    query = products.insert().values(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
        available=product.stock > 0  # Disponible si el stock es mayor a 0
    )
    await database.execute(query)
    return {"message": "Producto creado exitosamente"}

# Endpoint para crear una nueva orden
@app.post("/orders/")
async def create_order(order: OrderCreate):
    # Verificar si el producto existe y tiene stock suficiente
    query = products.select().where(products.c.id == order.product_id)
    product = await database.fetch_one(query)
    
    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    if product["stock"] < order.quantity:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    total_price = product["price"] * order.quantity

    # Crear el pedido
    order_query = orders.insert().values(
        product_id=order.product_id,
        quantity=order.quantity,
        total_price=total_price
    )
    await database.execute(order_query)

    # Actualizar el stock del producto
    new_stock = product["stock"] - order.quantity
    update_query = products.update().where(products.c.id == order.product_id).values(
        stock=new_stock,
        available=(new_stock > 0)
    )
    await database.execute(update_query)

    return {"message": "Pedido creado exitosamente"}


