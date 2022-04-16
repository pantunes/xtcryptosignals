upstream backend_nodes {
    ip_hash;

    server 127.0.0.1:5000;
    server 127.0.0.1:5001;
}

upstream socketio_nodes {
    ip_hash;

    server 127.0.0.1:5002;
    server 127.0.0.1:5003;
}

server {
    listen 80;

    server_name api.domain.com;

    return 301 https://api.domain.com$request_uri;
}

server {
    listen 443 ssl http2;

    server_name api.domain.com;

    ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        include proxy_params;
        proxy_pass http://backend_nodes;
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

server {
    listen 80;

    server_name domain.com www.domain.com;

    return 301 https://domain.com$request_uri;
}

server {
    listen 443 ssl;

    server_name www.domain.com;

    ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    return 301 https://domain.com$request_uri;
}

server {
    listen 443 ssl http2;

    server_name domain.com;

    add_header Access-Control-Allow-Origin "https://domain.com";

    ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    client_max_body_size 10M;

    location /static/  {
      alias /xtcryptosignals/client/static/;
      expires 15d;
      access_log off;
    }

    location / {
        proxy_pass_header Server;
        proxy_set_header Host $host;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_pass http://127.0.0.1:8000;
    }
}
