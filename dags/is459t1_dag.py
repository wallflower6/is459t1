from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from datetime import datetime
from twitter_scraper import run_etl
from twitter_translator import run_translator

default_args = {
    'owner': 'lindy',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 2
}

dag = DAG(
    dag_id='is459_t1',
    default_args=default_args,
    catchup=False,
    schedule_interval='@once',
)

# CREATE TASK 1
task1 = PythonOperator(
    task_id='twitter_scraper',
    python_callable=run_etl,
    dag=dag,
)

# CREATE TASK 2
task2 = PythonOperator(
    task_id='twitter_translator',
    python_callable=run_translator,
    dag=dag,
)

# CREATE EXECUTION SEQUENCE
task1 >> task2