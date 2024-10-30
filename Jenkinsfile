pipeline {
    agent any
    environment {
        PYTHON_VERSION = '3.11.9'
        VENV_DIR = 'venv'
    }
    stages {
        stage('Install Dependencies') {
            steps {
                // Встановлення pyenv, якщо він не встановлений
                sh '''
                if ! command -v pyenv &> /dev/null; then
                    echo "Installing pyenv..."
                    curl https://pyenv.run | bash
                    export PATH="$HOME/.pyenv/bin:$PATH"
                    eval "$(pyenv init --path)"
                    eval "$(pyenv init -)"
                fi
                pyenv install -s ${PYTHON_VERSION}
                pyenv global ${PYTHON_VERSION}

                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage("Creation of Python virtual environment") {
            steps {
                script {
                    sh """
                        source ~/.bashrc
                        export PATH="\$HOME/.pyenv/bin:\$PATH"
                        eval "\$(pyenv init --path)"
                        eval "\$(pyenv init -)"

                        if [ ! -d "\${VENV_DIR}" ]; then
                            echo "Creating virtual environment in \${VENV_DIR}"
                            python3 -m venv \${VENV_DIR}
                        else
                            echo "Virtual environment already exists in \${VENV_DIR}."
                        fi
                    """
                }
            }
        }
        stage("Activation of venv, installing dependencies, and running test cases") {
            steps {
                script {
                    sh """
                        source ~/.bashrc
                        source \${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pytest --maxfail=1 --disable-warnings -q lesson30/test_initial.py
                    """
                }
            }
        }
    }
}
