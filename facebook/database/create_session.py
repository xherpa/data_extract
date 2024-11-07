from facebook.config.session import SessionLocal
#from facebook.utils.database_models import User

# Función para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

