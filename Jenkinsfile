pipeline{
  agent any
  stages {
    
    stage("create S3 bucket")
      steps{
        def tmpSgIdFile = [
        "replicationServerSGIds" = "${env.SG_ID}"
        ]
        writeJSON file: 'tmpfile.json', json: tmpSgIdFile.split(',')

        """
        echo "Deploying to ${params.ENVIRONMENT}"
        sh chmod +x tutorial1.py
        python ./tutorial1.py """
      }
    }
