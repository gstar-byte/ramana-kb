// Service Worker for PWA - 拉玛那·马哈希知识库
const CACHE_NAME = 'ramana-kb-v1';
const OFFLINE_URL = '/index.html';

// 需要缓存的资源
const PRECACHE_ASSETS = [
  '/',
  '/index.html',
  '/graph.html',
  '/styles.css',
  '/manifest.json',
  // 索引页面
  '/books/index.html',
  '/concepts/index.html',
  '/methods/index.html',
  '/persons/index.html',
  // 核心书籍页面
  '/books/be-as-you-are.html',
  '/books/gems.html',
  '/books/talks.html',
  '/books/back-to-heart.html',
  '/books/day-by-day.html',
  // 核心概念页面
  '/concepts/atman.html',
  '/concepts/whoami.html',
  '/concepts/mind.html',
  '/concepts/moksha.html',
  '/concepts/grace.html',
  // 人物页面
  '/persons/ramana.html',
  '/persons/david.html',
];

// 安装事件 - 预缓存核心资源
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('[SW] Pre-caching core assets');
        return cache.addAll(PRECACHE_ASSETS);
      })
      .then(() => self.skipWaiting())
  );
});

// 激活事件 - 清理旧缓存
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('[SW] Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// 获取事件 - 网络优先，回退缓存
self.addEventListener('fetch', (event) => {
  // 跳过非GET请求
  if (event.request.method !== 'GET') return;
  
  // 跳过跨域请求
  if (!event.request.url.startsWith(self.location.origin)) return;
  
  // 跳过Chrome扩展等
  if (event.request.url.includes('chrome-extension')) return;

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        // 如果成功响应，克隆并缓存
        if (response.status === 200) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME)
            .then((cache) => {
              cache.put(event.request, responseClone);
            });
        }
        return response;
      })
      .catch(async () => {
        // 离线时尝试从缓存获取
        const cachedResponse = await caches.match(event.request);
        if (cachedResponse) {
          return cachedResponse;
        }
        
        // 对于HTML页面，返回离线页面
        if (event.request.headers.get('accept').includes('text/html')) {
          const offlineResponse = await caches.match(OFFLINE_URL);
          if (offlineResponse) {
            return offlineResponse;
          }
        }
        
        // 返回错误响应
        return new Response('离线', {
          status: 503,
          statusText: 'Service Unavailable'
        });
      })
  );
});

// 推送通知（可选）
self.addEventListener('push', (event) => {
  if (event.data) {
    const data = event.data.json();
    self.registration.showNotification(data.title, {
      body: data.body,
      icon: '/icon-192.png',
      badge: '/badge-72.png'
    });
  }
});
