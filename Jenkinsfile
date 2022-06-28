pipeline{
  agent any
  parameters{
    string(name: 'instance_name', defaultValue: '', description: '')
    choice(name: 'region', choices: ['us-ease-1', 'us-east-2'], description: '')
    choice(name: 'environment', choices: ['dev', 'prod'], description: '')
    }
  stages {
    stage("build"){
      steps{
        echo"Building the application ${instance_name}"
      }
    }
    stage("test"){
      steps{
        echo'Testing the application, ${region}"
      }
    }
    stage("deploy"){
      steps{
        echo'Deploing the application, ${environment}'
      }
    }    
  
  }

}
