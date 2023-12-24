from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta



MY_NAME = "hiep"
EXAMPLE_NUMBER = 12

def multiply_by_23(number: int) -> int:
    """Multiply the passed number by 23 and return the result to Airflow logs"""
    result = number * 23
    print(result)


with DAG(
    dag_id="hiep_dag",
    start_date=datetime(2021, 1, 1),
    schedule=timedelta(minutes=15),
    catchup=False,
    tags=["test"],
    default_args={
        "owner": MY_NAME,
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
    }
) as dag:
    
    t1 = BashOperator(
        task_id="say_my_nameeee",
        bash_command=f"echo {MY_NAME}",
    )

    t2 = PythonOperator(
        task_id="multiply_my_number_by_23",
        python_callable=multiply_by_23,
        op_kwargs={"number": EXAMPLE_NUMBER},
    )

    t1 >> t2
    
