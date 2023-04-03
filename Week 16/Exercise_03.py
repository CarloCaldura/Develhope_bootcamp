import requests 
import time 
import json 
from airflow import DAG 
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.python import BranchPythonOperator 
from airflow.operators.dummy import DummyOperator

from datetime import datetime, timedelta 

# exercise: write a DAG which is able to request market data for a list of stocks.
# you DAG should only have one task (?)
def get_data(tickers): 
    api_key = "H1IUEGJIML21MR9E"
    # Replace the DEMO apikey with your own key
    for ticker in tickers:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker +  '&interval=5min&apikey=' + api_key
        r = requests.get(url)
        try:
            data = r.json()
            path = '/home/carlo/airflow/DATA/RAW_DATA/'
            with open(path + 'stock_market_raw_data_' + ticker + '_' + str(time.time()), 'w') as outfile:
                json.dump(data, outfile)
        except:
            return ('Something went worn with the get_data function')

default_dag_args = { 
    'start_date': datetime(2022, 9, 1), 
    'email_on_failure': False, 
    'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=5), 
    'project_id': 1 
}

tickers = ['IBM', 'TSLA', 'META']
#crontab notation can be useful https://crontab.guru/#0_0_*_*_1
with DAG("Exercise_03_DAG", schedule_interval = '@daily', catchup=False, default_args = default_dag_args) as dag_python:
    
    task_0 = PythonOperator(task_id = "get_market_data_list_of_tickers", python_callable = get_data, op_kwargs = {'tickers' : tickers})
