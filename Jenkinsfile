def cleanUp()
{
    echo "Clean up the Workspace"
    sh "rm -rf ./*"
}

pipeline {
    agent any
    options {
        checkoutToSubdirectory('config-repo')
    }
    environment {
        AWS_CONFIG_FILE = "${env.WORKSPACE}/aws-config"
        AWS_SHARED_CREDENTIALS_FILE = "${env.WORKSPACE}/aws-credentials"
        AWS_SDK_LOAD_CONFIG = 'true'
    }        
    stages {
        stage("Configure AWS Credentials"){
          environment {
            accessKeyVariable: 'AWS_ACCESS_KEY_ID'
            credentialsId: 'kiran-aws-creds'
            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
            }
            steps {
                sh "echo \"[itmp-tudeploy]\" > ${env.AWS_SHARED_CREDENTIALS_FILE}"
                sh "echo aws_access_key_id=${env.accessKeyVariable} >> ${env.AWS_SHARED_CREDENTIALS_FILE}"
                sh "echo aws_secret_access_key=${env.secretKeyVariable} >> ${env.AWS_SHARED_CREDENTIALS_FILE}"
            }
        }      
        stage('build') {
            steps {             
              dir('config-repo') {
                sh """chmod +x aws_edrs_config.py
                python ./aws_edrs_config.py"""
              } 
            }
        }
        }
    post {
        always {
            cleanUp()
        }
    }
}