# Cloud Computing Project

## Introducion
In this repository you can find a Python API with 3 microservices that handles movies and rating information for administration and regular users. This project was created within the scope of the Cloud Computing subject project of Master in Informatics with the support of Professor Mário Calha. 

## Requirements
Python 3.5.2+

## Usage
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

To launch the integration tests, use tox inside of each microservice directory (for admin-service, movie-service and rating-service):
```
sudo pip install tox
tox
```

## Team
This project was developed by Group 3:
- Radica Giva (No. 44311)
- Filipe Pedroso (No. 51958)
- Jonathan Gehmayr (No. 57267)
