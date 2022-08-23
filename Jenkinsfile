pipeline {
    agent any
    options {
        checkoutToSubdirectory('config-repo')
    }    
    stages {
        stage('build') {
            steps {
            withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'kiran-aws-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                dir('config-repo/DR/PC-repo/'){
                sh 'aws_edrs_config.py'
                }
            }
            }
        }
        }
}