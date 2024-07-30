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

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});