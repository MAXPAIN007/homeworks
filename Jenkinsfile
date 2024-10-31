pipeline {
    agent any
    environment {
        PYTHON_VERSION = '3.12.5'
        VENV_DIR = 'venv'
    }
    stages {
        stage('Install Python') {
            steps {
                bat 'python --version'
            }
        }
        stage('Create Virtual Environment') {
            steps {
                bat '''
                    if not exist ${VENV_DIR} (
                        python -m venv ${VENV_DIR}
                    ) else (
                        echo Virtual environment already exists.
                    )
                '''
            }
        }
        stage("Install Dependencies and Run Tests") {
            steps {
                bat '''
                    ${VENV_DIR}\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest -v --maxfail=1 --disable-warnings --junitxml=report.xml -q lesson30/test_initial.py | tee pytest_output.txt
                '''
            }
        }
        stage('Publish Test Results') {
            steps {
                junit '**/report.xml'
                archiveArtifacts artifacts: 'pytest_output.txt', allowEmptyArchive: true
            }
        }
    }
}
