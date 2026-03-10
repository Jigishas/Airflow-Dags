from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'jose',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def extract():
    print("This is the extract task")
    data = [1, 2, 3, 4, 5]
    print(f"Extracted data: {data}")
with DAG(
    dag_id='etl_dag',
    default_args=default_args,
    description='A simple ETL DAG',
    start_date=datetime(2026, 1, 12),
    schedule_interval='@daily'
) as DAG:
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract
    )

extract_task    