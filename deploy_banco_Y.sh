source .env
export USE_DATABASE="mysql"
docker system prune -a -f
docker build --build-arg MY_SERVICE_PORT=8000 --build-arg MY_SERVICE_URL=0.0.0.0:8000 -t banco_y .
docker run -d -t banco_y
