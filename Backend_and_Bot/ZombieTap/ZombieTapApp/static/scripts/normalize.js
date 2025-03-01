document.addEventListener('DOMContentLoaded', function () {
    var metaViewport = document.querySelector('meta[name=viewport]');
    if (metaViewport) {
      metaViewport.content = "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no";
    } else {
      metaViewport = document.createElement('meta');
      metaViewport.name = 'viewport';
      metaViewport.content = "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no";
      document.head.appendChild(metaViewport);
    }
  });