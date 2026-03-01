from airflow import DAG
from airflow.operators.Bash import BashOperator
from datetime import datetime,timedelta

with DAG(
    default_args={
        'start_date': datetime(2026, 1, 13),
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    dag_id='New_learning_dag',
    schedule='@daily',
    catchup=False,
) as dag:

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "This is task 1"',
    )

    task2 = BashOperator(
        task_id='task2',
        bash_command='echo "This is task 2"',
    )

    task3 = BashOperator(
        task_id='task3',
        bash_command='echo "This is task 3"',
    )

    # Define task dependencies
task1 >> task2 
task1 >> task3