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
          /*environment {
            accessKeyVariable = aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID')
            credentialsId = 'kiran-aws-creds'
            secretKeyVariable = 'AWS_SECRET_ACCESS_KEY'
            }*/
            steps {
                sh "echo \"[itmp-tudeploy]\" > ${env.AWS_SHARED_CREDENTIALS_FILE}"
                sh "echo aws_access_key_id=${aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID')} >> ${env.AWS_SHARED_CREDENTIALS_FILE}"
                sh "echo aws_secret_access_key= ${aws(secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')} >> ${env.AWS_SHARED_CREDENTIALS_FILE}"
            }
        }      
        /*stage('build') {
            steps {             
              dir('config-repo') {
                sh """chmod +x aws_edrs_config.py
                python ./aws_edrs_config.py"""
              } 
            }
        }*/
        stage('Initialize EDR Service') {
            when {
                expression { return params.INITIALIZE_SERVICE }
            }
            steps {
                script {
                    dir('config-repo/scripts') {
                        sh "python3 aws_edrs_init.py"
                    }
                }
            }            
        }
        stage('Create Replication Configuration Template') {
            steps {
                script {
                    dir('config-repo/scripts') {
                        sh "python3 aws_edrs_config.py"
                    }
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