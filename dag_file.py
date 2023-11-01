from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.operators.python_operator import PythonOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 11, 1),
    'depends_on_past': False,
    'retries': 1,
}

# Create an instance of the DAG
dag = DAG(
    'data_processing_dag',
    default_args=default_args,
    schedule_interval=None,  # Set your desired schedule interval or None for manual triggering
    catchup=False,
    max_active_runs=1,
)

# Task to run download_data.py
download_data_task = BashOperator(
    task_id='download_data',
    bash_command='python /path/to/download_data.py',
    dag=dag,
)

# Task to run extractData.py
extract_data_task = BashOperator(
    task_id='extract_data',
    bash_command='python /path/to/extractData.py',
    dag=dag,
)

# Task to run mapper.py and reducer_daily1.py
process_data_task = BashOperator(
    task_id='process_data',
    bash_command='python /path/to/mapper.py && python /path/to/reducer_daily1.py',
    dag=dag,
)

# Task to copy the resulting file back to the local system
copy_file_task = BashOperator(
    task_id='copy_file',
    bash_command='docker cp hadoop-master:/path/to/output.csv /path/to/local/output.csv',
    dag=dag,
)

# Define task dependencies
download_data_task >> extract_data_task >> process_data_task >> copy_file_task
