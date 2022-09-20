def cleanUp()
{
    echo "Clean up the Workspace"
    sh "rm -rf ./*"
    sh "rm -rf ${WORKSPACE}/config-repo/*"
    sh "rm -fr ${env.AWS_CONFIG_FILE}"
    sh "rm -fr ${env.AWS_SHARED_CREDENTIALS_FILE}" 
}

pipeline {
    agent any
    options {
        checkoutToSubdirectory('config-repo')
    }
    environment {
        AWS_CONFIG_FILE = "${env.WORKSPACE}/config-repo/tmpconfig.json"
        AWS_SHARED_CREDENTIALS_FILE = "${env.WORKSPACE}/credentials"
        AWS_SDK_LOAD_CONFIG = 'true'
        REPLICATION_TEMPLATE = "${env.WORKSPACE}/config-repo/replication_template.json"
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
        stage('Parse Prerequisite Parameters'){

        environment {
            AWS_REGION = "${params.AWS_REGION}"
            SUBNET_ID = "${params.SUBNET_ID}"
            EDR_CLASS = "${params.EDR_CLASS}"
            SG_ID = "${params.SG_ID}"
        }
        /*
            steps {
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'kiran-aws-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                script {
                    dir("${WORKSPACE}/config-repo/") {
                        sh "python generate_script.py"
                    }
                
                    // Construct the JSON argument to the python function
                    def myap = [
                        "region": "${env.AWS_REGION}",
                        "stagingAreaSubnetId": "${env.SUBNET_ID}",
                        "edrClass": "${env.EDR_CLASS}"
                        
                    ]
                    // Convert Map to JSON
                    writeJSON file: 'config-repo/tmpfile.json', json: myap
                    sg_id = "${env.SG_ID}"
                    def tmpSgIdFile = [
                        "replicationServerSGIds": sg_id.split(',')
                        ]
                    writeJSON file: 'config-repo/tmpsgfile.json', json: tmpSgIdFile
                    

                   }
               }
            } 
          }  
        stage('Initialize EDR Service') {
            when {
                expression { return params.INITIALIZE_SERVICE }
            }
            steps {
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'kiran-aws-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                script {
                    dir('config-repo') {
                      sh "python3 aws_edrs_config.py init"
                    }
                }
                }
            }            
        }
        stage('describe Replication Template'){
            steps{
            withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'kiran-aws-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                sh "aws drs describe-replication-configuration-templates --region us-east-1 > ${env.REPLICATION_TEMPLATE}"
            }
            }
        }
        
        stage('Create Replication Template'){
            steps{
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'kiran-aws-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                script{
                dir('config-repo'){
                sh "python aws_edrs_config.py test"
                }
                }
                }
            }
        }*/

        stage('test Replication Configuration Template') {
            steps {
            withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'kiran-aws-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                script {
                dir('config-repo') {
                sh "python aws_edrs_config.py test"
                }
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