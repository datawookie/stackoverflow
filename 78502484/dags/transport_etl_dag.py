from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta
import json
import os
from scripts.utensils import get_snowpark_session

print("Done!")
