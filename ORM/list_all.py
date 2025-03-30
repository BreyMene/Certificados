from models import Participante, SessionLocal

def list_participante():
    session = SessionLocal()
    try:
        
        participantes = session.query(Participante).all() 
        if not participantes:  # Verifica si la lista está vacía
            print("🔍 No hay participantes registrados en la base de datos.")
            return
        else:
            for participante in participantes:
                print(f"""ID: {participante.id}
Documento: {participante.tipo_documento}.{participante.documento}
Nombre: {participante.nombre_completo}
Email: {participante.correo}
Tipo participante: {participante.tipo_participante}
Fecha: {participante.fecha}\n""")

    finally:
        session.close()

# Ejemplo de uso
if __name__ == "__main__":
    list_participante()
