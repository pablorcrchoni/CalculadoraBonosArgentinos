@echo off
REM Script de instalación para Windows
echo.
echo ==========================================
echo      Instalador - Calculadora de Bonos
echo ==========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo NOTA: Debes instalar Python primero
    echo Descargalo desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo Encontrado: %PYTHON_VERSION%
echo.

REM Crear entorno virtual
echo Creando entorno virtual...
python -m venv venv

if errorlevel 1 (
    echo Error creando entorno virtual
    pause
    exit /b 1
)

echo Entorno virtual creado
echo.

REM Activar entorno virtual
echo Activando entorno virtual...
call venv\Scripts\activate.bat

REM Actualizar pip
echo Actualizando pip...
python -m pip install --upgrade pip -q

REM Instalar dependencias
echo Instalando dependencias...
pip install -r requirements.txt -q

if errorlevel 1 (
    echo Error instalando dependencias
    pause
    exit /b 1
)

echo Dependencias instaladas
echo.

REM Probar la app
echo Ejecutando pruebas...
python test_calculos.py

echo.
echo ==========================================
echo      Instalacion completada!
echo ==========================================
echo.
echo NOTA: Para ejecutar la aplicacion:
echo.
echo   1. Abre una terminal en esta carpeta
echo   2. Ejecuta: venv\Scripts\activate.bat
echo   3. Ejecuta: python main.py
echo.
echo   Luego abre: http://localhost:5000
echo.
pause
