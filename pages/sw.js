// Ramana Maharshi Knowledge Base - Service Worker
const CACHE_NAME = 'ramana-kb-v1';
const ASSETS = [
  '/',
  '/index.html',
  '/books/index.html',
  '/books/be-as-you-are.html',
  '/books/gems.html',
  '/concepts/index.html',
  '/methods/index.html',
  '/persons/index.html',
  '/qa/index.html',
  '/graph.html',
  '/styles.css',
  '/manifest.json',
  '/icons/icon-192.png',
  '/icons/icon-512.png'
];

// Install: cache core assets
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS);
    }).then(() => self.skipWaiting())
  );
});

// Activate: clean old caches
self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k))
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch: network-first, fallback to cache
self.addEventListener('fetch', (e) => {
  // Skip non-GET and cross-origin requests (except Vercel CDN)
  if (e.request.method !== 'GET') return;
  if (!e.request.url.startsWith(self.location.origin) &&
      !e.request.url.includes('vercel.app')) return;

  e.respondWith(
    fetch(e.request)
      .then((res) => {
        // Cache successful responses
        if (res.status === 200) {
          const clone = res.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(e.request, clone));
        }
        return res;
      })
      .catch(() => {
        // Fallback to cache
        return caches.match(e.request);
      })
  );
});
