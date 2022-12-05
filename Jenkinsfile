pipeline {
    agent any

    environment {
        test_to_run = 't.py'
        ip = '100g-vm1'
        test2_to_run = 'PTP/t2.py'
    }

    stages {
        stage('test_1_t.py') {
            steps {
<<<<<<< HEAD
                bat 'python %test_to_run%' 
=======
                bat 'python %test_to_run%'
>>>>>>> ce5513f319095724c8f3d7fa92319596eac109ed
            }
        }
        stage('test_2_t2.py') {
            steps {
                sleep 5
                bat 'python %test2_to_run%'
            }
        }
    }
}
