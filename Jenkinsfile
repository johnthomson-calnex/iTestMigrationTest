pipeline {
    agent any

    environment {
        test_to_run = 't.py'
        ip = '100g-vm1'
    }

    stages {
        stage('test_1') {
            steps {
                python %test_to_run%
            }
        }
    }
}
