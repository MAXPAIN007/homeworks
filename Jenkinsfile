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
                    if not exist venv (
                        python -m venv venv
                    ) else (
                        echo "Virtual environment already exists."
                    )
                '''
            }
        }
        stage('Install Dependencies and Run Tests') {
            steps {
                echo 'Entering the test stage...'
                bat '''
                    echo Activating virtual environment
                    source venv/Scripts/activate

                    echo Checking if pytest is installed
                    pip show pytest || pip install pytest

                    echo Installing dependencies...
                    pip install -r requirements.txt

                    echo Running tests...
                    pytest -v --maxfail=1 -q lesson30/test_initial.py --junitxml=report.xml | tee pytest_output.txt

                    echo Test execution completed. Checking if report.xml was generated...
                    if exist report.xml (
                        echo "report.xml found!"
                    ) else (
                        echo "report.xml not found!"
                    )
                '''
            }
        }
        stage('Publish Test Results') {
            steps {
                junit 'report.xml'
            }
        }
    }
}

