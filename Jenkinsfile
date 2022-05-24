pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'docker-compose build'
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
                sh 'docker-compose push'
                sh 'kubectl create namespace cc'
                sh 'kubectl apply -f services-deployment.yaml -n cc'
                
            }
        }
    }
}