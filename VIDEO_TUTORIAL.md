# Tutorial Video - Calculadora de Bonos (Versión Texto)

## 📹 Flujo de Demostración

### ESCENA 1: Inicio de la Aplicación
```
[Terminal]
$ python main.py
 * Running on http://0.0.0.0:5000
 * Debug mode: on

[Navegador]
http://localhost:5000
↓
[Pantalla] Aparece formulario con 4 campos
```

### ESCENA 2: Ingresando Datos
```
Usurio ve:
┌──────────────────────────────────┐
│ 📊 Bonos Soberanos              │
│ ─────────────────────────────────│
│ 💵 Dólar Hoy:      [  1045  ]    │
│ 📅 Dólar Dic:      [  1200  ]    │
│ 📈 TIR PR17:       [  42.5  ]    │
│ 💱 Paridad Dual:   [  18.5  ]    │
│                                  │
│ [🚀 Calcular Rendimientos]      │
└──────────────────────────────────┘

Acción: Llena valores de ejemplo
Tiempo: 10 segundos
```

### ESCENA 3: Cálculo en Progreso
```
[Botón pulsado]
"Procesando simulación..."
[Spinner animado]
Tiempo: 1 segundo
```

### ESCENA 4: Resultados Mostrados
```
┌──────────────────────────────────────┐
│ 📊 Resultados                        │
│ ───────────────────────────────────  │
│ ┌─────────────┐    ┌─────────────┐  │
│ │  PR17 ✓     │    │   Dual      │  │
│ │  42.50%     │    │   33.14%    │  │
│ │ (mejor)     │    │  (peor)     │  │
│ └─────────────┘    └─────────────┘  │
│                                      │
│ 💹 Break-Even Dólar                 │
│ ────────────────────────────────────│
│         $1,234.56                    │
│ Precio de paridad entre opciones    │
│                                      │
│ Variación Dólar Esperada: +14.64%   │
│                                      │
│ [🔄 Nueva Simulación] [📥 Descargar]│
└──────────────────────────────────────┘

Tiempo: 2 segundos (aparición)
Transición: Suave fade-in
```

### ESCENA 5: Visualización de Historial
```
[Scroll bajo]
Aparece sección "📋 Últimas Simulaciones"

Muestra:
- Última simulación (hace 2 segundos)
- Fecha y hora exacta
- Parámetros ingresados
- Resultado (mejor opción)
- Break-even calculado

Tiempo: 3 segundos
```

### ESCENA 6: Acceso desde Android
```
[Cambio de dispositivo]
Smartphone Android conectado al WiFi

[URL en navegador]
http://192.168.1.100:5000

[Pantalla Android]
La misma interfaz se ve responsive:
- Buttons más grandes para touch
- Inputs tocan toda el ancho
- Historial en scroll vertical

Acción: Toca "Calcular"
Resultado: Funciona igual en móvil
```

### ESCENA 7: Descarga de Datos
```
[Botón "📥 Descargar Datos"]
↓
Navegador descarga: bonos-simulaciones-2026-03-03.csv
↓
Archivo abierto en Excel:
┌─────┬────────┬────────┬─────────┬──────────┐
│Fecha│Dol Hoy│Dol Dic│TIR PR17│Rendimiento
├─────┼────────┼────────┼─────────┼──────────┤
│3/3  │ 1045   │ 1200   │ 42.5%  │ PR17
│3/3  │ 1045   │ 1300   │ 42.5%  │ PR17
│3/3  │ 1045   │ 1500   │ 42.5%  │ Dual
└─────┴────────┴────────┴─────────┴──────────┘

Tiempo: Instantáneo
```

### ESCENA 8: Modificar Configuración
```
[Usuario abre config.py]
Edita valores por defecto:

DEFAULT_DOLAR_HOY = 1045  → 1050
DEFAULT_DOLAR_DICIEMBRE = 1200  → 1250

[Guarda config.py]
[Actualiza navegador]

Los nuevos valores aparecen precargados

Sin necesidad de reiniciar (Flask auto-recarga)
```

### ESCENA 9: Pruebas Automatizadas
```
[Terminal]
$ python test_calculos.py

🧪 PRUEBAS DE CALCULADORA DE BONOS
════════════════════════════════════

CASO 1: Dólar sube poco (PR17 más atractivo)
  Dólar: $1.045 → $1.100 (+5.26%)
  PR17:  42.50%
  Dual:  23.76%
  ✓ Mejor: PR17
  Break-Even: $1,234.56

CASO 2: Dólar sube mucho (Dual más atractivo)
  Dólar: $1.045 → $1.400 (+33.97%)
  PR17:  42.50%
  Dual:  52.47%
  ✓ Mejor: Dual
  Break-Even: $1,234.56

✓ Pruebas completadas
```

### ESCENA 10: Uso Real - Análisis Completo
```
[Usuario profesional - Caso real]

1. Abre calculadora
2. Ingresa predicción actualizada del dólar
3. Verifica TIR actual en MERVAL
4. Verifica paridad Dual en mercado
5. Hace clic en Calcular
6. Obtiene resultados inmediatos
7. Guarda en historial automáticamente
8. Exporta CSV para analizar en Excel
9. Compara con simulaciones anteriores
10. Toma decisión informada

Tiempo total: 5 minutos
Resultado: Decisión financiera basada en datos
```

