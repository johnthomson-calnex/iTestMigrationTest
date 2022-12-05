pipeline {
    agent any

    environment {
        test_to_run = 't.py'
        ip = '100g-vm1'
        test2_to_run = 'PTP/t2.py'
    }

    // parameters {
    //     string(name : 'test_to_run', defaultValue : 't.py')
    //     string(name : 'ip', defaultValue : '100g-vm1')
    //     string(name : 'test2_to_run', defaultValue : 'PTP/t2.py')
    // }

    stages {
        stage('test_1_t.py') {
            steps {
                bat 'python %params.test_to_run%'
            }
        }
        stage('test_2_t2.py') {
            steps {
                sleep 5
                bat 'python %params.test2_to_run%'
            }
        }
    }
}
