# server instance (backend)
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5000" > /dev/null 2>&1 &

# server instances (socket.io)
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5001" > /dev/null 2>&1 &
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5002" > /dev/null 2>&1 &
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5003" > /dev/null 2>&1 &

# client instance (N workers will be spawn automatically based on cli param or number of cpus)
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/client.prod.env xt-client --num-workers 2" > /dev/null 2>&1 &

# ticker instance
nohup bash -c "redis-cli FLUSHALL && SETTINGS_APP=`pwd`/config/server.prod.env xt-ticker --enable-messaging --log-minimal" > /dev/null 2>&1 &
