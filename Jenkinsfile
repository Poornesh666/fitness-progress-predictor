pipeline {
  agent any

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install Dependencies') {
      steps {
        bat '"C:\\Users\\poorn\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
      }
    }

    stage('Run App') {
      steps {
        bat 'start "" streamlit run app.py'
      }
    }

  }
}
