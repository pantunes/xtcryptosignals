# server instances (backend)
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5000" > /dev/null 2>&1 &
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5001" > /dev/null 2>&1 &

# server instances (socket.io)
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5002" > /dev/null 2>&1 &
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5003" > /dev/null 2>&1 &

# client gunicorn master instance (N workers will be spawn automatically based on cli param or defaults to the number of CPUs available in the machine)
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/client.prod.env xt-client --num-workers 1" > /dev/null 2>&1 &

# celery worker instance that will spawn N processes
# the number of worker processes/threads can be changed using the CELERYD_CONCURRENCY constant in celeryconfig.py file and defaults to the
# number of CPUs available in the machine
nohup bash -c "redis-cli FLUSHALL && SETTINGS_APP=`pwd`/config/server.prod.env xt-tasks --log-ticker-minimal" > /dev/null 2>&1 &
