pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Atharvpandarkar/SmartRail.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'C:\\Python314\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                bat 'C:\\Python314\\python.exe -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                bat 'C:\\Python314\\python.exe -m unittest discover -s tests'
            }
        }
    }

    post {
        success {
            echo 'SmartRail CI Pipeline Successful!'
        }
        failure {
            echo 'SmartRail CI Pipeline Failed!'
        }
    }
}
