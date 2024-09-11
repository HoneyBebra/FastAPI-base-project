if ! docker network inspect project-network > /dev/null 2>&1; then
  docker network create project-network
fi

docker-compose -f ../service/docker-compose.yml up -d --build&&
docker-compose -f docker-compose.infra.yml up -d --build
