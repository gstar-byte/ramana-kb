// Ramana Maharshi Knowledge Base - Service Worker v7
const CACHE_NAME = 'ramana-kb-v7';
const CORE_ASSETS = [
  '/',
  '/index/',
  '/graph/',
  '/sitemap/',
  '/styles.css',
  '/script.js',
  '/search.js',
  '/pwa-analytics.js',
  '/manifest.json',
  '/sw.js',
  // Books
  '/books/',
  '/books/index/',
  '/books/be-as-you-are/',
  '/books/be-as-you-are-ch1/',
  '/books/be-as-you-are-ch2/',
  '/books/be-as-you-are-ch3/',
  '/books/be-as-you-are-ch4/',
  '/books/be-as-you-are-ch5/',
  '/books/be-as-you-are-ch6/',
  '/books/be-as-you-are-ch7/',
  '/books/be-as-you-are-ch8/',
  '/books/be-as-you-are-ch9/',
  '/books/gems/',
  '/books/gems-ch1/',
  '/books/gems-ch2/',
  '/books/gems-ch3/',
  '/books/gems-ch4/',
  '/books/gems-ch5/',
  '/books/gems-ch6/',
  '/books/gems-ch7/',
  '/books/gems-ch8/',
  '/books/gems-ch9/',
  '/books/gems-ch10/',
  '/books/gems-ch11/',
  '/books/gems-ch12/',
  '/books/gems-ch13/',
  '/books/back-to-heart/',
  '/books/back-to-heart-ch1/',
  '/books/back-to-heart-ch2/',
  '/books/back-to-heart-ch3/',
  '/books/back-to-heart-ch4/',
  '/books/back-to-heart-ch5/',
  '/books/talks/',
  '/books/talks-ch1/',
  '/books/talks-ch2/',
  '/books/talks-ch3/',
  '/books/talks-ch4/',
  '/books/talks-ch5/',
  '/books/talks-ch6/',
  '/books/talks-ch7/',
  '/books/talks-ch8/',
  '/books/day-by-day/',
  '/books/face-to-face/',
  '/books/search-secret-india/',
  '/books/collected-works/',
  '/books/maha-yoga/',
  '/books/maharshi-gospel/',
  '/books/reflections/',
  '/books/reflections-ch1/',
  '/books/reflections-ch2/',
  '/books/spiritual-stories/',
  '/books/spiritual-stories-ch1/',
  '/books/spiritual-stories-ch2/',
  '/books/surpassing-love/',
  '/books/surpassing-love-ch1/',
  '/books/surpassing-love-ch2/',
  '/books/teachings/',
  '/books/teachings-ch1/',
  '/books/teachings-ch2/',
  '/books/timeless/',
  '/books/timeless-ch1/',
  '/books/timeless-ch2/',
  '/books/timeless-ch3/',
  '/books/timeless-ch4/',
  '/books/timeless-ch5/',
  '/books/timeless-ch6/',
  '/books/crumbs/',
  '/books/crumbs-ch1/',
  '/books/crumbs-ch2/',
  '/books/crumbs-ch3/',
  '/books/crumbs-ch4/',
  // Concepts
  '/concepts/',
  '/concepts/index/',
  '/concepts/whoami/',
  '/concepts/mind/',
  '/concepts/ego/',
  '/concepts/atman/',
  '/concepts/brahman/',
  '/concepts/moksha/',
  '/concepts/grace/',
  '/concepts/silence/',
  '/concepts/surrender/',
  '/concepts/self-enquiry/',
  '/concepts/japa/',
  '/concepts/samadhi/',
  '/concepts/karma/',
  '/concepts/samsara/',
  '/concepts/maya/',
  '/concepts/satchidananda/',
  '/concepts/enlightenment/',
  '/concepts/bhakti/',
  '/concepts/jnana/',
  '/concepts/jnani/',
  '/concepts/awareness/',
  '/concepts/heart/',
  '/concepts/fate/',
  '/concepts/freewill/',
  '/concepts/guru/',
  '/concepts/self/',
  '/concepts/sahaja/',
  '/concepts/peace/',
  '/concepts/thoughts/',
  '/concepts/svasthya/',
  '/concepts/world/',
  '/concepts/_template/',
  // Methods
  '/methods/',
  '/methods/index/',
  // Persons
  '/persons/',
  '/persons/index/',
  '/persons/ramana/',
  '/persons/david/',
  '/persons/venkataramana/',
  // QA
  '/qa/',
  '/qa/index/',
  '/qa/qa-1/',
  '/qa/qa-2/',
  '/qa/qa-3/',
  '/qa/qa-4/',
  '/qa/qa-5/',
  '/qa/qa-6/',
  '/qa/qa-7/',
  '/qa/qa-8/',
  '/qa/qa-9/',
  '/qa/qa-10/',
  '/qa/qa-11/',
  '/qa/qa-12/',
  '/qa/qa-13/',
  '/qa/qa-14/',
  '/qa/qa-15/',
  '/qa/qa-16/',
  '/qa/qa-17/',
  '/qa/qa-18/',
  '/qa/qa-19/',
  '/qa/qa-20/',
];

// Install: 逐个缓存，失败不影响其他，SW 必定安装成功
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(async (cache) => {
      console.log('[SW] Installing v7...');
      for (const url of CORE_ASSETS) {
        try {
          const resp = await fetch(url);
          if (resp.ok) {
            await cache.put(url, resp.clone());
          }
        } catch (err) {
          console.warn('[SW] Failed to cache:', url, err.message);
        }
      }
      console.log('[SW] Install complete, skipping wait');
      return self.skipWaiting();
    })
  );
});

// Activate: 删除旧缓存
self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => {
          console.log('[SW] Deleting old cache:', key);
          return caches.delete(key);
        })
      );
    }).then(() => {
      console.log('[SW] Activate complete');
      return self.clients.claim();
    })
  );
});

// Fetch: 网络优先，降级到缓存
self.addEventListener('fetch', (e) => {
  const { request } = e;
  const url = new URL(request.url);

  // 跳过非 GET / 非同域 / chrome-extension 请求
  if (request.method !== 'GET' || url.origin !== self.location.origin ||
      url.protocol === 'chrome-extension:') {
    return;
  }

  // Google Analytics 请求跳过
  if (url.hostname === 'www.google-analytics.com' ||
      url.hostname === 'analytics.google.com') {
    return;
  }

  e.respondWith(
    fetch(request)
      .then((resp) => {
        // 成功响应则缓存（仅同域 HTML）
        if (resp.ok && url.pathname.endsWith('/')) {
          const clone = resp.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
        }
        return resp;
      })
      .catch(() => {
        // 网络失败 → 缓存
        return caches.match(request).then((cached) => {
          if (cached) return cached;
          // SPA fallback
          if (url.pathname.startsWith('/books/') ||
              url.pathname.startsWith('/concepts/') ||
              url.pathname.startsWith('/persons/') ||
              url.pathname.startsWith('/methods/') ||
              url.pathname.startsWith('/qa/')) {
            return caches.match('/');
          }
          return new Response('Offline - 请检查网络连接', { status: 503 });
        });
      })
  );
});
