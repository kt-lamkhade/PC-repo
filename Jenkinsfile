pipeline{
  agent any
  environment{ 
    AWS_ACCESS_KEY_ID = credentials("aws_access_key_id")
    AWS_SECRET_ACCESS_KEY = credentials('aws_secret_access_key')
  }
  parameters{
    string(name: 'instance_name', defaultValue: '', description: 'Provide the name of instance: ')
    choice(name: 'aws_region', choices: ['us-east-1', 'us-east-2'], description: 'Select Region for deployment: ')
    choice(name: 'environment', choices: ['DEV', 'PROD'], description: 'Select the environment for this deployment: ')
    choice(name: 'instance_type', choices: ['t2.micro'], description: 'Select instance type: ')
    }
  stages {
    stage("build"){
      steps{
        echo"Building ${environment} instance ${instance_type} in ${aws_region}"
      }
    }
    stage("Deploy to non-production environment"){
      when{
        expression { params.environment == 'DEV' }
      }
      steps{
        echo "Deploying to ${params.environment}"
        sh """chmod +x ec2_create_functions.py
        python ./ec2_create_functions.py ${instance_name} ${instance_type} ${aws_region}"""
      }
    }
    stage("Deploy to production environment"){
      when{
        expression { params.environment == 'PROD' }
      }
      steps{
        input message: 'Confirm deployment to production....', ok: 'Deploy'
        echo "Deploying to ${params.environment}"
      }
    }
  }
}
