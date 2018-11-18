#
# In case of executing the script directly without using Celery
#

# Activate Virtual Environment
. venv/bin/activate

# Start MongoD, Redis-Server and Celery
rm dump.rdb & rm celerybeat-schedule.db & mongod -dbpath data &
redis-server & celery worker --loglevel=info --beat
