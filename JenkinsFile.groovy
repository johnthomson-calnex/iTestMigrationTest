pipeline {
    agent any

    stages {
        stage('test_1') {
            steps {
                python %Test_To_Run%
            }
        }
    }
}
