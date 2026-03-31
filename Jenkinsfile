pipeline {
  agent any

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Debug Files') {
      steps {
        bat 'dir'
      }
    }

    stage('Install Dependencies') {
      steps {
        bat '"C:\\Users\\poorn\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
      }
    }

    stage('Data Validation') {
      steps {
        bat '"C:\\Users\\poorn\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" scripts\\validate_data.py'
      }
    }

    stage('Model Training') {
      steps {
        bat '"C:\\Users\\poorn\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" model_training.py'
      }
    }

    stage('Evaluate') {
      steps {
        bat '"C:\\Users\\poorn\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" scripts\\evaluate.py --max-mae 0.20'
      }
    }

    stage('Deploy') {
      when { branch 'main' }
      steps {
        bat 'start "" streamlit run app.py'
      }
    }

  }

  post {
    failure {
      echo 'Build failed -- check MAE threshold or data validation'
    }
    success {
      echo 'Build passed -- model deployed successfully'
    }
  }
}
