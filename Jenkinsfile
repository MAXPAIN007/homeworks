pipeline {
    agent any
    environment {
        PYTHON_VERSION = 'python3' // Убедитесь, что Python доступен в PATH
        VENV_DIR = 'venv'
    }
    stages {
        stage('Checkout Code') {
            steps {
                // Извлечение кода из репозитория
                checkout scm
            }
        }
        stage('Create Virtual Environment') {
            steps {
                script {
                    // Создание виртуального окружения
                    bat """
                        ${PYTHON_VERSION} -m venv ${VENV_DIR}
                    """
                }
            }
        }
        stage('Activate venv, Install Dependencies, and Run Tests') {
            steps {
                script {
                    // Активация виртуального окружения, установка зависимостей и запуск тестов
                    bat """
                        call ${VENV_DIR}\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pytest --maxfail=1 --disable-warnings -q lesson30/test_initial.py
                    """
                }
            }
        }
        stage('Publish Test Results') {
            steps {
                // Загрузка результатов тестирования
                junit 'report.xml'
            }
        }
    }
}
