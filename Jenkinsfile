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
        //https://stackoverflow.com/questions/40836570/jenkinsfile-and-python-virtualenv
        stage('Test') {
            steps {
                echo 'Testing..'
                // Activate Python venv
                dir('/home/jonathangehmayr/dir_envs/') {
                    sh '. cc/bin/activate'
                }

                sh "pwd"
                // use test requirements for testing
                //                    pip install virtualenv
                sh '''
                    mkdir -p .env
                    cd .env

                    if ! [ -d "venv" ]; then
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r ../movie-service/test-requirements.txt
                    fi
                    . venv/bin/activate  
                    cd ../movie-service
                    python3 -m unittest discover
                '''
                dir('movie-service') {
                    sh "pwd"
                    //sh '/home/jonathangehmayr/dir_envs/cc/bin/python3 -m unittest discover'         
                    sh 'python3 -m unittest discover' 
                    //sh 'python3 -m unittest swagger_server/test/test_movie_controller.py'

                }
                sh "pwd"

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