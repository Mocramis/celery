##Broker settings
BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "test"
BROKER_PASSWORD = "test"
BROKER_VHOST = "test/"
#CELERY_RESULT_BACKEND = "amqp"
CELERY_IMPORTS = ("task",)
CELERYD_CONCURRENCY = 8

# configure backend to postgresql
CELERY_RESULT_BACKEND = "database"
CELERY_RESULT_DBURI = "postgresql://postgres:postgres@localhost/sync100ktest"

#Limit the number of cached results in order to make the bug visible with few results
CELERY_MAX_CACHED_RESULTS = 1



