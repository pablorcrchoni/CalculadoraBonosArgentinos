// api/market.js — Vercel Serverless Function
// Actua como proxy para data912.com (evita CORS desde el browser)

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Cache-Control', 's-maxage=20, stale-while-revalidate');

  try {
    const [mepRes, bondsRes, notesRes] = await Promise.all([
      fetch('https://data912.com/live/mep'),
      fetch('https://data912.com/live/arg_bonds'),
      fetch('https://data912.com/live/arg_notes'),
    ]);

    const [mep, bonds, notes] = await Promise.all([
      mepRes.json(),
      bondsRes.json(),
      notesRes.json(),
    ]);

    res.status(200).json({ mep, bonds, notes });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}
