pipeline{
  agent any
  parameters{
    string(name: 'INSTANCE_NAME', defaultValue: '', description: 'Provide the name of instance: ')
    choice(name: 'AWS_REGION', choices: ['us-east-1', 'us-east-2'], description: 'Select Region for deployment: ')
    choice(name: 'ENVIRONMENT', choices: ['DEV', 'PROD'], description: 'Select the environment for this deployment: ')
    choice(name: 'INSTANCE_TYPE', choices: ['t2.micro'], description: 'Select instance type: ')
    }
  stages {
    stage("build"){
      steps{
        echo"Building ${ENVIRONMENT} instance ${INSTANCE_NAME} in ${AWS_REGION}"
      }
    }
    stage("Deploy to non-production environment"){
      when{
        expression { params.ENVIRONMENT == 'DEV' }
      }
      steps{
        echo "Deploying to ${params.ENVIRONMENT}"
        sh """chmod +x ec2_create_functions.py
        python ./ec2_create_functions.py ${INSTANCE_NAME} ${INSTANCE_TYPE} ${AWS_REGION}"""
      }
    }
    stage("Deploy to production environment"){
      when{
        expression { params.ENVIRONMENT == 'PROD' }
      }
      steps{
        input message: 'Confirm deployment to production....', ok: 'Deploy'
        echo "Deploying to ${params.ENVIRONMENT}"
      }
    }
  }
}
