pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ankitdeepsaxena/testpylint.git']]])
            }
        }
        stage('Pre-build'){
            steps {
                sh """
                echo 'Checkout Done'
                pip3 install pylint
                python3 -m pylint --version
                ls /var/lib/jenkins/workspace/
                ls /var/lib/jenkins/workspace/pylint/
                ls /var/lib/jenkins/workspace/pylint/files/
                echo 'pylint command 1 executed'
                python3 -m pylint --fail-under=4.0 /var/lib/jenkins/workspace/pylint/files/*py
                """
            }
            
        }
        stage('Code Scan - Python') {
		steps{
			script {
				sh '''
				echo 'in code scan'
                python3 -m pylint --output-format=parseable --fail-under=4.0 module --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" | tee pylint.log || echo "pylint exited with $?"
                echo "linting Success, Generating Report"
                recordIssues enabledForFailure: true, aggregatingResults: true, tool: pyLint(pattern: 'pylint.log')
				'''
			}
		}
	}
        stage('Build') {
            steps {
                script {
                    echo "currentResult: ${currentBuild.currentResult}"
                    sh """#!/usr/bin/env bash
                            set -e
                            echo 'I AM STAGE TWO AND I SHOULD NOT BE EXECUTED'
                            """
                }
            }

        }
        stage ('CleanUp'){
            steps{
            echo "We are donesss"
            }
        }
    }
}
