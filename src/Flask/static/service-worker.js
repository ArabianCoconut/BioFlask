// src/Flask/static/service-worker.js
const CACHE_NAME = 'BioFlask-cache-v1';
const urlsToCache = [
  '/',
  '/static/style.css',
  '/static/script.js',
  '/static/images/dna_16px.png',
  '/static/images/dna_24px.png',
  '/static/images/dna_32px.png',
  '/static/images/dna_64px.png',
  '/static/images/dna_128px.png',
  '/static/images/dna_256px.png',
  '/static/images/dna_512px.png'
];

// Install the service worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
  self.skipWaiting(); // Force the waiting service worker to become the active service worker
});

// Activate the service worker
self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim(); // Ensure that the service worker takes control of the page immediately
});

// Fetch and update the service worker
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        const fetchPromise = fetch(event.request).then(networkResponse => {
          if (networkResponse && networkResponse.status === 200) {
            caches.open(CACHE_NAME).then(cache => {
              cache.put(event.request, networkResponse.clone());
            });
          }
          return networkResponse;
        }).catch(() => {
          return response; // Return the cached response if network fetch fails
        });
        return response || fetchPromise;
      })
  );
});