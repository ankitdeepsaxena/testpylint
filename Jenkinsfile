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
                python3 -m pylint --fail-under=4.0 --output-format=colorized --score=y /var/lib/jenkins/workspace/pylint/files/*py
                """
            }            
        }
        stage("Pytest") {
        steps {
            sh """
            pip3 install pytest
            python3 -m pytest --version
            pip3 install coverage
            pytest /var/lib/jenkins/workspace/pylint/tests/*
            coverage run -m pytest /var/lib/jenkins/workspace/pylint/tests/*
            coverage report -m
            """
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
