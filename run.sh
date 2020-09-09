mkdir -p data
docker run -v `pwd`/data:/wiki -p 4567:80 gollum
docker container prune -f
