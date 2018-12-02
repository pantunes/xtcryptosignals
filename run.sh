#
# Script that starts manually external dependencies and celery task
#

# Activate Virtual Environment
. venv/bin/activate

# Start MongoD, Redis-Server and Celery
rm dump.rdb & rm celerybeat-schedule.db & mongod -dbpath data &
redis-server & celery worker --loglevel=info --beat
