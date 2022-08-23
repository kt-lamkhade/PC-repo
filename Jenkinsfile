pipeline {
    agent any
    stages {
        stage('build') {
            steps {
            withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'kiran-aws-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                dir("${env.WORKSPACE}/ec2-structure/"){
                sh 'aws_edrs_config.py'
                }
            }
            }
        }
        }
}