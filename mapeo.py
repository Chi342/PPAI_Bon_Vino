from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

class Vino(Base):
    __tablename__ = 'vino'

    id = Column(Integer, primary_key=True, autoincrement=True)
    añada = Column(Integer, nullable=True)
    fechaActualizacion = Column(DateTime, nullable=True)
    imagenEtiqueta = Column(Integer, nullable=True)
    nombre = Column(String(50), nullable=True)
    notaDeCataBodega = Column(Integer, nullable=True)
    precioARS = Column(Numeric(18, 0), nullable=True)

    def tenes_resenas_de_tipo_en_periodo(self, tipo: str, inicio: datetime, fin: datetime) -> bool:
        # Implementation goes here
        pass

    def get_nombre(self) -> str:
        return self.nombre

    def get_precio(self) -> float:
        return self.precio_ars

    def buscar_info_bodega(self) -> dict:
        # Implementation goes here
        pass

    def buscar_varietal(self) -> str:
        # Implementation goes here
        pass

    def calcular_puntaje_de_sommelier_en_periodo(self, inicio: datetime, fin: datetime) -> float:
        # Implementation goes here
        pass

    def calcular_puntaje_promedio(self) -> float:
        # Implementation goes here
        pass

# Connection setup using Windows Authentication
DATABASE_URI = (
    'mssql+pyodbc:///?odbc_connect='
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=MAIN;'
    'DATABASE=Bon_vino;'
    'Trusted_Connection=yes;'
)

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

