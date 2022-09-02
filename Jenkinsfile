pipeline{
  agent any
  stages {
    
    stage("create S3 bucket"){
      steps{
        script{
        
       sg_id = "${env.SG_ID}"
        def tmpSgIdFile = [
        "replicationServerSGIds": sg_id.split(';')
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