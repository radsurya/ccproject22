pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'docker-compose up -d --build'
                sh 'docker tag mysql:latest fc44311/mysql:latest'
                echo 'Finished building!'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'cd movie-service'
                //sh 'python -m unittest discover'
                sh '/home/jonathangehmayr/dir_envs/cc/bin/python3 -m unittest discover'
                //sh 'docker-compose down'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                //sh 'docker push fc44311/mysql:latest'
                //sh 'docker-compose push'
                //sh 'kubectl create namespace cc'
                //sh 'kubectl apply -f mysql-secret.yaml -n cc'
                //sh 'kubectl apply -f mysql-deployment.yaml -n cc'
                //sh 'mysql --password=user --user=user --host=35.233.63.181 --database=mubi_data < "database/initdb1.sql"'
                //sh 'mysql --password=user --user=user --host=35.233.63.181 --database=mubi_data < "database/initdb2.sql"'
                //sh 'kubectl apply -f services-deployment.yaml -n cc'             
            }
        }
    }
}