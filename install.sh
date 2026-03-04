#!/bin/bash
# Script de instalación automatizada

echo "=========================================="
echo "🚀 Instalador - Calculadora de Bonos"
echo "=========================================="
echo ""

# Verificar if Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    echo "   Descárgalo desde: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "✓ Encontrado: $PYTHON_VERSION"
echo ""

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "❌ Error creando entorno virtual"
    exit 1
fi

echo "✓ Entorno virtual creado"
echo ""

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Actualizar pip
echo "📥 Actualizando pip..."
pip install --upgrade pip -q

# Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -r requirements.txt -q

if [ $? -ne 0 ]; then
    echo "❌ Error instalando dependencias"
    deactivate
    exit 1
fi

echo "✓ Dependencias instaladas"
echo ""

# Probar la app
echo "🧪 Ejecutando pruebas..."
python3 test_calculos.py

echo ""
echo "=========================================="
echo "✓ ¡Instalación completada!"
echo "=========================================="
echo ""
echo "🚀 Para ejecutar la aplicación:"
echo ""
echo "   source venv/bin/activate  # Activar env"
echo "   python main.py              # Iniciar servidor"
echo ""
echo "📱 Abre tu navegador en:"
echo "   http://localhost:5000"
echo ""
