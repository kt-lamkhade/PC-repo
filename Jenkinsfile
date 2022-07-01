pipeline{
  agent any
  parameters{
    string(name: 'instance_name', defaultValue: '', description: 'Please mention name of instance: ')
    choice(name: 'region', choices: ['us-ease-1', 'us-east-2'], description: 'Select Region for deployment: ')
    choice(name: 'environment', choices: ['dev', 'prod'], description: ' Select environmentL ')
    }
  stages {
    stage("build"){
      steps{
        echo"Building the application ${instance_name}"
      }
    }
    stage("test"){
      steps{
        echo"Testing the application, ${region}"
      }
    }
    stage("deploy"){
      steps{
        echo"Deploing the application, ${environment}"
      }
    }    
  
  }

}
