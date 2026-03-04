// Service Worker para Calculadora de Bonos (Versión Local - Solo Cliente)
const CACHE_NAME = 'bonos-v1';
const urlsToCache = [
  './',
  './index.html',
  './manifest.json'
];

// Evento de instalación: cachea los recursos
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('[Service Worker] Cacheando recursos...');
        // Intentamos cachear los URLs, pero no fallamos si alguno no está disponible
        return Promise.all(
          urlsToCache.map((url) => {
            return cache.add(url).catch((err) => {
              console.warn(`[Service Worker] No se pudo cachear ${url}:`, err);
            });
          })
        );
      })
      .catch((err) => {
        console.error('[Service Worker] Error durante install:', err);
      })
  );
  self.skipWaiting();
});

// Evento de activación: limpia cachés antiguos
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('[Service Worker] Eliminando caché antiguo:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Estrategia: Cache first, fallback to network
// Para una PWA local, prioriza el caché
self.addEventListener('fetch', (event) => {
  const { request } = event;

  // Solo cachear GET requests
  if (request.method !== 'GET') {
    return;
  }

  event.respondWith(
    caches.match(request)
      .then((response) => {
        // Si está en caché, devuélvelo
        if (response) {
          console.log('[Service Worker] Sirviendo desde caché:', request.url);
          return response;
        }

        // Si no está en caché, intenta la red
        return fetch(request)
          .then((response) => {
            // No cachear solicitudes fallidas o POST/PUT/DELETE
            if (!response || response.status !== 200 || request.method !== 'GET') {
              return response;
            }

            // Cachear respuestas exitosas
            const responseToCache = response.clone();
            caches.open(CACHE_NAME)
              .then((cache) => {
                cache.put(request, responseToCache);
              });

            return response;
          })
          .catch(() => {
            // Si todo falla y es una página HTML, intenta servir index.html
            if (request.destination === 'document' || request.url.includes('.html')) {
              return caches.match('./index.html');
            }
            // Para otros recursos, devuelve un error offline
            return new Response('Offline', {
              status: 503,
              statusText: 'Service Unavailable'
            });
          });
      })
  );
});
