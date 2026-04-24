// Ramana Maharshi Knowledge Base - Service Worker v9
const CACHE_NAME = 'ramana-kb-v10';
// 只预缓存核心资源，避免安装失败
const CORE_ASSETS = [
  '/',
  '/styles.css',
  '/script.js',
  '/search.js',
  '/pwa-analytics.js',
  '/manifest.json',
  '/sw.js'
];

// Install: 逐个缓存，失败不影响其他，SW 必定安装成功
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(async (cache) => {
      console.log('[SW] Installing v9...');
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
    fetch(request, {
      cache: 'no-cache', // 确保每次都请求最新内容
      credentials: 'same-origin'
    })
      .then((resp) => {
        // 成功响应则缓存（静态资源和HTML）
        if (resp.ok) {
          const clone = resp.clone();
          caches.open(CACHE_NAME).then((cache) => {
            // 只缓存静态资源和HTML
            if (url.pathname.endsWith('/') || 
                url.pathname.endsWith('.css') || 
                url.pathname.endsWith('.js') ||
                url.pathname.endsWith('.png') ||
                url.pathname.endsWith('.svg') ||
                url.pathname.endsWith('.ico')) {
              cache.put(request, clone);
            }
          });
        }
        return resp;
      })
      .catch(() => {
        // 网络失败 → 缓存
        return caches.match(request).then((cached) => {
          if (cached) {
            console.log('[SW] Serving from cache:', request.url);
            return cached;
          }
          // 缓存也没有 → 返回离线页面
          return new Response('网络连接已断开，请检查网络连接后重试', {
            status: 503,
            headers: { 'Content-Type': 'text/plain; charset=utf-8' }
          });
        });
      })
  );
});
