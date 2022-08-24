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
                  environment {
                    AWS_ACCESS_KEY_ID     = credentials('aws_access_key_id')
                    AWS_SECRET_ACCESS_KEY = credentials('aws_secret_access_key')
            }
            steps {
                sh "echo \"[itmp-tudeploy]\" > ${env.AWS_SHARED_CREDENTIALS_FILE}"
                sh "echo aws_access_key_id=${env.AWS_ACCESS_KEY_ID} >> ${env.AWS_SHARED_CREDENTIALS_FILE}"
                sh "echo aws_secret_access_key=${env.AWS_SECRET_ACCESS_KEY} >> ${env.AWS_SHARED_CREDENTIALS_FILE}"
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