pipeline {
  agent {
    node {
      label 'node0'
    }
    
  }
  stages {
    stage('modify content') {
      steps {
        sh '''echo `date` >> /tmp/222
'''
      }
    }
  }
}