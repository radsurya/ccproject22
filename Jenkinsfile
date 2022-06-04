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

                sh '''
                    rm -r .env
                    mkdir -p .env
                    cd .env

                    if ! [ -d "venv" ]; then
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r ../movie-service/test-requirements.txt
                        pip install connexion[swagger-ui]
                    fi

                    . venv/bin/activate  
                    cd ../movie-service
                    python3 -m unittest discover
                '''

                sh 'docker-compose down'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'docker push fc44311/mysql:latest'
                sh 'docker-compose push'
                sh 'kubectl create -f namespace.yaml'
                sh 'kubectl apply -f mysql-secret.yaml'
                sh 'kubectl apply -f mysql-deployment.yaml'
                sh 'mysql --password=user --user=user --host=35.233.63.181 --database=mubi_data < "database/initdb1.sql"'
                sh 'mysql --password=user --user=user --host=35.233.63.181 --database=mubi_data < "database/initdb2.sql"'
                sh 'kubectl apply -f services-deployment.yaml'             
            }
        }
    }
}