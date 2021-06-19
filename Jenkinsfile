pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ankitdeepsaxena/testpylint.git']]])
            }
        }
        stage('Pylint'){
            steps {
                sh """
                echo 'Checkout Done'
                pip3 install pylint &> /dev/null
                python3 -m pylint --version
                python3 -m pylint --fail-under=4.0 --output=/var/lib/jenkins/workspace/pylint/pylint.log --output-format=colorized --score=y /var/lib/jenkins/workspace/pylint/files/*py
                """
            }            
        }
        stage("Pytest") {
        steps {
            sh """
            pip3 install pytest &> /dev/null
            python3 -m pytest --version
            pip3 install coverage &> /dev/null
            python3 -m coverage --version
            python3 -m pytest /var/lib/jenkins/workspace/pylint/tests/*
            python3 -m coverage run -m pytest /var/lib/jenkins/workspace/pylint/tests/test_*.py
            python3 -m coverage report -i
            #coverage report -i
            """
            }
        }
        stage('Build') {
            steps {
                script {
                    echo "currentResult: ${currentBuild.currentResult}"
                    sh """#!/usr/bin/env bash
                            set -e
                            echo 'I AM STAGE TWO AND I SHOULD  BE EXECUTED'
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
