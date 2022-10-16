docker system prune -a -f
docker build -t banco_x .
docker run -d -t banco_x
