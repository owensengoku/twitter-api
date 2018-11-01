#!/bin/bash
set -e

if [ -z "${TWITTER_API_CONSUMER_KEY}" ]; then
    echo "TWITTER_API_CONSUMER_KEY environment variable require to set correctly"
    exit 1
fi

if [ -z "${TWITTER_API_CONSUMER_SECRET}" ]; then
    echo "TWITTER_API_CONSUMER_SECRET environment variable require to set correctly"
    exit 1
fi

if [ "$1" = 'gunicorn' ]; then
    exec gunicorn -b ${APPLICATION_HOST}:${APPLICATION_PORT} -e TWITTER_API_CONSUMER_KEY=${TWITTER_API_CONSUMER_KEY} -e TWITTER_API_CONSUMER_SECRET=${TWITTER_API_CONSUMER_SECRET} server
fi

# execute  application
exec "$@"
