pipeline{
  agent any
  stages {
    
    stage("create S3 bucket"){
      steps{
        script{
        
        def tmpSgIdFile = [
        "replicationServerSGIds": "${env.SG_ID}"
        ]
        writeJSON file: 'tmpfile.json', json: tmpSgIdFile

        """
        echo "Deploying to ${params.ENVIRONMENT}"
        sh chmod +x tutorial1.py
        python ./tutorial1.py """
        }
      }
    }
    }
}