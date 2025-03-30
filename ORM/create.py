import csv
# Usamos la tabla existente
from models import Participante, SessionLocal, create_database  

# Asegurar que la base de datos esté creada
create_database()

# Crear sesión
session = SessionLocal()

def cargar_usuarios_desde_csv(archivo_csv):
    try:
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                nuevo_usuario = Participante(
                    tipo_documento=fila['tipo_documento'],
                    documento=fila['documento'],
                    tipo_participante=fila['tipo_participante'],
                    correo=fila['correo'],
                    nombre_completo=fila['nombre_completo']
                )
                session.add(nuevo_usuario)
        
        session.commit()
        print("✅ Usuarios cargados exitosamente desde el CSV.")
    except Exception as e:
        session.rollback()
        print(f"❌ Error al cargar usuarios: {e}")
    finally:
        session.close()

# Nombre del archivo CSV con los datos, la ruta del csv va con \\
archivo_csv = "ruta_csv\\usuarios.csv"
cargar_usuarios_desde_csv(archivo_csv)