---

## 📊 Flujo de Datos - Diagrama

```
┌─────────────────────────────────────────────────┐
│           Navegador (Usuario)                   │
│  ┌───────────────────────────────────────────┐  │
│  │  Formulario HTML                          │  │
│  │  • Input: Dólar Hoy                       │  │
│  │  • Input: Dólar Diciembre                 │  │
│  │  • Input: TIR PR17                        │  │
│  │  • Input: Paridad Dual                    │  │
│  │  • Button: Calcular                       │  │
│  └───────────────────────────────────────────┘  │
└────────────────┬────────────────────────────────┘
                 │
          JSON POST /calcular
                 │
                 ▼
┌────────────────────────────────────────────────┐
│         Flask Backend (main.py)                │
│  ┌──────────────────────────────────────────┐  │
│  │ calcular_rendimientos()                  │  │
│  │ ├─ Variación Dólar (%)                  │  │
│  │ ├─ Rendimiento PR17                     │  │
│  │ ├─ Rendimiento Dual                     │  │
│  │ ├─ Mejor Opción                         │  │
│  │ └─ Break-Even Dólar                     │  │
│  └──────────────────────────────────────────┘  │
│                                                │
│  ┌──────────────────────────────────────────┐  │
│  │ guardar_simulacion()                     │  │
│  │ └─ INSERT INTO simulaciones              │  │
│  └──────────────────────────────────────────┘  │
└────────────────┬────────────────────────────────┘
                 │
          JSON Response + SQLite Write
                 │
                 ▼
┌────────────────────────────────────────────────┐
│      SQLite Database                           │
│  ┌──────────────────────────────────────────┐  │
│  │ Tabla: simulaciones                      │  │
│  │ Columnas:                                │  │
│  │ • id, fecha_creacion                     │  │
│  │ • dolar_hoy, dolar_diciembre             │  │
│  │ • tir_pr17, paridad_dual                 │  │
│  │ • rendimiento_pr17, rendimiento_dual     │  │
│  │ • mejor_opcion, breakeven_dolar          │  │
│  │                                          │  │
│  │ 📁 bonos_simulaciones.db                 │  │
│  └──────────────────────────────────────────┘  │
└────────────────────────────────────────────────┘
```

---

## 🎯 Casos de Uso - Guion

### Usuario 1: Inversor Conservador
```
[Escena] Oficina en Buenos Aires, 10:00 AM

"Tengo $50.000 USD y no sé si comprar PR17 o Dual.
El dólar está en $1.045, pero creo que llega a $1.150
máximo en diciembre. PR17 está rindiendo 42%. "

[Acción]
1. Abre calculadora
2. Ingresa: 1045, 1150, 42, 18.5
3. Calcula
4. Ve: PR17 rinde 42%, Dual 26.7%
   Break-Even: $1.261

[Conclusión]
"Claro, voy PR17 porque mi predicción del dólar
es conservadora."
```

### Usuario 2: Operador de Renta Fija
```
[Escena] Trading desk, horario bursátil

"Necesito saber si vale la pena la rally del Dual
con la devaluación esperada."

[Acción]
1. Abre calculadora
2. Ingresa: 1045, 1400, 42.5, 18.5
3. Calcula
4. Ve: Dual rinde 62%, PR17 42.5%
   Break-Even: $1.234,56

[Conclusión]
"Con devaluación al 34%, Dual rinde casi 50% más.
Vale la pena tomar riesgo dólar."
```

### Usuario 3: Analista Macroeconómico
```
[Escena] Investigación económica, modelado

"Quiero crear un análisis de sensibilidad:
qué pasa en 5 escenarios distintos de dólar."

[Acción]
1. Simula 5 veces con diferentes dólares:
   - Optimista: $1.050 (casi nada)
   - Realista bajo: $1.150 (+10%)
   - Realista: $1.200 (+14.64%)
   - Realista alto: $1.300 (+24.4%)
   - Pesimista: $1.500 (+43.5%)
2. Exporta CSV
3. Copia a Excel y hace gráfico

[Conclusión]
"En X puntos de dólar cambia la recomendación.
El break-even es la variable crítica."
```

---

## 🎬 Duración Total del Tutorial

- **Video versión rápida (Sin sonido):** 2 minutos
- **Video versión didáctica (Con explicaciones):** 5 minutos
- **Video versión completa (Casos reales):** 10 minutos

---

## ✨ Puntos Clave a Enfatizar

✅ Simple pero poderosa
✅ Responde una pregunta clara: ¿PR17 o Dual?
✅ Cálculos matemáticos exactos
✅ Historial para seguimiento
✅ Acceso desde cualquier dispositivo
✅ Privacidad total (local only)
✅ Educativa, no asesoría financiera

---

## 📱 Versión Mobile

La misma funcionalidad en pantalla pequeña:
- Inputs más grandes
- Botones optimizados para touch
- Scroll vertical para historial
- Todos los resultados visibles sin desplazarse mucho
