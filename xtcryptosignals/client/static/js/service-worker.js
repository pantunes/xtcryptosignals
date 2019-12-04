self.addEventListener('push', function(event) {
  const data = event.data.json();
  const title = data.title;
  let options = {
    body: data.message,
    data: {
      url: data.url,
    },
  };
  if ('icon' in data) {
    options.icon = data.icon
  }
  if ('badge' in data) {
    options.badge = data.badge
  }
  event.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener('notificationclick', function(event) {
  event.notification.close();
  event.waitUntil(
    clients.openWindow(event.notification.data.url)
  );

});
