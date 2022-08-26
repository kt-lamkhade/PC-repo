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
        AWS_CONFIG_FILE = "${env.WORKSPACE}/config"
        AWS_SHARED_CREDENTIALS_FILE = "${env.WORKSPACE}/credentials"
        AWS_SDK_LOAD_CONFIG = 'true'
    } 
    stages {
        stage("Configure AWS Credentials"){
          environment {
             AWS_CREDENTIALS = credentials('aws_credentials')
            }
            steps {
              sh "echo \"[aws_credentials]\" > ${env.AWS_SHARED_CREDENTIALS_FILE}"
              sh "echo aws_access_key_id=${env.AWS_CREDENTIALS_USR} >> ${env.AWS_SHARED_CREDENTIALS_FILE}"
              sh "echo aws_secret_access_key=${env.AWS_CREDENTIALS_PSW} >> ${env.AWS_SHARED_CREDENTIALS_FILE}"
            }
        }    
        stage('Initialize EDR Service') {
            /*when {
                expression { return params.INITIALIZE_SERVICE }
            }*/
            steps {
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'kiran-aws-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                script {
                    dir('config-repo') {
                      sh "echo Initialize EDR Service inside"
                      sh "python3 aws_edrs_config.py init"
                    }
                }
                }
            }            
        }/*
        stage('Create Replication Configuration Template') {
            steps {
            withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'kiran-aws-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                script {
                dir('config-repo') {
                sh "echo Create Replication Configuration Template"
                sh "python aws_edrs_config.py create"
                }
                }
            }
            }
        }*/
        }
    post {
        always {
            cleanUp()
        }
    }
}