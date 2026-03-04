# Changelog

## [1.0] - 2026-03-03

### ✨ Características Iniciales

#### Backend (Python + Flask)
- ✅ Cálculo automático de rendimientos PR17 vs Dual
- ✅ Cálculo de precio de Break-Even del dólar
- ✅ Análisis de variación porcentual del dólar
- ✅ Base de datos SQLite para almacenar historial
- ✅ API REST con endpoints: `/calcular`, `/historial`
- ✅ Validación de datos de entrada

#### Frontend (HTML + CSS + JavaScript)
- ✅ Interfaz responsive (Mobile-First)
- ✅ Formulario con 4 campos principales
- ✅ Visualización comparativa lado a lado
- ✅ Destacado del mejor activo (verde/optimizado)
- ✅ Historial con últimas simulaciones
- ✅ Exportación de datos a CSV
- ✅ Diseño gradiente moderno

#### Infraestructura
- ✅ Host `0.0.0.0` para acceso desde dispositivos móviles
- ✅ Puerto 5000 (configurable)
- ✅ Soporte multiplataforma (Windows, Linux, macOS)
- ✅ Scripts de instalación automatizada (.sh y .bat)

#### Documentación
- ✅ README.md completo con instrucciones
- ✅ config.py para personalización
- ✅ test_calculos.py para validar funciones
- ✅ .gitignore para versionamiento

---

## Posibles Mejoras Futuras

### Features
- [ ] Gráficos de simulaciones en el tiempo
- [ ] Análisis de sensibilidad (qué pasa si...)
- [ ] Simulación por rangos de dólar
- [ ] Alertas cuando se alcanza break-even
- [ ] Comparativa con otros bonos (GD29, AY26, etc)
- [ ] Integración con API de precios reales
- [ ] Autenticación y múltiples usuarios
- [ ] Exportar resultados en PDF

### Performance
- [ ] Caché de cálculos
- [ ] Compresión de respuestas
- [ ] Lazy loading del historial
- [ ] Base de datos más robusta (PostgreSQL)

### Mobile
- [ ] App nativa iOS/Android con React Native
- [ ] PWA (Progressive Web App)
- [ ] Notificaciones push

---

## Notas Técnicas

- Desarrollado con Flask 2.3.3
- Compatible con Python 3.7+
- SQLite3 para persistencia
- JavaScript vanilla (sin dependencias frontend)
- CSS custom properties para temas

---

## Contribuir

Este es un proyecto personal educativo. Siéntete libre de forkearlo y mejorarlo según tus necesidades.
