pipeline {
    agent any
    stages {
        stage('build') {
            steps {
            withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'kiran-aws-creds', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                sh 'terraform fmt --no-color'
                sh 'terraform init --no-color'
                sh 'terraform apply -var-file=\"my.tfvars\" --auto-approve --no-color'
        }
            }
        }
    }
}