### FastAPI-Postgres-docker-compose ##

* FastAPI app 
* PostgreSQL integration using SQLAlchemy
* Dockerfile and docker-compose integations


### How to run this with Docker? ###

* Make sure you have docker installed and runninng on your machine
* Open the terminal to the docker-compose path and hit the following command - 

DB_CONNECTION=postgresql://{{YOUR_OWNER}}:{{YOUR_PASSWORD_DATABASE}}@db:{{YOUR_PORT_DATABASE}}/{{YOUR_NAME_DATABASE}}
 ```
 MYCOMPUTER:FastAPI user$ cp .env.template .env
 MYCOMPUTER:FastAPI user$ docker-compose up -d --build db app
 MYCOMPUTER:FastAPI user$ docker logs app
 ```
 
