# Cloud Computing Project

## Introducion
In this repository you can find a Python API with 3 microservices that handles movies and rating information for administration and regular users. This project was created within the scope of the Cloud Computing subject project of Master in Informatics with the support of Professor Mário Calha. 

## Methodology
This project aimed to learn commonly used technologies in the field of cloud computing, with special focus on DevOps. The APIs for the microservices were defined using Swagger. Data in use stems from the [MUBI Kaggle dataset](https://www.kaggle.com/clementmsika/mubi-sqlite-database-for-movie-lovers) and is fed into a MySQL database. Building the Docker images for the microservices and database was automated with Docker Compose. Deployment of the project was managed by Kubernetes, whereas the YAML manifests in the repository define the configurations for that. In first phases the services were deployed to a local Minikube cluster, while in the final deployment we published at the Kubernetes Engine at GCP. Concerning automation of the development cycle a Jenkins pipline was created to fully automated the process of building, testing and deploying of the application. 


## Requirements
Git and Python 3.5.2+

## Usage
Clone the project:
```
git clone https://github.com/radsurya/ccproject22.git 
```

### Running manually
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


### Running with Docker

To run the 3 micro services and the database on a Docker container, please execute the following from the root directory:

```
docker-compose up -d --build
```
This will build the images and starting up the containers.


### Running with Jenkins

Install Jenkins locally and connect with Github repository. When the pipeline is started with Jenkins, the services are built, tested with accroding to the unit-tests, the docker images pushed to Docker Hub, and then delployed at regarding cluster assigned to `kubectl`. 


## Team
This project was developed by Group  of 2:
- Radica Giva (No. 44311)
- Jonathan Gehmayr (No. 57267)
