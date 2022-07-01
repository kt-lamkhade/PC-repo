pipeline{
  agent any
  parameters{
    string(name: 'INSTANCE_NAME', defaultValue: '', description: 'Provide the name of instance: ')
    choice(name: 'REGION', choices: ['us-east-1', 'us-east-2'], description: 'Select Region for deployment: ')
    choice(name: 'ENVIRONMENT', choices: ['DEV', 'PROD'], description: 'Select the environment for this deployment: ')
    }
  stages {
    stage("build"){
      steps{
        echo"Building ${ENVIRONMENT} instance ${INSTANCE_NAME} in ${REGION}"
      }
    }
    stage("Deploy to non-production environment"){
      when{
        expression {parame.ENVIRONMENT = 'DEV'}
      }
      steps{
        echo "Deploying to ${params.ENVIRONMENT}"
      }
    }
  }
}
