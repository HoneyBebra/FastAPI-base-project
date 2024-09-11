# FastAPI-base-project

Blank for developing services

### Technology

[![FastAPI][FastAPI-badge]][FastAPI-url]
[![Gunicorn][Gunicorn-badge]][Gunicorn-url]
[![Nginx][Nginx-badge]][Nginx-url]
[![Docker][Docker-badge]][Docker-url]

### Installation and launch

1. Clone repo

    ```shell
    git clone https://github.com/HoneyBebra/FastAPI-base-project.git
    cd FastAPI-base-project
    ```

2. Install dependencies

   ```shell
   pip install --upgrade pip
   pip install -r requirements-dev.txt
   cd service
   pip install -r requirements.txt
   cd ..
   ```

3. Create a .env as in deploy/.env.example
4. Deploy

   ```shell
   cd deploy
   docker-compose up -d
   ```

<!-- MARKDOWN LINKS & BADGES -->

[FastAPI-url]: https://fastapi.tiangolo.com/
[FastAPI-badge]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi

[Gunicorn-url]: https://gunicorn.org
[Gunicorn-badge]: https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white

[Nginx-url]: https://nginx.org
[Nginx-badge]: https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white~~

[Docker-url]: https://www.docker.com
[Docker-badge]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
