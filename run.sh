. venv/bin/activate
rm dump.rdb & rm celerybeat-schedule.db & mongod -dbpath data &
redis-server & celery worker --loglevel=info --beat
