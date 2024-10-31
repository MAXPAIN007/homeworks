pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Create Virtual Environment') {
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
        stage("Activate venv, Install Dependencies, and Run Tests") {
            steps {
                bat """
                    ${VENV_DIR}\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest --maxfail=1 --disable-warnings -q lesson30/test_initial.py
                """
            }
        }
        stage("Publish Test Results") {
            steps {
                junit 'report.xml'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.xml', allowEmptyArchive: true
        }
        success {
            mail to: 'InsertYour@Mail.Here',
                 subject: "SUCCESS: Pipeline ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                 body: "Всі тести пройшли успішно. Ви можете перевірити результати тут: ${env.BUILD_URL}"
        }
        failure {
            mail to: 'InsertYour@Mail.Here',
                 subject: "FAILURE: Pipeline ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                 body: "Деякі тести не пройшли. Перевірте результати тут: ${env.BUILD_URL}"
        }
    }
}
