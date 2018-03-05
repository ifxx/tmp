pipeline {
  agent {
    docker {
      image 'nginx'
      args '-d'
    }
    
  }
  stages {
    stage('modify content') {
      steps {
        sh 'pwd'
      }
    }
  }
}