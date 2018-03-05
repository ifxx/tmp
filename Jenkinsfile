pipeline {
  agent {
    docker {
      image 'nginx'
      args '-d -p 9090:80 -v /tmp/tmp'
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