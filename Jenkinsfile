pipeline {
  agent {
    node {
      label 'node0'
    }
    
  }
  stages {
    stage('modify content') {
      steps {
        sh 'echo 123 > /tmp/123'
      }
    }
  }
}