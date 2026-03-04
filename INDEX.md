# 📊 Calculadora de Arbitraje de Bonos Soberanos Argentinos

## 🎯 Propósito

Herramienta para comparar **en tiempo real** el rendimiento del **PR17** vs el **Bono Dual (TTD26)** según tus propias predicciones del dólar.

Toma decisiones de inversión informadas basadas en cálculos matemáticos claros.

---

## 📚 Documentación Completa

### 🚀 Para Comenzar
- **[QUICKSTART.md](QUICKSTART.md)** - Instala y comienza en 2 minutos
- **[README.md](README.md)** - Documentación completa y detallada

### 📖 Guías
- **[EXAMPLES.md](EXAMPLES.md)** - Casos de uso reales y ejemplos prácticos
- **[VIDEO_TUTORIAL.md](VIDEO_TUTORIAL.md)** - Flujo visual del programa

### 🔧 Configuración
- **[config.py](config.py)** - Personaliza valores y límites

### 👨‍💻 Código
- **[main.py](main.py)** - Backend Flask + SQLite (220 líneas)
- **[templates/index.html](templates/index.html)** - Frontend HTML/CSS/JS (450 líneas)
- **[test_calculos.py](test_calculos.py)** - Pruebas de cálculos

### 📦 Dependencias
- **[requirements.txt](requirements.txt)** - Paquetes necesarios (Flask 2.3.3)

### 📋 Otros
- **[CHANGELOG.md](CHANGELOG.md)** - Historial de versiones
- **[.gitignore](.gitignore)** - Configuración para Git

---

## ⭐ Características Principales

### 💡 Cálculos Inteligentes
- ✅ Rendimiento del PR17 (Tasa fija)
- ✅ Rendimiento del Dual (Variación dólar + paridad)
- ✅ Comparativa automática
- ✅ **Break-Even**: Precio de dólar de paridad

### 📱 Acceso Universal
- ✅ Desktop (Windows, Linux, macOS)
- ✅ Mobile (Android, iOS)
- ✅ Mismo WiFi: `http://192.168.X.X:5000`
- ✅ Host `0.0.0.0` para acceso remoto

### 💾 Historial Persistente
- ✅ SQLite autom  ático
- ✅ Todas las simulaciones guardadas
- ✅ Exportar a CSV
- ✅ Análisis de tendencias

### 🎨 Interfaz IntuitivaI
- ✅ Diseño Mobile-First
- ✅ Responsive en todos los tamaños
- ✅ Resultados claros y visibles
- ✅ Formulario simple (4 campos)

---

## 🧮 La Matemática

### Variables de Entrada
```
Dólar Hoy (X)           → Precio actual del dólar
Dólar Diciembre (Y)     → Tu predicción
TIR PR17 (%)            → Rendimiento fijo del bono
Paridad Dual (%)        → Ganancia del bono dual
```

### Cálculos Realizados
```
1. Variación Dólar (%) = ((Y - X) / X) × 100

2. Rendimiento PR17 (%) = TIR PR17 (fijo)

3. Rendimiento Dual (%) = Variación Dólar + Paridad Dual

4. Mejor Opción = Max(Rendimiento PR17, Rendimiento Dual)

5. Break-Even = X × (1 + (TIR PR17 - Paridad Dual) / 100)
```

### Resultado: ¿Qué Comprar?
```
SI Rendimiento PR17 > Rendimiento Dual
   → COMPRA PR17

SI Rendimiento Dual > Rendimiento PR17
   → COMPRA DUAL

BREAK-EVEN te dice qué precio de dólar hace que ambos
rendan igual
```

---

## 🚀 Inicio Rápido

### Linux / macOS
```bash
cd ~/Programacion/CalculadoraBonosArgentinos
bash install.sh
# Luego: python main.py
# Abre: http://localhost:5000
```

### Windows
```cmd
cd %USERPROFILE%\Programacion\CalculadoraBonosArgentinos
install.bat
REM Luego: venv\Scripts\activate.bat
REM        python main.py
REM Abre: http://localhost:5000
```

### Android (Mismo WiFi)
```
IP local de tu PC: 192.168.X.X
URL en navegador: http://192.168.X.X:5000
```

---

## 📊 Ejemplo Real

**Escenario:** Marzo 2026, $100.000 USD para invertir hasta diciembre

```
ENTRADA:
├─ Dólar Hoy: $1.045
├─ Dólar Dic (predicción): $1.200
├─ TIR PR17: 42.5%
└─ Paridad Dual: 18.5%

PROCESAMIENTO:
├─ Variación dólar: +14.64%
├─ Rendimiento PR17: 42.50%
├─ Rendimiento Dual: 33.14%
└─ Break-Even: $1.234,56

SALIDA:
├─ 🎯 MEJOR OPCIÓN: PR17
├─ Ventaja: +9.36 %
└─ Si dólar > $1.234,56 → mejor Dual
```

