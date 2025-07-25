from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime


def print_hello():
    print("Hello, world!")


def print_time():
    print(f"Current time is {datetime.utcnow()}")


with DAG(
    dag_id="hello_world",
    start_date=datetime(2023, 1, 1),
    schedule_interval="*/10 * * * *",
    catchup=False,
) as dag:

    start = BashOperator(
        task_id="start",
        bash_command="echo 'Starting workflow'",
    )

    hello_task = PythonOperator(
        task_id="hello",
        python_callable=print_hello,
    )

    time_task = PythonOperator(
        task_id="print_time",
        python_callable=print_time,
    )

    end = BashOperator(
        task_id="end",
        bash_command="echo 'Workflow complete'",
    )

    start >> hello_task >> time_task >> end
