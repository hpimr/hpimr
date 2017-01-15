// Cache everything static
self.addEventListener('install', function(e) {
    console.log('installing cache', e);
    e.waitUntil(
        caches.open('the-magic-cache').then(function(cache) {
            return cache.addAll([
                __FILES_TO_CACHE__
            ]);
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
