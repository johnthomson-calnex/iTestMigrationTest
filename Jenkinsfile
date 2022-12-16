pipeline {
  agent any
  parameters { string(name: 'JSON',  description: '')
      
  }
  stages {
      stage ("Example") {
        steps {
         script{
            def jsonObj = readJSON text: "${params.JSON}", returnPojo: true
            def ip = jsonObj['ip']
            for(String test : jsonObj['Tests']){
                bat "python $test $ip"
            } 
             
        }
      }
  }
}
}