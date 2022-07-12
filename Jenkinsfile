pipeline{
  agent any
  stages {
    
    stage("create S3 bucket")
      steps{
        echo "Deploying to ${params.ENVIRONMENT}"
        sh """chmod +x tutorial1.py
        python ./tutorial1.py """
      }
    }
