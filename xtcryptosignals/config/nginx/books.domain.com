server {
    listen 80;

    server_name books.domain.com;

    return 301 https://books.domain.com$request_uri;
}

server {
    listen 443 ssl http2;

    server_name books.domain.com;

    ssl_certificate /etc/letsencrypt/live/books.domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/books.domain.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location /socket.io {
        include proxy_params;
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_pass http://server.instance:<port>/socket.io;
    }
}