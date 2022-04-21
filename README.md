# Cloud Computing Project

## Introducion
In this repository you can find a Python API with 3 microservices that handles movies and rating information for administration and regular users. This project was created within the scope of the Cloud Computing subject project of Master in Informatics with the support of Professor Mário Calha. 

## Requirements
Git and Python 3.5.2+

## Usage
Clone the project:
```
git clone https://github.com/radsurya/ccproject22.git 
```

To run the microservices, please execute the following commands inside each microservice directory (for admin-service, movie-service and rating-service):
```
pip3 install -r requirements.txt
python3 -m swagger_server
```

To check that the microservices are running, open your browser in this urls:

For admin-service:
```
http://localhost:8080/fc44311/ccproject22/1.0.0/ui/
```

For movie-service:
```
http://localhost:8081/fc44311/ccproject22/1.0.0/ui/
```

For rating-service:
```
http://localhost:8082/fc44311/ccproject22/1.0.0/ui/
```


## Running with Docker

To run the 3 micro services and the database on a Docker container, please execute the following from the root directory:

```
docker-compose -f docker-compose.yml up -d --build
```
This will build the images and starting up the containers.


## Team
This project was developed by Group 3:
- Radica Giva (No. 44311)
- Filipe Pedroso (No. 51958)
- Jonathan Gehmayr (No. 57267)
