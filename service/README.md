# Service example

## Deploy

To deploy a separate service you need to add

```yaml
ports:
  - "80:80"
```

to a container with nginx

By default, no ports are added, this is for general purposes
deployment in ```FastAPI-base-project/deploy```, in this case
all requests go through the ```nginx-gateway``` container

Also, to deploy a separate service, you need to create a network ```project-network```

```shell
docker network create project-network
docker-compose up -d --build
```