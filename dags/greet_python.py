from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta

default_args= { 
    'owner':'jose',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

def greet():
    print("hello there !")

with DAG (
    dag_id='python_greet',
    default_args=default_args,
    description='this is a DAG python operator',
    start_date=datetime(2026, 1, 12 ),
    schedule_interval='@daily'
    ) as dag:
    task1=PythonOperator(
        task_id='greet',
        python_callable=greet

    )

    task1