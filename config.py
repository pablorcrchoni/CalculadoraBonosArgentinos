# Configuración de la Calculadora de Bonos
# Modifica estos valores según tus necesidades

# ========== SERVIDOR ==========
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True

# ========== BASE DE DATOS ==========
DATABASE_NAME = 'bonos_simulaciones.db'
MAX_HISTORIAL = 500  # Máximo de simulaciones a guardar

# ========== VALORES POR DEFECTO ==========
# Estos valores pre-llenados cuando carga la página
DEFAULT_DOLAR_HOY = 1045
DEFAULT_DOLAR_DICIEMBRE = 1200
DEFAULT_TIR_PR17 = 42.5
DEFAULT_PARIDAD_DUAL = 18.5

# ========== BONOS (información referencial) ==========
BONOS = {
    'PR17': {
        'nombre': 'Bonos Globales 2,750% 16/11/2026',
        'ticker': 'PR17',
        'moneda': 'USD',
        'descripcion': 'Bono soberano a tasa fija en dólares'
    },
    'DUAL': {
        'nombre': 'Bonos con Cláusula de Ajuste por CER (Dual) 2026',
        'ticker': 'DUALUL26',
        'moneda': 'ARS/USD',
        'descripcion': 'Bono soberano con variación según el dólar'
    }
}

# ========== LÍMITES DE VALIDACIÓN ==========
MIN_DOLAR = 100
MAX_DOLAR = 10000
MIN_TIR = -100
MAX_TIR = 200
MIN_PARIDAD = -100
MAX_PARIDAD = 200

# ========== PRECISIÓN DE CÁLCULOS ==========
DECIMALES_DEFAULT = 2
DECIMALES_BREAKEVEN = 2

# ========== CARACTERÍSTICAS HABILITADAS ==========
FEATURE_HISTORIAL = True
FEATURE_EXPORTAR_CSV = True
FEATURE_LIMPIAR_HISTORIAL = False  # Set True solo si confías en ti mismo :)
