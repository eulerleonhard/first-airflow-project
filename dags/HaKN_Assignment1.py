from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.time_delta import TimeDeltaSensor

default_args = {
    'owner': 'airflow',
    'depend_on_past': False,
    'start_date': datetime(2023, 1, 1),
    # 'retries': 1
}

with DAG(
    'multi_task_dag',
    default_args=default_args,
    description='Assignment 1',
    schedule_interval=timedelta(minutes=30),
    catchup=False,
) as dag:
    # T1
    t1 = TimeDeltaSensor(
        task_id='wait_5m',
        delta=timedelta(minutes=5)
    )
    # T2
    t2 = BashOperator(
        task_id='execution_date_bash',
        bash_command='echo "Execution date: {{ execution_date.strftime(\'%Y-%m-%d %H:%M:%S\') }}"',
    )

    # T3
    def print_world(execution_date, **kwargs):
        one_hour_later = execution_date + timedelta(hours=1)
        print(f"Execution date with one hour added: {one_hour_later.strftime('%Y-%m-%d %H:%M:%S')}")

    t3 = PythonOperator(
        task_id='execution_date_python',
        python_callable=print_world,
    )

# Set the task dependencies
t1 >> t2 >> t3