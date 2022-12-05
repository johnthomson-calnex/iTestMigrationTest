pipeline {
    agent any

    environment {
        Test_To_Run = 't.py'
        ip = '100g-vm1'
    }

    stages {
        stage('test_1') {
            steps {
                python %Test_To_Run%
            }
        }
    }
}
