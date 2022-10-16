source .env
source .env.sqlserver
export USE_DATABASE="sqlserver"
docker system prune -a -f
docker build --build-arg MY_SERVICE_PORT=5000 --build-arg MY_SERVICE_URL=0.0.0.0:5000  -t banco_x .
docker run -d -t banco_x
