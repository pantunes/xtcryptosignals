nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server" > /dev/null 2>&1 &
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/client.prod.env xt-client" > /dev/null 2>&1 &
nohup xt-ticker --enable-messaging --log-minimal > /dev/null 2>&1 &
