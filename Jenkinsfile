pipeline {
  agent {
    docker {
      image 'nginx'
    }
    
  }
  stages {
    stage('modify content') {
      steps {
        sh 'hostname'
      }
    }
  }
}