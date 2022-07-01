pipeline{
  agent any
  parameters{
    string(name: 'INSTANCE_NAME', defaultValue: '', description: 'Please mention name of instance: ')
    choice(name: 'REGION', choices: ['us-east-1', 'us-east-2'], description: 'Select Region for deployment: ')
    choice(name: 'ENVIRONMENT', choices: ['dev', 'prod'], description: ' Select environmentL ')
    }
  stages {
    stage("build"){
      steps{
        echo"Building the application ${INSTANCE_NAME}"
      }
    }
    stage("test"){
      steps{
        echo"Testing the application, ${REGION}"
      }
    }
    stage("deploy"){
      steps{
        echo"Deploing the application, ${ENVIRONMENT}"
      }
    }    
  
  }

}
