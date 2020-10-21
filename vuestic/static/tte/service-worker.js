importScripts("/vuestic/static/tte/precache-manifest.8f88b7723c8fb8cf3af3f876c7bb6e85.js", "/vuestic/static/tte/workbox-v4.3.1/workbox-sw.js");
workbox.setConfig({
    modulePathPrefix: "/workbox-v4.3.1"
});
self.__precacheManifest = [].concat(self.__precacheManifest || [])
workbox.precaching.suppressWarnings()
workbox.precaching.precacheAndRoute(self.__precacheManifest, {})

workbox.routing.registerRoute(
    /\.(?:png|gif|jpg|jpeg|svg)$/,
    workbox.strategies.staleWhileRevalidate(0),
)

workbox.routing.registerRoute(
    new RegExp('https://reqres.in'),
    workbox.strategies.networkFirst(),
)