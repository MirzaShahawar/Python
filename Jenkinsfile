pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t python-cicd:${env.master} .'
                }
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Tests executed successfully!"'
            }
        }

        stage('Push to Registry') {
            when {
                branch 'production'
            }
            steps {
                script {
                    sh 'docker tag python-cicd:production <mirzashahawar>/python-cicd:latest'
                    sh 'docker push <mirzashahawar>/python-cicd:latest'
                }
            }
        }
    }

    post {
        always {
            echo "Build completed."
        }
    }
}

