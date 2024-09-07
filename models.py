from sqlalchemy import Table, Column, Integer, String, Float, Boolean, MetaData, ForeignKey
from pydantic import BaseModel

metadata = MetaData()

# Definición de la tabla de productos
products = Table(
    'products', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('description', String(255), nullable=False),
    Column('price', Float, nullable=False),
    Column('stock', Integer, nullable=False),
    Column('available', Boolean, nullable=False, default=True)
)

# Definición de la tabla de órdenes
orders = Table(
    'orders', metadata,
    Column('id', Integer, primary_key=True),
    Column('product_id', ForeignKey('products.id'), nullable=False),
    Column('quantity', Integer, nullable=False),
    Column('total_price', Float, nullable=False)
)

# Modelos Pydantic para validación de entrada
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class OrderCreate(BaseModel):
    product_id: int
    quantity: int


