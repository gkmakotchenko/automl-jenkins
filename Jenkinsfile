pipeline {
  agent any

  triggers {
    githubPush()
  }

  options {
    timestamps()
    disableConcurrentBuilds()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup venv') {
      steps {
        sh '''
          set -eux
          python3 -V
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -U pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Checks (ruff + black)') {
      steps {
        script {
          int ruffCode = sh(
            script: '''
              set +e
              . .venv/bin/activate
              ruff check .
              echo $? > .ruff_exit
              exit 0
            ''',
            returnStatus: true
          )

          int blackCode = sh(
            script: '''
              set +e
              . .venv/bin/activate
              black --check .
              echo $? > .black_exit
              exit 0
            ''',
            returnStatus: true
          )

          def ruffExit = sh(script: "cat .ruff_exit", returnStdout: true).trim()
          def blackExit = sh(script: "cat .black_exit", returnStdout: true).trim()

          echo "ruff exit code: ${ruffExit}"
          echo "black exit code: ${blackExit}"

          if (ruffExit != "0" || blackExit != "0") {
            currentBuild.result = 'FAILURE'
          }
        }
      }
    }

    stage('Fail if checks failed') {
      steps {
        script {
          if (currentBuild.result == 'FAILURE') {
            error("Code quality checks failed (see Ruff/Black output above).")
          }
        }
      }
    }
  }

  post {
    always {
      echo "Build finished: ${currentBuild.currentResult}"
    }
  }
}
