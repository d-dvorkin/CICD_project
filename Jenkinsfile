pipeline {
  agent any
  environment {
    IMAGE_NAME = 'rzlinux0/proj3:${BUILD_NUMBER}'
    awsPath = "/var/jenkins_home/.aws"
  }
  stages {
    stage('Checkout') {
      steps {
        cleanWs()
        sh 'git clone -b main https://github.com/d-dvorkin/CICD_project.git'

      }
    }
    stage('Build Docker Image') {
      steps {
        //copy aws creds for docker to be able to run .py using boto
        sh "cp -r ${env.awsPath} Proj3/"
        dir('Proj3') {
          script {
            sh "docker build -t ${env.IMAGE_NAME} ."
          }      
        }
      }
    }

    stage('DockerHub push') {
        steps {
            script {
                // Read the DockerHub credentials from the properties file
                def dockerhubCredentials = readFile('/var/jenkins_home/.dockerhub/dockerhub-credentials.properties').trim()
                // Split the contents of the file into an array of lines
                def credentials = dockerhubCredentials.tokenize("\n")
                // Set the DockerHub username and password as environment variables
                env.DOCKERHUB_USERNAME = credentials[0].trim().split("=")[1].trim()
                env.DOCKERHUB_PASSWORD = credentials[1].trim().split("=")[1].trim()
                sh "docker login -u ${env.DOCKERHUB_USERNAME} -p ${env.DOCKERHUB_PASSWORD} https://index.docker.io/v1/"
                sh "docker push ${env.IMAGE_NAME}"
            }
        }
    }

    stage('Run cat pylint output') {
      steps {
        script {
          sh "docker run ${env.IMAGE_NAME} cat pylint-output.txt"
        }
      }
    }

  }
}
