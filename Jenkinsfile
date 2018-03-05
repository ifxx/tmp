pipeline {
  agent {
    docker {
      image 'nginx'
    }
    
  }
  stages {
    stage('modify content') {
      steps {
        sh 'docker run -d -p 9090:80 -v /tmp:/tmp nginx'
      }
    }
  }
}