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
                python3 -m venv ~/jenkins_env
                source ~/jenkins_env/bin/activate
                pip install --upgrade pip
                pip install pylint
                pylint /var/lib/jenkins/workspace/pylint@script/files/*.py || exit 0
                #pylint --output-format=colorized
                #pylint --output-format=parseable --reports=no module > pylint.log || echo "pylint exited with")
                echo 'pylint command 1 executed'
                """
            }
            
        }
        stage('Code Scan - Python') {
		steps{
			script {
				sh '''
				echo 'in code scan'
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
