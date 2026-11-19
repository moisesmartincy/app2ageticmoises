import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from geoalchemy2 import Geometry
import datetime

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ZonaAgricola(Base):
    __tablename__ = "zonas_agricolas"

    id = Column(Integer, primary_key=True, index=True)
    nombre_propietario = Column(String, index=True)
    tipo_cultivo = Column(String)
    geometria = Column(Geometry(geometry_type='POLYGON', srid=4326))

class AlertaIncendio(Base):
    __tablename__ = "alertas_incendio"

    id = Column(Integer, primary_key=True, index=True)
    fecha_deteccion = Column(DateTime, default=datetime.datetime.utcnow)
    temperatura_estimada = Column(Float)
    nivel_riesgo = Column(String)
    geometria = Column(Geometry(geometry_type='POINT', srid=4326))

# Crear las tablas en la base de datos (Requiere tener la extensión PostGIS habilitada)
# Base.metadata.create_all(bind=engine)
