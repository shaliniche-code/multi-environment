pipeline {
    agent any
    stages {
        stage("git clone"){
            steps{
                git branch: 'main', 
                credentialsId: 'github-sshkey', 
                url: 'git@github.com:shaliniche-code/multi-environment.git'
            }
        }
        stage("listing the files"){
            steps{
                sh 'ls'
            }
        }
        stage("build image"){
    steps{
        sh 'docker rmi -f simpleflaskimgv1 || true'
        sh 'docker build -t simpleflaskimgv1 .'
    }
}

        stage('Push to Docker Hub') {
    steps {
        withCredentials([
            usernamePassword(
                credentialsId: 'dockerhub-creds',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS'
            )
        ]) {
            sh '''
            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin

            docker tag simpleflaskimgv1 $DOCKER_USER/simpleflaskimgv1:latest

            docker push $DOCKER_USER/simpleflaskimgv1:latest
            '''
        }
    }
}
         stage('Deploy DEV') {
    steps {
        sh '''
        ssh root@172.31.33.21 "

        docker pull shalinidocker12/simpleflaskimgv1:latest

        docker stop devsimpleflaskcontainerv1 || true
        docker rm devsimpleflaskcontainerv1 || true
        
        docker run -d \
        --name devsimpleflaskcontainerv1 \
        -p 5000:5000 \
        -e APP_ENV=Development \
        shalinidocker12/simpleflaskimgv1:latest
        "
        '''
        
    }
}

        stage('Health Check') {
    steps {
        sh '''
        ssh root@172.31.33.21 "
        sleep 10
        curl -f http://localhost:5000
        "
        '''
    }
}
      stage('Approval') {
    steps {
        input 'Deploy to Production?'
    }
}

    stage('Deploy PROD') {
    steps {
        sh '''
        ssh root@172.31.33.21 "
        
        docker pull shalinidocker12/simpleflaskimgv1:latest

        docker stop prodsimpleflaskcontainerv1 || true
        docker rm prodsimpleflaskcontainerv1 || true

        docker run -d \
        --name prodsimpleflaskcontainerv1 \
        -p 5001:5000 \
        -e APP_ENV=Production \
        shalinidocker12/simpleflaskimgv1:latest
        "
        '''
    }
}
    }
    
 }   
