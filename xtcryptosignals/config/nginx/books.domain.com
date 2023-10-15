upstream socketio_nodes {
    ip_hash;

    server 127.0.0.1:5004;
    server 127.0.0.1:5005;
    server 127.0.0.1:5006;
    server 127.0.0.1:5007;
}

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
    ssl_trusted_certificate /etc/letsencrypt/live/books.domain.com/chain.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;

    location / {
        deny all;
        return 404;
    }

    location /socket.io {
        include proxy_params;
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_pass http://socketio_nodes/socket.io;
    }
}
