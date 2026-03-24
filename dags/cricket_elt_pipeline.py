from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from datetime import datetime, timedelta

from scripts.extract import fetch_cricket_data
from scripts.load_s3 import upload_to_s3
from scripts.load_gsheet import upload_to_gsheet
from scripts.redshift_load import load_to_redshift

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

def run_pipeline():
    data = fetch_cricket_data()
    upload_to_s3(data)
    upload_to_gsheet(data)

def run_redshift():
    load_to_redshift()

with DAG(
    dag_id="cricket_elt_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule_interval="@hourly",
    catchup=False
) as dag:

    extract_load = PythonOperator(
        task_id="extract_load",
        python_callable=run_pipeline
    )

    s3_sensor = S3KeySensor(
        task_id="wait_for_s3",
        bucket_name="your-bucket-name",
        bucket_key="cricket_*.json",
        aws_conn_id="aws_default",
        poke_interval=60,
        timeout=600
    )

    redshift_task = PythonOperator(
        task_id="load_redshift",
        python_callable=run_redshift
    )

    extract_load >> s3_sensor >> redshift_task