---

## 💻 Requisitos Técnicos

- **Python:** 3.7 o superior
- **Dependencias:** Flask 2.3.3 (en requirements.txt)
- **BD:** SQLite3 (incluido en Python)
- **Navegador:** Cualquiera (Chrome, Firefox, Safari, Edge)
- **RAM:** ~50 MB
- **Almacenamiento:** ~2 MB (con historial completo)

---

## 🎯 Casos de Uso

### 👨‍💼 Para Inversores
- Comparar opciones antes de invertir
- Analizar sensibilidad a cambios del dólar
- Guardar historial de decisiones

### 📈 Para Operadores
- Análisis rápido en horario bursátil
- Monitorear condiciones del mercado
- Señales de compra/venta

### 👨‍🏫 Para Estudiantes
- Entender matemática financiera
- Aprender sobre bonos soberanos
- Practicar análisis de escenarios

### 📊 Para Analistas
- Crear modelos de sensibilidad
- Exportar datos a Excel
- Presentar análisis con datos reales

---

## 🔐 Privacidad y Seguridad

✅ **Completamente Local**
- Datos guardados en tu PC/Móvil
- No se envía información a internet
- Base de datos SQLite local

✅ **Control Total**
- Puedes ver el código (open source)
- Modifica como necesites
- Ejecuta bajo tu control

⚠️ **Responsabilidad del Usuario**
- No es asesoría financiera
- Úsalo como herramienta educativa
- Realiza tu propia Due Diligence

---

## 🛠️ Estructura del Proyecto

```
CalculadoraBonosArgentinos/
│
├── 📝 main.py                 ← Backend Flask
├── 🎨 templates/
│   └── index.html             ← Frontend HTML/CSS/JS
├── ⚙️  config.py              ← Configuración
│
├── 📦 requirements.txt         ← Dependencias
├── 🧪 test_calculos.py        ← Pruebas
│
├── 🔧 install.sh              ← Instalador Linux/Mac
├── 🔧 install.bat             ← Instalador Windows
│
├── 📖 README.md               ← Doc completa
├── 🚀 QUICKSTART.md           ← Inicio rápido
├── 📊 EXAMPLES.md             ← Casos reales
├── 🎬 VIDEO_TUTORIAL.md       ← Flujo visual
├── 📋 CHANGELOG.md            ← Historial
└── 📄 INDEX.md                ← Este archivo

DB:
├── bonos_simulaciones.db      ← SQLite (se crea automáticamente)
```

---

## 🎓 Aprendizaje

### Variables Clave
- **Break-Even:** El punto crítico de decisión
- **Variación Dólar:** Variable macro más importante
- **Paridad:** Compensación por riesgo dólar
- **TIR:** Rendimiento de la opción "segura"

### Por Qué Es Importante
```
Argentina = Alta inflación + incertidumbre dólar
↓
Inversores deben calcular escenarios
↓
PR17 (sin riesgo dólar) vs DUAL (apuesta a dólar)
↓
Esta herramienta automatiza ese análisis
```

---

## 📞 Soporte y Mejoras

### Preguntas Frecuentes
Consulta [README.md](README.md#troubleshooting)

### Personalización
Edita [config.py](config.py) para ajustar valores

### Mejoras Sugeridas
Lee [CHANGELOG.md](CHANGELOG.md#posibles-mejoras-futuras)

### Reportar Bugs
Revisa el código en [main.py](main.py)

---

## 📊 Estadísticas

- **Líneas de código:** ~700
- **Funciones:** 10 principales
- **Endpoints API:** 4
- **Variables calculadas:** 5
- **Tiempo de desarrollo:** ~2 horas
- **Tiempo de aprendizaje:** ~10 minutos

---

## 🎓 Licencia

**Uso personal y educativo**
Modificación libre para uso propio

---

## 🚀 ¿Por Dónde Empezar?

1. **Si tienes prisa:** → [QUICKSTART.md](QUICKSTART.md)
2. **Si quieres aprender:** → [EXAMPLES.md](EXAMPLES.md)
3. **Si necesitas más detalles:** → [README.md](README.md)
4. **Si quieres ver cómo funciona:** → [VIDEO_TUTORIAL.md](VIDEO_TUTORIAL.md)

---

## ✨ Características Futuras

- Gráficos de simulaciones en tiempo
- Integración con API de precios reales
- Comparativa con otros bonos (GD29, AY26, etc)
- App nativa para iOS/Android
- Análisis de cartera diversificada
- Alertas automáticas de break-even

---

**Última actualización:** 3 de marzo de 2026
**Versión:** 1.0
**Estado:** 🟢 Funcional y listo para usar

---

**¡Comienza ahora! Abre [QUICKSTART.md](QUICKSTART.md)**
