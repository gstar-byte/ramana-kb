// Ramana Maharshi Knowledge Base - Service Worker v6
const CACHE_NAME = 'ramana-kb-v6';
const CORE_ASSETS = [
  '/','/index.html','/graph.html','/sitemap.html',
  '/styles.css','/script.js','/search.js','/pwa-analytics.js','/manifest.json','/sw.js',
  '/books/','/books/index.html',
  '/books/back-to-heart.html',
  '/books/back-to-heart-ch1.html','/books/back-to-heart-ch2.html','/books/back-to-heart-ch3.html',
  '/books/back-to-heart-ch4.html','/books/back-to-heart-ch5.html',
  '/books/be-as-you-are.html',
  '/books/be-as-you-are-ch1.html','/books/be-as-you-are-ch2.html','/books/be-as-you-are-ch3.html',
  '/books/be-as-you-are-ch4.html','/books/be-as-you-are-ch5.html','/books/be-as-you-are-ch6.html',
  '/books/be-as-you-are-ch7.html','/books/be-as-you-are-ch8.html','/books/be-as-you-are-ch9.html',
  '/books/collected-works.html',
  '/books/crumbs.html',
  '/books/crumbs-ch1.html','/books/crumbs-ch2.html','/books/crumbs-ch3.html','/books/crumbs-ch4.html',
  '/books/day-by-day.html',
  '/books/face-to-face.html',
  '/books/gems.html',
  '/books/gems-ch1.html','/books/gems-ch2.html','/books/gems-ch3.html','/books/gems-ch4.html',
  '/books/gems-ch5.html','/books/gems-ch6.html','/books/gems-ch7.html','/books/gems-ch8.html',
  '/books/gems-ch9.html','/books/gems-ch10.html','/books/gems-ch11.html','/books/gems-ch12.html','/books/gems-ch13.html',
  '/books/maha-yoga.html',
  '/books/maharshi-gospel.html',
  '/books/reflections.html',
  '/books/reflections-ch1.html','/books/reflections-ch2.html',
  '/books/search-secret-india.html',
  '/books/spiritual-stories.html',
  '/books/spiritual-stories-ch1.html','/books/spiritual-stories-ch2.html',
  '/books/surpassing-love.html',
  '/books/surpassing-love-ch1.html','/books/surpassing-love-ch2.html',
  '/books/talks.html',
  '/books/talks-ch1.html','/books/talks-ch2.html','/books/talks-ch3.html','/books/talks-ch4.html',
  '/books/talks-ch5.html','/books/talks-ch6.html','/books/talks-ch7.html','/books/talks-ch8.html',
  '/books/teachings.html',
  '/books/teachings-ch1.html','/books/teachings-ch2.html',
  '/books/timeless.html',
  '/books/timeless-ch1.html','/books/timeless-ch2.html','/books/timeless-ch3.html',
  '/books/timeless-ch4.html','/books/timeless-ch5.html','/books/timeless-ch6.html',
  '/concepts/','/concepts/index.html',
  '/concepts/atman.html','/concepts/awareness.html','/concepts/bhakti.html','/concepts/brahman.html',
  '/concepts/ego.html','/concepts/enlightenment.html','/concepts/fate.html','/concepts/freewill.html',
  '/concepts/grace.html','/concepts/guru.html','/concepts/heart.html','/concepts/japa.html',
  '/concepts/jnana.html','/concepts/jnani.html','/concepts/karma.html','/concepts/maya.html',
  '/concepts/mind.html','/concepts/moksha.html','/concepts/peace.html','/concepts/sahaja.html',
  '/concepts/samadhi.html','/concepts/samsara.html','/concepts/satchidananda.html','/concepts/self.html',
  '/concepts/self-enquiry.html','/concepts/silence.html','/concepts/surrender.html',
  '/concepts/svasthya.html','/concepts/thoughts.html','/concepts/whoami.html','/concepts/world.html',
  '/methods/','/methods/index.html',
  '/persons/','/persons/index.html',
  '/persons/david.html','/persons/ramana.html','/persons/venkataramana.html',
  '/qa/','/qa/index.html',
  '/qa/qa-1.html','/qa/qa-2.html','/qa/qa-3.html','/qa/qa-4.html','/qa/qa-5.html',
  '/qa/qa-6.html','/qa/qa-7.html','/qa/qa-8.html','/qa/qa-9.html','/qa/qa-10.html',
  '/qa/qa-11.html','/qa/qa-12.html','/qa/qa-13.html','/qa/qa-14.html','/qa/qa-15.html',
  '/qa/qa-16.html','/qa/qa-17.html','/qa/qa-18.html','/qa/qa-19.html','/qa/qa-20.html'
];

// Install: 逐个缓存，失败不影响其他，SW 必定安装成功
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(async (cache) => {
      console.log('[SW] Installing v6...');
      for (const url of CORE_ASSETS) {
        try {
          const resp = await fetch(url);
          if (resp.ok) {
            await cache.put(url, resp.clone());
          }
        } catch (err) {
          console.warn('[SW] Skip:', url);
        }
      }
      console.log('[SW] Install complete');
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

// Fetch: network-first for HTML (有网时优先网络，离线时用缓存)
self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  const src = self.location.origin;
  if (!e.request.url.startsWith(src) && !e.request.url.includes('vercel.app')) return;

  const url = new URL(e.request.url);
  const isHtml = url.pathname.endsWith('.html') || url.pathname === '/' || url.pathname.endsWith('/');

  if (isHtml) {
    // HTML: network-first，失败时用缓存，再失败时用首页
    e.respondWith(
      fetch(e.request)
        .then((res) => {
          if (res && res.status === 200) {
            const clone = res.clone();
            caches.open(CACHE_NAME).then((c) => c.put(e.request, clone));
          }
          return res;
        })
        .catch(() => caches.match(e.request))
        .then((cached) => cached || caches.match('/index.html'))
    );
  } else {
    // 静态资源: cache-first，失败时用网络
    e.respondWith(
      caches.match(e.request).then((cached) => {
        if (cached) return cached;
        return fetch(e.request).then((res) => {
          if (res && res.status === 200) {
            const clone = res.clone();
            caches.open(CACHE_NAME).then((c) => c.put(e.request, clone));
          }
          return res;
        });
      })
    );
  }
});
