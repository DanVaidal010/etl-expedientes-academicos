from src.database.schema import crear_tablas
from src.gui.app import iniciar_aplicacion


if __name__ == "__main__":
    crear_tablas()
    iniciar_aplicacion()