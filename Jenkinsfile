pipeline {
    agent any
    environment {
        PYTHON_VERSION = '3.11.9'
        VENV_DIR = 'venv'
    }
    stages {
        stage('Install Python') {
            steps {
                bat '''
                if exist "%USERPROFILE%\\.pyenv" (
                    echo Pyenv уже установлен.
                ) else (
                    echo Устанавливаем pyenv...
                    curl -o pyenv-installer.bat https://pyenv.run
                    pyenv-installer.bat
                    set PATH=%USERPROFILE%\\.pyenv\\bin;%PATH%
                )
                '''
            }
        }
        stage("Create Virtual Environment") {
            steps {
                bat '''
                if not exist "%VENV_DIR%" (
                    echo Создаем виртуальное окружение
                    python -m venv %VENV_DIR%
                ) else (
                    echo Виртуальное окружение уже существует
                )
                '''
            }
        }
        stage("Install Dependencies and Run Tests") {
            steps {
                bat '''
                call %VENV_DIR%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pytest --maxfail=1 --disable-warnings -q lesson30/test_initial.py
                '''
            }
        }
    }
}
