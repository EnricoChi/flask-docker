# Dockerizing Flask with Gunicorn and Nginx, tutorial

example: https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

nginx: https://nginx.org/ru/docs/stream/ngx_stream_proxy_module.html#proxy_pass
gunicorn: https://gunicorn.org/

## Docker base command

##### build
```
docker-compose build
```

##### run
```
docker-compose up -d
```

##### build and run
```
docker-compose up -d --build
```

##### clear
```
docker-compose down -v
docker system prune
```


## Run project

```
$ docker-compose -f docker-compose.yml up -d --build
```

# Todo:
- [X] Dokerizing project
    - [X] configure Docker
    - [X] configure Gunicorn
    - [X] configure Nginx
    - [ ] configure env_file for dev/prod
    - [ ] separate on dev/prod containers
    - [ ] add PostgreSql
- [ ] GitLab CI/CD
    - [ ] ----