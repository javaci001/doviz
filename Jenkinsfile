pipeline {
    agent any

        stages {
            stage('git islemleri') {
                steps {
                    sh 'echo "basliyorum"'     
                    // /var/lib/jenkins/workspace/ucuncu ya doviz repo clone edilir
                    git branch: 'main', url: 'https://github.com/javaci001/doviz.git'
                }
            } 
        stage('Dockerfile islemleri') {
            steps {
                sh '''
                cat > Dockerfile << 'EOF'
                FROM python:3.8.20
                ENV PYTHONUNBUFFERED=1
                WORKDIR /app
                COPY . .
                RUN python -m pip install flask
                RUN python -m pip install beautifulsoup4
                RUN python -m pip install gunicorn
                EXPOSE 5555
                CMD ["python", "app.py"]
                EOF
                '''
            }
        }   
        stage('Dockerfile build et ve run et') {
            steps {
                sh '''
                docker build -f Dockerfile -t doviz .
                docker run -d -p 5555:5555 --name doviz doviz
                '''
            }
        }   
    }
} 