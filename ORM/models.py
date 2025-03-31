from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener credenciales desde el entorno
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# Declarative base para definir las clases del ORM
Base = declarative_base()

# Configuración de la conexión sin base de datos
DATABASE_URL_NO_DB = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/"
engine_no_db = create_engine(DATABASE_URL_NO_DB)

# Crear la base de datos si no existe
def create_database():
    with engine_no_db.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
        print(f"✅ Base de datos '{DB_NAME}' creada o ya existía.")

# Conectar a la base de datos
DATABASE_URL_WITH_DB = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine_with_db = create_engine(DATABASE_URL_WITH_DB)

# Sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_with_db)

# Modelo de la tabla "fli_participantes"
class Participante(Base):
    __tablename__ = "fli_participantes"
    
    id = Column(Integer, primary_key=True, index=True)
    tipo_documento = Column(String(50), nullable=False)
    documento = Column(String(50), unique=True, nullable=False)
    tipo_participante = Column(String(50), nullable=False, default="ASISTENTE")
    fecha = Column(DateTime, default=datetime.now)
    correo = Column(String(100), unique=True, nullable=False)
    nombre_completo = Column(String(150), nullable=False)

# Modelo de la tabla "fli_contador"
class Contador(Base):
    __tablename__ = "fli_contador"
    
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.now)
    documento = Column(String(50), ForeignKey("fli_participantes.documento"), nullable=False)

# Bloques try-except con traceback para capturar errores detallados
if __name__ == "__main__":
    try:
        create_database()
        Base.metadata.create_all(bind=engine_with_db)  # Intentar crear las tablas
        print("✅ Tablas creadas exitosamente.")
    except Exception as e:
        print(f"❌ Error al crear las tablas: {str(e)}")