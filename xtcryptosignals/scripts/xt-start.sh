nohup bash -c "DEBUG=0 xt-server" > /dev/null 2>&1 &
nohup bash -c "SERVER_API_BASE_URL=https://api.xtcryptosignals.com/ xt-client --gunicorn" > /dev/null 2>&1 &
nohup xt-ticker --enable-messaging --log-minimal > /dev/null 2>&1 &
