# Ejemplos de Uso - Calculadora de Bonos

## 📚 Casos de Uso Reales

### Escenario 1: Duda sobre qué comprar HOY

**Tu situación:** Es marzo de 2026, tienes $100.000 USD para invertir hasta diciembre y no sabes si comprar:
- **PR17**: Bono a tasa fija del 42.5% anual
- **DUAL**: Bono ligado al dólar + 18.5% de paridad

**Datos que ingresas:**
```
Dólar Hoy:        $1.045
Dólar Diciembre:  $1.200  (tu predicción)
TIR PR17:         42.5%
Paridad Dual:     18.5%
```

**Análisis:**
- **Variación esperada del dólar:** +14.64%
- **Rendimiento PR17:** 42.50% (fijo)
- **Rendimiento DUAL:** 18.5% + 14.64% = 33.14%

**Recomendación:** 🎯 **Compra PR17** (9.36% más de ganancia)

**Break-Even:** $1.234,56
- Si el dólar llega a $1.234,56, ambos rinden igual
- Si sube más → mejor Dual
- Si sube menos → mejor PR17

---

### Escenario 2: Pesimismo extremo

**Tu situación:** Crees que el dólar puede llegar a $1.500 para diciembre

**Datos que ingresas:**
```
Dólar Hoy:        $1.045
Dólar Diciembre:  $1.500   (escenario alcista)
TIR PR17:         42.5%
Paridad Dual:     18.5%
```

**Análisis:**
- **Variación esperada del dólar:** +43.54%
- **Rendimiento PR17:** 42.50%
- **Rendimiento DUAL:** 18.5% + 43.54% = 62.04%

**Recomendación:** 🎯 **Compra DUAL** (19.54% más de ganancia)

**Break-Even:** $1.234,56 (es el mismo siempre para estos parámetros)

---

### Escenario 3: Dólar "pegado"

**Tu situación:** Crees que el dólar se va a mantener más o menos estable

**Datos que ingresas:**
```
Dólar Hoy:        $1.045
Dólar Diciembre:  $1.060   (casi sin movimiento)
TIR PR17:         42.5%
Paridad Dual:     18.5%
```

**Análisis:**
- **Variación esperada del dólar:** +1.43%
- **Rendimiento PR17:** 42.50%
- **Rendimiento DUAL:** 18.5% + 1.43% = 19.93%

**Recomendación:** 🎯 **Compra PR17** (22.57% más de ganancia)

---

## 💰 Matemática Detrás de los Cálculos

### Fórmula 1: Variación del Dólar
```
Variación % = ((Dólar_Futuro - Dólar_Actual) / Dólar_Actual) × 100

Ejemplo: ((1.200 - 1.045) / 1.045) × 100 = 14.64%
```

### Fórmula 2: Rendimiento del Dual
```
Rendimiento_Dual = Variación_Dólar + Paridad_Dual

Ejemplo: 14.64% + 18.5% = 33.14%
```

### Fórmula 3: Break-Even (Punto de Equilibrio)
```
Dólar_BreakEven = Dólar_Actual × (1 + (TIR_PR17 - Paridad_Dual) / 100)

Ejemplo:
1.045 × (1 + (42.5 - 18.5) / 100)
= 1.045 × (1 + 0.24)
= 1.045 × 1.24
= $1.295.80
```

---

## 📊 Tabla Comparativa

| Escenario | Dólar Dic | Var % | PR17 | DUAL | Ganancia | % Ventaja |
|-----------|-----------|-------|------|------|----------|-----------|
| Pessimista | $1500 | +43.54% | 42.50% | 62.04% | DUAL | +19.54% |
| Realista | $1200 | +14.64% | 42.50% | 33.14% | PR17 | +9.36% |
| Optimista | $1060 | +1.43% | 42.50% | 19.93% | PR17 | +22.57% |
| Estancado | $1045 | 0% | 42.50% | 18.50% | PR17 | +24.00% |

---

## 🎯 Cómo Encontrar tu Predicción del Dólar

### Método 1: Análisis Fundamental
- Revisar inflación diferencial ARG vs USA
- Reservas del BCRA y flujo de efectivo
- Balanza comercial y deuda externa
- Expectativas de elecciones

### Método 2: Análisis Técnico
- Gráficos históricos en Trading View
- Niveles de soporte y resistencia
- Promedio móvil de tendencias

### Método 3: Consenso de Mercado
- CER (Coeficiente de Estabilización de Referencia)
- Forwards de dólar futures
- Estimaciones de bancos locales

### Método 4: Consultar Fuentes
- BCRA.gob.ar
- MERVAL
- Análisis de consultoras
- Opinion de economistas

---

## 💡 Tips de Uso

✅ **Ejecuta varias simulaciones:**
- Ingresa diferentes predicciones de dólar
- Encuentra tu punto de indiferencia (break-even)
- Visualiza en qué escenarios gana cada activo

✅ **Usa el historial:**
- Guarda tus simulaciones
- Compara predicciones que hiciste hace tiempo
- Aprende de tus errores

✅ **Considera márgenes de seguridad:**
- El dólar es impredecible
- Agrega un +10-15% a tus predicciones "normales"
- Sé conservador con escenarios muy optimistas

✅ **Revisa periódicamente:**
- Cada mes recalcula según nuevas variables
- Ajusta TIR y paridad con precios reales del mercado
- Revisa si tus predicciones siguen siendo válidas

---

## ⚠️ Aclaraciones Importantes

1. **Esto NO es asesoría financiera** - son cálculos matemáticos puros
2. **Los rendimientos futuros no están garantizados** - pueden cambiar
3. **El dólar es impredecible** - las variables macroeconómicas cambian constantemente
4. **Riesgo soberano:** Argentina puede defaultear nuevamente
5. **Riesgo de mercado:** Los bonos pueden bajar de precio

**Usa esta calculadora como herramienta educativa para entender las matemáticas, no como asesoría de inversión.**

---

## 📞 ¿Preguntas?

Modifica los parámetros en `config.py` para ajustar valores por defecto según tus predicciones actuales.
