// Cache everything static

var cacheName = 'hpmor__VERSION__';
var files2cache = [
__FILES_TO_CACHE__
];

self.addEventListener('install', function(e) {
    console.log('installing cache', e);
    e.waitUntil(
        caches.open(cacheName).then(function(cache) {
            return cache.addAll(files2cache);
        })
    );
});

// If request matches something in cache - return it from cache
// otherwise do actual request
self.addEventListener('fetch', function(event) {
    console.log('fetch', event.request);
    event.respondWith(
        caches.match(event.request).then(function(response) {
            console.log('matched cache', response);
            return response || fetch(event.request);
        })
    );
});

// This will clean old caches after new one is installed
self.addEventListener('activate', function(event) {
    event.waitUntil(
        caches.keys().then(function(cacheNames) {
            return Promise.all(
                cacheNames.map(function(cn) {
                    if (cn != cacheName) {
                        return caches.delete(cn);
                    }
                })
            );
        })
    );
});
