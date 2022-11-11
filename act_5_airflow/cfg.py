from datetime import timedelta
from airflow.utils.dates import days_ago

# defining DAG arguments
default_args = {
 'owner': 'Alkemy_Prisma',
 'start_date': days_ago(0),
 'email': ['some@somemail.com'],
 'email_on_failure': False,
 'email_on_retry': False,
 'retries': 1,
 'retry_delay': timedelta(minutes=5),
}
