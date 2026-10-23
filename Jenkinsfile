
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Check Python Installation') {
            steps {
                bat '"C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" --version'
            }
        }

        stage('Run HTML Form Tests') {
            steps {
                bat '"C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m unittest test_form.py -v'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed!'
        }

        failure {
            echo 'FAILURE: Check Console Output for errors.'
        }

        always {
            echo 'HTML Form Jenkins Pipeline execution completed.'
        }
    }
}
