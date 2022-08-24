def cleanUp()
{
    echo "Clean up the Workspace"
    sh "rm -rf ./*"
}

pipeline {
    agent any
    /*options {
        checkoutToSubdirectory('config-repo')
    }
    environment {
        AWS_CONFIG_FILE = "${env.WORKSPACE}/aws-config"
        AWS_SHARED_CREDENTIALS_FILE = "${env.WORKSPACE}/aws-credentials"
        AWS_SDK_LOAD_CONFIG = 'true'
    } */
    stages {
        stage("Configure AWS Credentials"){
          environment {
             AWS_CREDENTIALS = credentials('kiran-aws-creds')
            }
            steps {
                sh "echo $AWS_CREDENTIALS"
                /*sh "echo \"[itmp-tudeploy]\" > ${env.AWS_SHARED_CREDENTIALS_FILE}"
                sh "echo aws_access_key_id=${env.AWS_CREDENTIALS_USR} >> ${env.AWS_SHARED_CREDENTIALS_FILE}"
                sh "echo aws_secret_access_key=${env.AWS_CREDENTIALS_PSW} >> ${env.AWS_SHARED_CREDENTIALS_FILE}"*/
            }
        }      
        /*stage('build') {
            steps {             
              dir('config-repo') {
                sh """chmod +x aws_edrs_config.py
                python ./aws_edrs_config.py"""
              } 
            }
        }
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
        }*/
    post {
        always {
            cleanUp()
        }
    }
}