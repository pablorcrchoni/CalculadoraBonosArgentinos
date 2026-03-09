# Calculadora de Arbitraje de Bonos Soberanos Argentinos

Una aplicación web para comparar en tiempo real el rendimiento del **PR17** vs el **Bono Dual (TTD26)** según tus propias predicciones del dólar.

## 🌟 Funcionalidades

✅ **Cálculo de Rendimientos:**
- Rendimiento directo del PR17 (Tasa fija)
- Rendimiento del Dual (Variación dólar + Ganancia por paridad)
- Comparación lado a lado

✅ **Análisis de Break-Even:**
- Calcula automáticamente el precio del dólar en el que ambas opciones rinden igual

✅ **Historial de Simulaciones:**
- Guarda cada simulación en SQLite
- Ver el historial completo desde el móvil
- Descargar datos en CSV

✅ **Acceso Remoto:**
- Funciona en cualquier dispositivo (PC, tablet, móvil)
- Ejecutado en host `0.0.0.0` para acceso desde la red local

## 📋 Requisitos

- Python 3.7+
- Flask
- SQLite3 (incluido en Python)

## 🚀 Instalación y Ejecución

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación

```bash
python main.py
```

La aplicación estará disponible en:
- **Desde tu PC:** `http://localhost:5000`
- **Desde tu Android:** `http://<IP-DE-TU-PC>:5000`

> Encuentra tu IP local con `ipconfig` (Windows) o `ifconfig` (Linux/Mac)

## 📊 Parámetros de Entrada

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| **💵 Dólar Hoy** | Precio actual del dólar | 1045 |
| **📅 Dólar Diciembre** | Tu predicción para diciembre | 1200 |
| **📈 TIR PR17 (%)** | Tasa interna de retorno del PR17 | 42.5 |
| **💱 Paridad Dual (%)** | Ganancia por paridad del Dual | 18.5 |

## 🧮 Lógica de Cálculo

### Rendimiento PR17
```
Rendimiento PR17 = TIR fija
```

### Rendimiento Dual
```
Rendimiento Dual = Variación Dólar (%) + Paridad Dual (%)
Variación Dólar (%) = ((Dólar Diciembre - Dólar Hoy) / Dólar Hoy) × 100
```

### Break-Even (Dólar de Paridad)
```
El precio del dólar en el que:
Rendimiento PR17 = Variación Dólar del Dual + Paridad Dual

Break-Even = Dólar Hoy × (1 + (Rendimiento PR17 - Paridad Dual) / 100)
```

## 💾 Base de Datos

Los datos se guardan automáticamente en `bonos_simulaciones.db` con la siguiente tabla:

```sql
CREATE TABLE simulaciones (
    id INTEGER PRIMARY KEY,
    fecha_creacion TIMESTAMP,
    dolar_hoy REAL,
    dolar_diciembre REAL,
    tir_pr17 REAL,
    paridad_dual REAL,
    rendimiento_pr17 REAL,
    rendimiento_dual REAL,
    mejor_opcion TEXT,
    breakeven_dolar REAL
)
```

## 🎨 Diseño Mobile-First

- Interfaz responsive optimizada para móvil
- Gradientes moderno y botones intuitivos
- Compatible con Android, iOS y navegadores de escritorio

## 📥 Exportar Datos

Haz clic en **"📥 Descargar Datos"** para exportar tu historial de simulaciones en formato CSV compatible con Excel.

## 🔧 Endpoints API

### POST /calcular
Realiza una simulación y la guarda en la BD.

```json
{
  "dolar_hoy": 1045,
  "dolar_diciembre": 1200,
  "tir_pr17": 42.5,
  "paridad_dual": 18.5
}
```

### GET /historial
Obtiene las últimas 100 simulaciones guardadas.

### GET /
Carga la interfaz web principal.

## 📱 Uso desde Android

1. Encontrar IP local de tu PC:
   ```bash
   # Linux/Mac
   ifconfig | grep "inet "
   
   # Windows
   ipconfig
   ```

2. Abrir en navegador del Android:
   ```
   http://<IP_LOCAL>:5000
   ```
   Ej: `http://192.168.1.100:5000`

3. Guardar como acceso directo en pantalla de inicio (opcional)

## 🐛 Troubleshooting

### No puedo acceder desde Android
- Verifica que ambos dispositivos estén en la misma red WiFi
- Asegúrate que el firewall no bloquea el puerto 5000
- Intenta con la IP local exacta (no `localhost`)

### Base de datos llena
- Borrar historial: Elimina manualmente `bonos_simulaciones.db`
- O actualiza main.py para agregar un endpoint de limpieza

## 📈 Ejemplo de Uso

1. **Escenario:** Dólar en $1.200 para diciembre
   - Dólar Hoy: $1.045
   - Variación: +14.64%

2. **Comparativa:**
   - PR17: 42.5% anual (rendimiento fijo)
   - Dual: 18.5% + 14.64% variación = 33.14%

3. **Resultado:** PR17 es mejor opción

4. **Break-Even:** $1.234,56
   - Si el dólar llega a $1.234,56, ambos rinden igual
   - Si sube más, mejor Dual
   - Si sube menos, mejor PR17

## 📄 Licencia

Uso personal y educativo.

---

¿Preguntas? Modifica `main.py` según tus necesidades o agrega más funciones.
