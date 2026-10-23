
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
                bat 'python --version'
            }
        }

        stage('Run HTML Form Tests') {
            steps {
                bat 'python -m unittest test_form.py -v'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed!'
        }

        failure {
            echo 'FAILURE: Pipeline failed. Check Console Output.'
        }

        always {
            echo 'HTML Form Jenkins Pipeline execution completed.'
        }
    }
}
