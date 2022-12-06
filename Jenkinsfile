pipeline {
    agent any

    environment {
        test_to_run = 'set_ccsa.py'
        ip = '100g-vm1'
        test2_to_run = 'PTP/set_cmcc5g.py'
    }

    stages {
        stage('CCSA') {
            steps {
                bat 'python %test_to_run%' 
            }
        }
        stage('CMCC5G') {
            steps {
                sleep 5
                bat 'python %test2_to_run%'
            }
        }
    }
}
