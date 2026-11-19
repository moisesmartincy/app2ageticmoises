@echo off
cd /d "%~dp0"
echo ====================================================
echo Iniciando Sistema de Teledeteccion Forestal...
echo ====================================================

echo 1. Iniciando API (Backend)...
start cmd /k ".\env\Scripts\python.exe -m uvicorn main:app --reload"

echo 2. Esperando a que inicie la API...
timeout /t 3 /nobreak > NUL

echo 3. Iniciando Dashboard (Frontend)...
start cmd /k ".\env\Scripts\python.exe -m streamlit run app.py"

echo Todo iniciado!
