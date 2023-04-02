from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python_operator import PythonOperator

# First we write our python logic

# Defining a function: print the current datetime
def current_datetime():
    print(datetime.now())



# Create the DAG which calls the python logic above
default_dag_args = {
    'start_date': datetime(2023, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1,
}

with DAG('Exercise_02_DAG', schedule_interval='@daily', catchup=False, default_args=default_dag_args) as dag_python:

    # Here we define our task
    task_00 = PythonOperator(task_id = 'print_current_datetime', python_callable = current_datetime)
