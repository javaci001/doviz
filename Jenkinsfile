pipeline {
    agent any

        stages {
            stage('Hello') {
                steps {
                    sh 'echo "Hello World"'
                }
            }
        stage('Log date') {
            steps {
                sh '''
                date
                pwd
                '''
            }
        }   
        stage('hostname yaz') {
            steps {
                sh 'hostname -f'
            }
        }   
    }
}   