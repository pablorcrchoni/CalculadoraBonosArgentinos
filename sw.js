// Service Worker para Calculadora de Bonos
const CACHE_NAME = 'calculadora-bonos-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/static/styles.css',
  '/static/app.js',
  'https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js'
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

// Estrategia: Network first, fallback to cache
self.addEventListener('fetch', (event) => {
  const { request } = event;

  // Ignorar solicitudes que no sean GET
  if (request.method !== 'GET') {
    event.respondWith(fetch(request));
    return;
  }

  // Para archivos HTML, intenta red primero, fallback a caché
  if (request.destination === 'document' || request.url.includes('.html')) {
    event.respondWith(
      fetch(request)
        .then((response) => {
          // Actualiza el caché con la respuesta nueva
          if (response.status === 200) {
            const responseToCache = response.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(request, responseToCache);
            });
          }
          return response;
        })
        .catch(() => {
          // Si falla la red, intenta servir desde caché
          return caches.match(request).then((cachedResponse) => {
            if (cachedResponse) {
              console.log('[Service Worker] Sirviendo desde caché:', request.url);
              return cachedResponse;
            }
            // Si no hay caché, devuelve una página de error offline
            return caches.match('/index.html');
          });
        })
    );
    return;
  }

  // Para otros recursos (CSS, JS, imágenes), usa estrategia cache first
  event.respondWith(
    caches.match(request)
      .then((cachedResponse) => {
        if (cachedResponse) {
          // Devuelve desde caché pero intenta actualizar en background
          fetch(request).then((response) => {
            if (response.status === 200) {
              const responseToCache = response.clone();
              caches.open(CACHE_NAME).then((cache) => {
                cache.put(request, responseToCache);
              });
            }
          }).catch(() => {
            // Fallo silencioso al actualizar
          });
          return cachedResponse;
        }

        // Si no está en caché, intenta red
        return fetch(request)
          .then((response) => {
            // Cachea la respuesta si es exitosa
            if (response.status === 200) {
              const responseToCache = response.clone();
              caches.open(CACHE_NAME).then((cache) => {
                cache.put(request, responseToCache);
              });
            }
            return response;
          })
          .catch((err) => {
            console.warn('[Service Worker] Solicitud fallida:', request.url, err);
            // Si todo falla, devuelve una respuesta de error
            return new Response('Offline - Recurso no disponible', {
              status: 503,
              statusText: 'Service Unavailable',
              headers: new Headers({
                'Content-Type': 'text/plain'
              })
            });
          });
      })
  );
});

// Manejo de mensajes desde el cliente
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

// Sincronización en background (cuando vuelve la conectividad)
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-simulaciones') {
    event.waitUntil(
      // Aquí podrías sincronizar datos guardados localmente
      Promise.resolve()
        .then(() => {
          console.log('[Service Worker] Sincronización completada');
        })
        .catch((err) => {
          console.error('[Service Worker] Error en sincronización:', err);
        })
    );
  }
});
