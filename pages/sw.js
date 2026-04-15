// Ramana Maharshi Knowledge Base - Service Worker
const CACHE_NAME = 'ramana-kb-v4';
const CORE_ASSETS = [
  '/',
  '/index.html',
  '/graph.html',
  '/styles.css',
  '/script.js',
  '/search.js',
  '/manifest.json',
  '/sw.js',
  '/books/index.html',
  '/concepts/index.html',
  '/methods/index.html',
  '/persons/index.html',
  '/qa/index.html'
];

// Install: cache core assets only
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(CORE_ASSETS);
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

// Fetch: network-first with cache fallback
self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  if (!e.request.url.startsWith(self.location.origin) &&
      !e.request.url.includes('vercel.app')) return;

  e.respondWith(
    fetch(e.request)
      .then((res) => {
        if (res && res.status === 200) {
          const clone = res.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(e.request, clone).catch(err => console.log('Cache put error:', err));
          });
        }
        return res;
      })
      .catch((err) => {
        console.log('Network error, falling back to cache:', err);
        // Try to match both the original request and the clean URL version
        return caches.match(e.request).then((cached) => {
          if (cached) return cached;
          
          // Try clean URL version (without .html)
          if (e.request.url.endsWith('.html')) {
            const cleanUrl = e.request.url.replace(/\.html$/, '');
            return caches.match(cleanUrl).then((cleanCached) => {
              return cleanCached || caches.match('/');
            });
          }
          
          // Try .html version if clean URL
          if (!e.request.url.endsWith('.html') && !e.request.url.endsWith('/')) {
            const htmlUrl = e.request.url + '.html';
            return caches.match(htmlUrl).then((htmlCached) => {
              return htmlCached || caches.match('/');
            });
          }
          
          return caches.match('/');
        });
      })
  );
});
