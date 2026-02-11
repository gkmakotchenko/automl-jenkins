pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup venv') {
      steps {
        sh '''
          python3 -V
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -U pip
          pip install -r lab3/requirements.txt
        '''
      }
    }

    stage('Lint (ruff)') {
      steps {
        sh '''
          . .venv/bin/activate
          cd lab3
          ruff check .
        '''
      }
    }

    stage('Format check (black)') {
      steps {
        sh '''
          . .venv/bin/activate
          cd lab3
          black --check .
        '''
      }
    }
  }

  post {
    always {
      echo "Build finished: ${currentBuild.currentResult}"
    }
  }
}
