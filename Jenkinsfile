pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'docker-compose up -d --build'
                sh 'docker-compose down'
                sh 'docker tag mysql:latest fc44311/mysql:latest'
                echo 'Finished building!'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'docker push fc44311/mysql:latest'
                sh 'docker-compose push'
                sh 'kubectl create namespace cc'
                sh 'kubectl apply -f mysql-secret.yaml -n cc'
                sh 'kubectl apply -f mysql-deployment.yaml -n cc'
                sh 'mysql -h 35.233.63.181 -u user -p'
                sh 'user'
                sh 'source /home/jonathangehmayr/projects/ccproject22/database/initdb1.sql'
                sh 'source /home/jonathangehmayr/projects/ccproject22/database/initdb2.sql'
                sh 'kubectl apply -f services-deployment.yaml -n cc'               
            }
        }
    }
}