# 🚀 Guía Rápida - Start in 2 Minutes

## Linux / macOS (Terminal)

```bash
# 1. Ir a la carpeta del proyecto
cd ~/Programacion/CalculadoraBonosArgentinos

# 2. Ejecutar instalador
bash install.sh

# 3. Cuando termine, ejecutar:
python main.py

# 4. Abrir navegador
# http://localhost:5000
```

---

## Windows (Command Prompt)

```cmd
# 1. Ir a la carpeta del proyecto
cd %USERPROFILE%\Programacion\CalculadoraBonosArgentinos

# 2. Ejecutar instalador
install.bat

# 3. Cuando termine, en otra terminal:
venv\Scripts\activate.bat
python main.py

# 4. Abrir navegador
# http://localhost:5000
```

---

## Desde Android (Mismo WiFi)

1. **Encuentra tu IP local:**

   **Linux/Mac:**
   ```bash
   ifconfig | grep "inet " | grep -v 127
   ```

   **Windows:**
   ```cmd
   ipconfig
   ```

2. **En el navegador de tu teléfono:**
   ```
   http://192.168.X.X:5000
   ```
   (Reemplaza X.X con tu IP)

3. **Prueba:** Ingresa valores y hace clic en "Calcular"

---

## Estructura de Archivos

```
CalculadoraBonosArgentinos/
├── main.py                 # 💾 Backend (Flask + SQLite)
├── templates/
│   └── index.html          # 🎨 Frontend (HTML/CSS/JS)
├── requirements.txt        # 📦 Dependencias Python
├── config.py              # ⚙️ Configuración personalizable
├── test_calculos.py       # 🧪 Pruebas y validación
├── install.sh             # 🔧 Instalador Linux/Mac
├── install.bat            # 🔧 Instalador Windows
├── README.md              # 📖 Documentación completa
├── EXAMPLES.md            # 📊 Casos de uso reales
├── CHANGELOG.md           # 📝 Historial de cambios
└── .gitignore            # Git config
```

---

## Primeros Pasos

### 1️⃣ Instala dependencias
```bash
pip install -r requirements.txt
```

### 2️⃣ Ejecuta la app
```bash
python main.py
```

### 3️⃣ Abre en navegador
```
http://localhost:5000
```

### 4️⃣ Ingresa tus predicciones
- **Dólar Hoy:** Precio actual
- **Dólar Diciembre:** Tu predicción
- **TIR PR17:** Tasa del bono (consulta el mercado)
- **Paridad Dual:** Ganancia del Dual (consulta el mercado)

### 5️⃣ Haz clic en "Calcular"

---

## Problemas Comunes

### ❌ "Port 5000 is already in use"
```bash
# Opción 1: Cambiar puerto en main.py (línea final)
# Cambiar: app.run(host='0.0.0.0', port=5000)
# Por:     app.run(host='0.0.0.0', port=8000)

# Opción 2: Matar el proceso (Linux/Mac)
lsof -i :5000 | grep -v PID | awk '{print $2}' | xargs kill -9
```

### ❌ "Module not found: Flask"
```bash
# Instala manualmente
pip install Flask==2.3.3
```

### ❌ "No puedo acceder desde Android"
- Verifica que ambos en mismo WiFi
- Asegúrate de IP correcta
- Prueba desactivar firewall temporalmente

### ❌ "Database error"
```bash
# Elimina la BD antigua y deja que se cree nueva
rm bonos_simulaciones.db
python main.py
```

---

## Configuración Personalizada

Edita `config.py` para:
- Cambiar valores por defecto
- Modificar límites de validación
- Agregar nuevos bonos
- Habilitar/deshabilitar características

---

## Próximos Pasos

✅ Prueba con tus propios números
✅ Exporta historial a CSV
✅ Modifica `config.py` según necesites
✅ Lee [EXAMPLES.md](EXAMPLES.md) para casos reales
✅ Consulta [README.md](README.md) para documentación completa

---

## 💬 Notas

- **Base de datos:** SQLite (`bonos_simulaciones.db`) - se crea automáticamente
- **Historial:** Se guarda cada cálculo automáticamente
- **Privacidad:** Todo local en tu PC/móvil, sin enviar datos a internet
- **Responsabilidad:** Esto es una herramienta educativa, NO asesoría financiera

---

**¿Listo? ¡Abre una terminal y comienza! 🚀**
