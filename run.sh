#
# Script that starts manually external dependencies and celery task
# @Note:
# This script is a reference, as does not need to be executed
#

# Activate Virtual Environment
. venv/bin/activate

# Start MongoD, Redis-Server and Celery
rm dump.rdb & rm celerybeat-schedule.db &
mongod -dbpath data & redis-server & celery worker --loglevel=info --beat
