# CER Monitor 📊

Monitor de bonos CER soberanos argentinos (ARS y Dólar MEP).  
Detecta oportunidades de precio y arbitraje en tiempo real.

**Datos:** [data912.com](https://data912.com) — actualización cada ~20s

---

## Deploy en Vercel (5 minutos)

### 1. Subir a GitHub
```bash
git init
git add .
git commit -m "init"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/cer-monitor.git
git push -u origin main
```

### 2. Deploy en Vercel
1. Entrá a [vercel.com](https://vercel.com) y logueate con GitHub
2. Click **"Add New Project"**
3. Importá el repo `cer-monitor`
4. En **"Root Directory"** dejá `/` (raíz)
5. Click **Deploy** — listo ✅

Vercel te da una URL tipo `cer-monitor.vercel.app` accesible desde cualquier dispositivo.

---

## Estructura del proyecto

```
cer-monitor/
├── api/
│   └── market.js      ← Serverless function (proxy para data912, evita CORS)
├── public/
│   └── index.html     ← Frontend completo
├── vercel.json        ← Config de rutas
└── package.json
```

## Funcionalidades

- **Bonos CER en USD/MEP**: precio, variación, TIR, bid/ask, spread
- **Bonos CER en ARS**: precio implícito en USD, delta vs MEP
- **Detección automática de oportunidades**:
  - ⚡ Bono en oferta: cayó más del umbral configurado
  - ⇄ Arbitraje: spread entre precio ARS/MEP supera el umbral
  - ✅ Target alcanzado: precio bajó a tu nivel objetivo
- **Targets personales**: se guardan en localStorage del browser
- **Auto-refresh**: cada 60 segundos

## Notas sobre la API

Los datos de `data912.com` tienen estas características:
- Bonos con sufijo `D` (TX26D, TZX6D...): precio `c` ya en **USD directo**
- Bonos sin sufijo (TX26, TZX26...): precio `c` en **ARS**
- `pct_change`: ya es porcentaje directo (ej: `-2.75` = -2.75%)

> Solo informativo. No constituye asesoramiento financiero.
