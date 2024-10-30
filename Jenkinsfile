pipeline {
    agent any
    environment {
        PYTHON_VERSION = '3.11.9'
        VENV_DIR = 'venv'
    }
    stages {
        stage('Installing Python') {
            steps {
                script {
                    sh """
                        if command -v pyenv &> /dev/null; then
                            echo "Pyenv is already installed."
                        else
                            echo "Installing pyenv..."
                            curl https://pyenv.run | bash
                        fi
                        export PATH="\$HOME/.pyenv/bin:\$PATH"
                        eval "\$(pyenv init --path)"
                        eval "\$(pyenv init -)"

                        if pyenv versions | grep -q \${PYTHON_VERSION}; then
                            echo "Python \${PYTHON_VERSION} is already installed."
                        else
                            pyenv install \${PYTHON_VERSION}
                        fi
                        pyenv global \${PYTHON_VERSION}
                    """
                }
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
