source .env
export USE_DATABASE="sqlserver"
docker system prune -a -f
docker build --build-arg MY_SERVICE_PORT=8000 --build-arg MY_SERVICE_URL=0.0.0.0:8000  -t banco_x .
docker run -d -t banco_x
