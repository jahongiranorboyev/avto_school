#!/bin/bash

HOST=$1
PORT=$2

shift 2

until nc -z -v -w30 $HOST $PORT
do
  echo "Connection to Postgres on $HOST:$PORT is not available, try again ...."
  slepp 1
done

echo "Postgres is available on $HOST:$PORT!"

exec "$@"