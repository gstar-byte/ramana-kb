// Service Worker for PWA - 拉玛那·马哈希知识库
const CACHE_NAME = 'ramana-kb-v3';
const OFFLINE_URL = '/index.html';

// 预缓存所有核心页面
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
  '/qa/index.html',
  // 经典著作
  '/books/be-as-you-are.html',
  '/books/gems.html',
  '/books/back-to-heart.html',
  '/books/talks.html',
  '/books/day-by-day.html',
  '/books/face-to-face.html',
  '/books/maharshi-gospel.html',
  '/books/maha-yoga.html',
  '/books/crumbs.html',
  '/books/guru-vachaka.html',
  '/books/timeless.html',
  '/books/spiritual-stories.html',
  '/books/reflections.html',
  '/books/surpassing-love.html',
  '/books/search-secret-india.html',
  '/books/collected-works.html',
  // 走向静默章节页
  '/books/be-as-you-are-ch1.html',
  '/books/be-as-you-are-ch2.html',
  '/books/be-as-you-are-ch3.html',
  '/books/be-as-you-are-ch4.html',
  '/books/be-as-you-are-ch5.html',
  '/books/be-as-you-are-ch6.html',
  '/books/be-as-you-are-ch7.html',
  '/books/be-as-you-are-ch8.html',
  '/books/be-as-you-are-ch9.html',
  // 宝钻集章节页
  '/books/gems-ch1.html',
  '/books/gems-ch2.html',
  '/books/gems-ch3.html',
  '/books/gems-ch4.html',
  '/books/gems-ch5.html',
  '/books/gems-ch6.html',
  '/books/gems-ch7.html',
  '/books/gems-ch8.html',
  '/books/gems-ch9.html',
  '/books/gems-ch10.html',
  '/books/gems-ch11.html',
  '/books/gems-ch12.html',
  '/books/gems-ch13.html',
  // 核心概念
  '/concepts/atman.html',
  '/concepts/brahman.html',
  '/concepts/whoami.html',
  '/concepts/mind.html',
  '/concepts/ego.html',
  '/concepts/thoughts.html',
  '/concepts/svasthya.html',
  '/concepts/awareness.html',
  '/concepts/jnana.html',
  '/concepts/heart.html',
  '/concepts/bhakti.html',
  '/concepts/samadhi.html',
  '/concepts/surrender.html',
  '/concepts/japa.html',
  '/concepts/silence.html',
  '/concepts/guru.html',
  '/concepts/grace.html',
  '/concepts/karma.html',
  '/concepts/maya.html',
  '/concepts/samsara.html',
  '/concepts/fate.html',
  '/concepts/freewill.html',
  '/concepts/world.html',
  '/concepts/moksha.html',
  '/concepts/jnani.html',
  '/concepts/enlightenment.html',
  '/concepts/sahaja.html',
  '/concepts/peace.html',
  '/concepts/satchidananda.html',
  '/concepts/self.html',
  '/concepts/self-enquiry.html',
  // 人物
  '/persons/ramana.html',
  '/persons/david.html',
  '/persons/venkataramana.html',
  // 方法
  '/methods/index.html',
];

// 安装事件 - 预缓存
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('[SW] Pre-caching...');
        return cache.addAll(PRECACHE_ASSETS);
      })
      .then(() => self.skipWaiting())
      .catch((err) => console.log('[SW] Pre-cache failed:', err))
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
  
  // 跳过Chrome扩展
  if (event.request.url.includes('chrome-extension')) return;

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        if (response.status === 200) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME)
            .then((cache) => cache.put(event.request, responseClone));
        }
        return response;
      })
      .catch(async () => {
        const cachedResponse = await caches.match(event.request);
        if (cachedResponse) return cachedResponse;
        
        if (event.request.headers.get('accept').includes('text/html')) {
          return caches.match(OFFLINE_URL) || caches.match('/index.html');
        }
        
        return new Response('离线不可用', {
          status: 503,
          statusText: 'Offline'
        });
      })
  );
});
