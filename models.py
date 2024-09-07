from sqlalchemy import Table, Column, Integer, String, Float, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from database import metadata

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("description", String(255)),
    Column("price", Float),
    Column("stock", Integer),
    Column("available", Boolean, default=True), 
)

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("quantity", Integer),
    Column("total_price", Float),
    Column("order_date", TIMESTAMP, server_default=func.now())
)


