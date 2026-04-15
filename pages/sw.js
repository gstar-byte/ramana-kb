// Ramana Maharshi Knowledge Base - Service Worker
const CACHE_NAME = 'ramana-kb-v3';
const ASSETS = [
  '/',
  '/index.html',
  '/graph.html',
  '/manifest.json',
  '/styles.css',
  '/script.js',
  '/search.js',
  '/sw.js',
  
  // Books
  '/books/back-to-heart-ch1.html',
  '/books/back-to-heart-ch2.html',
  '/books/back-to-heart-ch3.html',
  '/books/back-to-heart-ch4.html',
  '/books/back-to-heart-ch5.html',
  '/books/back-to-heart.html',
  '/books/be-as-you-are-ch1.html',
  '/books/be-as-you-are-ch2.html',
  '/books/be-as-you-are-ch3.html',
  '/books/be-as-you-are-ch4.html',
  '/books/be-as-you-are-ch5.html',
  '/books/be-as-you-are-ch6.html',
  '/books/be-as-you-are-ch7.html',
  '/books/be-as-you-are-ch8.html',
  '/books/be-as-you-are-ch9.html',
  '/books/be-as-you-are.html',
  '/books/collected-works.html',
  '/books/crumbs-ch1.html',
  '/books/crumbs-ch2.html',
  '/books/crumbs-ch3.html',
  '/books/crumbs-ch4.html',
  '/books/crumbs.html',
  '/books/day-by-day.html',
  '/books/face-to-face.html',
  '/books/gems-ch1.html',
  '/books/gems-ch10.html',
  '/books/gems-ch11.html',
  '/books/gems-ch12.html',
  '/books/gems-ch13.html',
  '/books/gems-ch2.html',
  '/books/gems-ch3.html',
  '/books/gems-ch4.html',
  '/books/gems-ch5.html',
  '/books/gems-ch6.html',
  '/books/gems-ch7.html',
  '/books/gems-ch8.html',
  '/books/gems-ch9.html',
  '/books/gems.html',
  '/books/index.html',
  '/books/maha-yoga.html',
  '/books/maharshi-gospel.html',
  '/books/reflections-ch1.html',
  '/books/reflections-ch2.html',
  '/books/reflections.html',
  '/books/search-secret-india.html',
  '/books/spiritual-stories-ch1.html',
  '/books/spiritual-stories-ch2.html',
  '/books/spiritual-stories.html',
  '/books/surpassing-love-ch1.html',
  '/books/surpassing-love-ch2.html',
  '/books/surpassing-love.html',
  '/books/talks-ch1.html',
  '/books/talks-ch2.html',
  '/books/talks-ch3.html',
  '/books/talks-ch4.html',
  '/books/talks-ch5.html',
  '/books/talks-ch6.html',
  '/books/talks-ch7.html',
  '/books/talks-ch8.html',
  '/books/talks.html',
  '/books/teachings-ch1.html',
  '/books/teachings-ch2.html',
  '/books/teachings.html',
  '/books/timeless-ch1.html',
  '/books/timeless-ch2.html',
  '/books/timeless-ch3.html',
  '/books/timeless-ch4.html',
  '/books/timeless-ch5.html',
  '/books/timeless-ch6.html',
  '/books/timeless.html',
  
  // Concepts
  '/concepts/_template.html',
  '/concepts/atman.html',
  '/concepts/awareness.html',
  '/concepts/bhakti.html',
  '/concepts/brahman.html',
  '/concepts/ego.html',
  '/concepts/enlightenment.html',
  '/concepts/fate.html',
  '/concepts/freewill.html',
  '/concepts/grace.html',
  '/concepts/guru.html',
  '/concepts/heart.html',
  '/concepts/index.html',
  '/concepts/japa.html',
  '/concepts/jnana.html',
  '/concepts/jnani.html',
  '/concepts/karma.html',
  '/concepts/maya.html',
  '/concepts/mind.html',
  '/concepts/moksha.html',
  '/concepts/peace.html',
  '/concepts/sahaja.html',
  '/concepts/samadhi.html',
  '/concepts/samsara.html',
  '/concepts/satchidananda.html',
  '/concepts/self-enquiry.html',
  '/concepts/self.html',
  '/concepts/silence.html',
  '/concepts/surrender.html',
  '/concepts/svasthya.html',
  '/concepts/thoughts.html',
  '/concepts/whoami.html',
  '/concepts/world.html',
  
  // Methods
  '/methods/index.html',
  
  // Persons
  '/persons/david.html',
  '/persons/index.html',
  '/persons/ramana.html',
  '/persons/venkataramana.html',
  
  // QA
  '/qa/index.html',
  '/qa/new_qa_content.html',
  '/qa/qa-1.html',
  '/qa/qa-10.html',
  '/qa/qa-11.html',
  '/qa/qa-12.html',
  '/qa/qa-13.html',
  '/qa/qa-14.html',
  '/qa/qa-15.html',
  '/qa/qa-16.html',
  '/qa/qa-17.html',
  '/qa/qa-18.html',
  '/qa/qa-19.html',
  '/qa/qa-2.html',
  '/qa/qa-20.html',
  '/qa/qa-3.html',
  '/qa/qa-4.html',
  '/qa/qa-5.html',
  '/qa/qa-6.html',
  '/qa/qa-7.html',
  '/qa/qa-8.html',
  '/qa/qa-9.html',
  
  // Icons
  '/icons/icon-128.png',
  '/icons/icon-144.png',
  '/icons/icon-152.png',
  '/icons/icon-192.png',
  '/icons/icon-384.png',
  '/icons/icon-512.png',
  '/icons/icon-72.png',
  '/icons/icon-96.png'
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

// Fetch: cache-first strategy for offline reliability
self.addEventListener('fetch', (e) => {
  // Skip non-GET and cross-origin requests (except Vercel CDN)
  if (e.request.method !== 'GET') return;
  if (!e.request.url.startsWith(self.location.origin) &&
      !e.request.url.includes('vercel.app')) return;

  e.respondWith(
    caches.match(e.request)
      .then((cachedResponse) => {
        // If found in cache, return it immediately
        if (cachedResponse) {
          // Update cache in background
          fetch(e.request)
            .then((res) => {
              if (res.status === 200) {
                const clone = res.clone();
                caches.open(CACHE_NAME).then((cache) => cache.put(e.request, clone));
              }
            })
            .catch(() => {
              // Network error, keep using cache
            });
          return cachedResponse;
        }
        
        // If not in cache, fetch from network
        return fetch(e.request)
          .then((res) => {
            // Cache successful responses
            if (res.status === 200) {
              const clone = res.clone();
              caches.open(CACHE_NAME).then((cache) => cache.put(e.request, clone));
            }
            return res;
          })
          .catch(() => {
            // Network error, try to find similar resource in cache
            const url = new URL(e.request.url);
            if (url.pathname.endsWith('/')) {
              return caches.match(url.pathname + 'index.html');
            }
            return caches.match('/'); // Fallback to home page
          });
      })
  );
});
