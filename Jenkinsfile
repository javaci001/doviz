pipeline {
    agent any

        stages {
            stage('Hello') {
                steps {
                    sh 'echo "basliyorum"'
                    sh 'mkdir /home/ubuntum/Desktop/jenkinsislem/dovizkodindir'
                    dir('/home/ubuntum/Desktop/jenkinsislem/dovizkodindir') {
                        git branch: 'main', url: 'https://github.com/javaci001/doviz.git'
                    }
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