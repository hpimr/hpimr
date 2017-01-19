// Cache everything static

var cacheName = 'HPMOR';
var files2cache = __FILES_TO_CACHE__;

self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open(cacheName).then(function(cache) {
            return cache.addAll(Object.keys(files2cache));
        })
    );
});

// If request matches something in cache - return it from cache
// otherwise do actual request
self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {
            return response || fetch(event.request);
        })
    );
});
