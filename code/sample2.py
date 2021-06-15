import os
import json
from airflow.models.dag import DAG
#from airflow.operators.python import PythonOperator
#from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.operators.s3_bucket import S3CreateBucketOperator, S3DeleteBucketOperator
from airflow.utils.dates import days_ago
from datetime import datetime
import boto3
from airflow.operators.dummy import DummyOperator    
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.operators.s3_bucket import S3CreateBucketOperator
BUCKET_NAME = os.environ.get('BUCKET_NAME', 'test-airflow-gabdu')
key = 'dev/param/variables.json'
BUCKET_VARIABLE_NAME=''
s3 = boto3.resource('s3')
default_args = {
    'start_date': datetime(2020, 1, 1)
}

dag = DAG(
    'airflow_variable_test', default_args=default_args, 
    schedule_interval=None,catchup=False)

with dag:
    task_1 = DummyOperator(task_id = 'Start', dag = dag)

    create_bucket = S3CreateBucketOperator(
        task_id='s3_bucket_dag_create',
        bucket_name="Test-jordi-aiiiiiiiiii",
        region_name='us-east-1',dag=dag
    )
    
    
    task_1 >>  create_bucket
