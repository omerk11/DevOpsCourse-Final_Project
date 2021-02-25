pipeline {
    agent any
    environment {
        registry = "omerk11/my-repo"
        registryCredential = 'docker_hub'
        dockerImage = ''
        }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5' ))
    }
    stages {
        stage('[1] Pull Code') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
                git 'https://github.com/omerk11/Project2.git'
            }
        }
        stage('[2] Run rest app server ') {
            steps {
                script {
                    sh 'nohup python rest_app.py &'

                }
            }
        }

        stage('[3] Run backend testing') {
            steps {
                script {
                    sh 'python3.8 backend_testing.py'

                }
            }
        }
        stage('[4] Run clean environment ') {
            steps {
                script {
                    sh ' python3.8 clean_environment.py'

                }
            }
        }
        stage('[5] Build docker image ') {
            steps {
                script {
                    sh ' docker build -t project2 .'
                }
            }
        }
         stage('[6] Build and push image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry('', registryCredential) {
                    dockerImage.push()
                    }
                }
            }
        post{
        always{
            sh "docker rmi $registry:$BUILD_NUMBER"
        }
       }
      }

        stage('[7] Set compose image version ') {
            steps {
                script {
                    sh ' echo IMAGE_TAG=${BUILD_NUMBER} > .env'
                }
            }
        }
        stage('[8] Run docker compose ') {
            steps {
                script {
                    sh ' docker-compose up -d '
                }
            }
        }
        stage('[9] Run docker backend testing') {
            steps {
                script {
                    sh ' python3.8 docker_backend_testing.py'
                }
            }
        }
         stage('[10] Run clean docker environment environment ') {
            steps {
                script {
                    sh 'docker rmi project3'
                    sh 'docker-compose down'
                }
            }
        }
    }
}
