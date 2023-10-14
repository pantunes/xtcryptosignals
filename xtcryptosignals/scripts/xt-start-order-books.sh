# server instance (backend)
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5004" > /dev/null 2>&1 &
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5005" > /dev/null 2>&1 &
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5006" > /dev/null 2>&1 &
nohup bash -c "FLASK_ENV=production SETTINGS_APP=`pwd`/config/server.prod.env xt-server --port 5007" > /dev/null 2>&1 &

# celery worker instance that will spawn N processes
# the number of worker processes/threads can be changed using the CELERYD_CONCURRENCY constant in celeryconfig.py file and defaults to the
# number of CPUs available in the machine
nohup bash -c "redis-cli FLUSHALL && SETTINGS_APP=`pwd`/config/server.prod.env xt-tasks -t order_book" > /dev/null 2>&1 &
