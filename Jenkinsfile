pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
    }
    stages {
        stage('Install Python') {
            steps {
                bat 'python --version'
            }
        }
        stage("Create Virtual Environment") {
            steps {
                bat """
                    if not exist ${VENV_DIR} (
                        python -m venv ${VENV_DIR}
                    ) else (
                        echo Virtual environment already exists.
                    )
                """
            }
        }
        stage("Install Dependencies and Run Tests") {
            steps {
                bat """
                    ${VENV_DIR}\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest --maxfail=1 --disable-warnings --junitxml=report.xml -q lesson30/test_initial.py
                """
            }
        }
        stage('Publish Test Results') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
