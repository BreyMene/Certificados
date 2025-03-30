from models import Participante, SessionLocal

def read_user(participante_id):
    # Inicia una sesión
    session = SessionLocal()
    try:
        # Consulta un usuario por ID
        part = session.query(Participante).filter(Participante.id == participante_id).first()
        if part:
            print(f"""ID: {part.id}
Documento: {part.tipo_documento}.{part.documento}
Nombre: {part.nombre_completo}
Email: {part.correo}
Tipo participante: {part.tipo_participante}
Fecha: {part.fecha}\n""")
        else:
            print("Usuario no encontrado")
    finally:
        session.close()

# Ejemplo de uso
if __name__ == "__main__":
    read_user(1) #Retorna la informacion del usuario-return the User Data
    read_user(998) #Usuario no encontrado - User not found
