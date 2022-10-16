docker system prune -a -f
docker build -t banco_x .
docker run -p 8000:5000 -d -t banco_x
