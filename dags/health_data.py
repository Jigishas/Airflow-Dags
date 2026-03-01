from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

args={
    owner:"jose",
    start_date: datetime(2026,2,28),
    retry_delay:timedelta(minutes=5),
    retries:5
}
def extract_data():
    print("Extracting data...")
    with open('https://www.who.int/data/inequality-monitor/data', 'r') as f:
        data = f.read()
        print(data)
        return data
    


    with DAG(
     dag_Id="extraction",
     default_args=args,
     description="extraction from online",
     start_date=datetime(2026,2,7)


 ) as dag:
        task1=PythonOperator(
        taskId="extract the data",
        python_callable=extract_data,
    )
task1