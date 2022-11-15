# import the librarias
import logging
import logging.config
from datetime import timedelta
from airflow import DAG
import pandas as pd
from cfg import default_args

# El path
path = '{aca el path donde se encuentra la carpeta}'
# creando logger airflow
airflow_logger = logging.getLogger('airflow.task')
# creando logger custom
custom_logger = logging.getLogger('custom')
custom_logger.setLevel(logging.INFO)
# formatter
log_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d')
# filehandler
fh = logging.FileHandler(f'{path}/logs.log')
fh.setLevel(logging.INFO)
fh.setFormatter(log_format)
# treamhandler
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
sh.setFormatter(log_format)
# agregando handleres al logger
custom_logger.addHandler(fh)
custom_logger.addHandler(sh)

dag = DAG(
 'DAG_Unidad_5',
 default_args=default_args,
 description='My first DAG',
 schedule_interval=timedelta(days=1),
)

# Tasks


@dag.task(task_id="read_top10")
def read_top10():

    # ----- Completar logging ------
    custom_logger.info('[*] Descargando archivo, loggeando con custom logger')
    airflow_logger.info('[*] Descargando archivo, loggeando con airflow')
    # -----Fin Completar logging ------

    # Read CSV from web
    url = "http://winterolympicsmedals.com/medals.csv"

    try:

        df = pd.read_csv(url)

        # Get top 10 countries with most medals
        top_countries = df.NOC.value_counts().sort_values(ascending=False)\
            .head(10)

        # Convert pandas series to data frame
        to_countries_df = top_countries.to_frame()

        # Save data frame in Excel format
        # Completar tu propia ubicación para guardar el archivo de salida
        to_countries_df.to_excel(f'{path}/top10_medals_by_country.xlsx')

        # Logging message INFO Success --- Completar
        custom_logger.info('[+] Tarea procesada exitosamente')
        airflow_logger.info('[+] Tarea procesada exitosamente')
    except Exception:
        # Logging message ERROR Fail --- Completar
        custom_logger.error('[-] Fallo descarga', exc_info=True)
        airflow_logger.error('[-] Fallo descarga', exc_info=True)
        logging.exception('[-] Fallo descarga, logging exception')

# task pipeline


read_top10()
