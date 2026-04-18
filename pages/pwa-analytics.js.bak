/**
 * PWA 安装事件跟踪
 * 监听 beforeinstallprompt 事件并发送到 GA4
 */

let deferredPrompt = null;

// 监听 beforeinstallprompt 事件
window.addEventListener('beforeinstallprompt', (e) => {
    console.log('PWA install prompt triggered');
    e.preventDefault();
    deferredPrompt = e;
    
    // 发送到 GA4 - 用户触发了安装提示
    if (typeof gtag !== 'undefined') {
        gtag('event', 'pwa_install_prompt_shown', {
            'event_category': 'PWA',
            'event_label': 'beforeinstallprompt'
        });
    }
});

// 监听 appinstalled 事件 - 用户成功安装
window.addEventListener('appinstalled', (e) => {
    console.log('PWA installed successfully');
    
    // 发送到 GA4 - 安装成功
    if (typeof gtag !== 'undefined') {
        gtag('event', 'pwa_installed', {
            'event_category': 'PWA',
            'event_label': 'appinstalled',
            'value': 1
        });
    }
    
    // 清理
    deferredPrompt = null;
});

// 如果页面加载时已经可以安装，记录
if (window.matchMedia('(display-mode: standalone)').matches) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'pwa_already_installed', {
            'event_category': 'PWA',
            'event_label': 'standalone_mode'
        });
    }
}
