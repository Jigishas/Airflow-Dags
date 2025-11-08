from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'jose',
    'retries':4,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='new dag',
    default_args=default_args,
    description='This is my new DAG',
    start_date=datetime(2025, 11, 10),
    schedule_interval='@daily',


)as dag:
    task1=BashOperator(
        task_id='my new dag',
        bash_command="echo this is a new dag now!"
    )
