# Sistema de Teledetección Forestal

API FastAPI y panel Streamlit para visualizar alertas de incendios. La aplicación inicia con datos simulados.

## Instalación en Windows

Con Python 3 instalado, ejecuta en PowerShell:

```powershell
git clone https://github.com/moisesmartincy/app2ageticmoises.git
cd app2ageticmoises
py -3 -m venv env
.\env\Scripts\python.exe -m pip install -r requirements.txt
.\run.bat
```

El panel se abre en http://localhost:8501 y la documentación de la API está en http://localhost:8000/docs.

## Base de datos opcional

El modo simulado funciona sin PostgreSQL. Para usar los modelos de `database.py`, habilita PostGIS en tu base de datos PostgreSQL y configura la variable de entorno `DATABASE_URL` en el proceso que importe el módulo. Usa el formato `postgresql+psycopg2://USUARIO:CLAVE@HOST:5432/BASE` con tus propios valores.
