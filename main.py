from flask import Flask, render_template, request, jsonify, send_file, send_from_directory
import sqlite3
from datetime import datetime
import os

app = Flask(__name__, static_folder='.', static_url_path='/static')
DATABASE = 'bonos_simulaciones.db'

# Inicializar base de datos
def init_db():
    """Crear tabla de simulaciones si no existe"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS simulaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            dolar_hoy REAL NOT NULL,
            dolar_diciembre REAL NOT NULL,
            tir_pr17 REAL NOT NULL,
            paridad_dual REAL NOT NULL,
            rendimiento_pr17 REAL NOT NULL,
            rendimiento_dual REAL NOT NULL,
            mejor_opcion TEXT NOT NULL,
            breakeven_dolar REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def calcular_rendimientos(dolar_hoy, dolar_diciembre, tir_pr17, paridad_dual, tir_adicional=0):
    """
    Calcula los rendimientos de Bono Fijo vs Bono Indexado
    
    Bono Fijo: Rendimiento directo = TIR fija
    Bono Indexado: Rendimiento = Variación índice + Ganancia por paridad (convergencia) + TIR Adicional
    
    La paridad representa el precio actual del bono como % del valor nominal.
    Si compras a 93.5%, tu ganancia por convergencia es: (100/93.5 - 1) * 100 ≈ 6.95%
    
    TIR Adicional: Rendimiento adicional del bono (ej. CER+6.5%)
    """
    # 1. Ganancia por "descuento" de paridad (convergencia al valor nominal 100%)
    # Si paridad_dual viene como 93.5, la convertimos a ganancia real
    ganancia_paridad = ((100 / paridad_dual) - 1) * 100
    
    # 2. Variación del índice proyectada
    variacion_indice = ((dolar_diciembre - dolar_hoy) / dolar_hoy) * 100
    
    # 3. Rendimiento Bono Indexado Total (Variación + Ganancia Paridad + TIR Adicional)
    # Nota: Financieramente es multiplicativo, pero para simplificar usamos suma
    rendimiento_bono_indexado = variacion_indice + ganancia_paridad + tir_adicional
    
    # 4. Rendimiento Bono Fijo (Tasa fija directa)
    rendimiento_bono_fijo = tir_pr17
    
    # 5. Cálculo de Break-even
    # Despejando el Valor_Proyectado (dolar_diciembre) para que ambos rendimientos sean iguales:
    # TIR_Fijo = ((Valor_Proyectado / Valor_Hoy) - 1) * 100 + Ganancia_Paridad + TIR_Adicional
    # Reordenando:
    # (TIR_Fijo - Ganancia_Paridad - TIR_Adicional) / 100 = Valor_Proyectado / Valor_Hoy - 1
    # Valor_Proyectado = Valor_Hoy * (1 + (TIR_Fijo - Ganancia_Paridad - TIR_Adicional) / 100)
    variacion_necesaria_decimal = (rendimiento_bono_fijo - ganancia_paridad - tir_adicional) / 100
    breakeven_indice = dolar_hoy * (1 + variacion_necesaria_decimal)
    
    mejor_opcion = "PR17" if rendimiento_bono_fijo > rendimiento_bono_indexado else "Dual"
    
    return {
        'rendimiento_pr17': round(rendimiento_bono_fijo, 2),
        'rendimiento_dual': round(rendimiento_bono_indexado, 2),
        'mejor_opcion': mejor_opcion,
        'breakeven_dolar': round(breakeven_indice, 2),
        'variacion_dolar': round(variacion_indice, 2)
    }

def guardar_simulacion(dolar_hoy, dolar_diciembre, tir_pr17, paridad_dual, rendimientos):
    """Guardar simulación en la base de datos"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO simulaciones 
        (dolar_hoy, dolar_diciembre, tir_pr17, paridad_dual, rendimiento_pr17, rendimiento_dual, mejor_opcion, breakeven_dolar)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        dolar_hoy,
        dolar_diciembre,
        tir_pr17,
        paridad_dual,
        rendimientos['rendimiento_pr17'],
        rendimientos['rendimiento_dual'],
        rendimientos['mejor_opcion'],
        rendimientos['breakeven_dolar']
    ))
    conn.commit()
    conn.close()

def obtener_historial(limite=50):
    """Obtener historial de simulaciones"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM simulaciones 
        ORDER BY fecha_creacion DESC 
        LIMIT ?
    ''', (limite,))
    simulaciones = cursor.fetchall()
    conn.close()
    return simulaciones

@app.route('/')
def index():
    """Página principal - Sirve la PWA desde la raíz"""
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html', mimetype='text/html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Sirve archivos estáticos (manifest.json, sw.js, etc)"""
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), filename)

@app.route('/calcular', methods=['POST'])
def calcular():
    """Endpoint para calcular rendimientos"""
    try:
        data = request.get_json()
        
        # Validar datos
        dolar_hoy = float(data.get('dolar_hoy', 0))
        dolar_diciembre = float(data.get('dolar_diciembre', 0))
        tir_pr17 = float(data.get('tir_pr17', 0))
        paridad_dual = float(data.get('paridad_dual', 0))
        tir_adicional = float(data.get('tir_adicional', 0))
        
        if dolar_hoy <= 0 or dolar_diciembre <= 0:
            return jsonify({'error': 'Precios del dólar deben ser mayores a 0'}), 400
        
        # Calcular rendimientos
        rendimientos = calcular_rendimientos(dolar_hoy, dolar_diciembre, tir_pr17, paridad_dual, tir_adicional)
        
        # Guardar en base de datos
        guardar_simulacion(dolar_hoy, dolar_diciembre, tir_pr17, paridad_dual, rendimientos)
        
        return jsonify(rendimientos)
    
    except ValueError as e:
        return jsonify({'error': f'Valores inválidos: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Error al procesar: {str(e)}'}), 500

@app.route('/historial')
def api_historial():
    """API para obtener historial"""
    historial = obtener_historial(100)
    return jsonify([dict(row) for row in historial])

@app.route('/limpiar-historial', methods=['POST'])
def limpiar_historial():
    """Limpiar todo el historial"""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM simulaciones')
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'mensaje': 'Historial limpiado'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Inicializar base de datos
    if not os.path.exists(DATABASE):
        init_db()
    else:
        init_db()  # Asegurar que la tabla existe
    
    # Ejecutar app
    app.run(host='0.0.0.0', port=5000, debug=True)
