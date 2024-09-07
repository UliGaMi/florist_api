from sqlalchemy import create_engine, MetaData
from databases import Database
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL de la base de datos desde el archivo .env
DATABASE_URL = os.getenv('DATABASE_URL')

# Configuración de la base de datos
database = Database(DATABASE_URL)
metadata = MetaData()

# Usar pymysql para conectarse a MySQL
engine = create_engine(
    DATABASE_URL.replace('asyncmy', 'pymysql'), 
    echo=True
)




