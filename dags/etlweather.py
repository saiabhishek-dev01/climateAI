from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago
from airflow.providers.postgres.hooks.postgres import PostgresHook
import requests
import logging

# Define constants
LATITUDE = '51.5074'
LONGITUDE = '-0.1278'
API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true"
POSTGRES_CONN_ID = 'postgres_default'

# Default arguments for Airflow DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 2  # Retries the task if it fails
}

# Define the DAG
with DAG(
    dag_id='weather_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    @task()
    def extract_weather_data():
        """Extracts weather data from Open-Meteo API."""
        try:
            response = requests.get(API_URL, timeout=10)  # Set timeout for reliability
            response.raise_for_status()  # Raise an error for bad responses
            
            data = response.json()
            if "current_weather" not in data:
                raise ValueError("Invalid API response: 'current_weather' key is missing")

            logging.info(f"Extracted data: {data}")
            return data["current_weather"]

        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            raise Exception(f"API request failed: {e}")

    @task()
    def transform_weather_data(weather_data):
        """Transforms extracted weather data."""
        transformed_data = {
            'latitude': LATITUDE,
            'longitude': LONGITUDE,
            'temperature': weather_data.get('temperature'),
            'windspeed': weather_data.get('windspeed'),
            'winddirection': weather_data.get('winddirection'),
            'weathercode': weather_data.get('weathercode')
        }
        logging.info(f"Transformed data: {transformed_data}")
        return transformed_data

    @task()
    def load_weather_data(transformed_data):
        """Loads transformed data into PostgreSQL database."""
        try:
            pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
            conn = pg_hook.get_conn()
            cursor = conn.cursor()

            # Create table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS weather_data (
                    id SERIAL PRIMARY KEY,
                    latitude FLOAT,
                    longitude FLOAT,
                    temperature FLOAT,
                    windspeed FLOAT,
                    winddirection FLOAT,
                    weathercode INT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Insert transformed data into table
            cursor.execute("""
                INSERT INTO weather_data (latitude, longitude, temperature, windspeed, winddirection, weathercode)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (
                transformed_data['latitude'],
                transformed_data['longitude'],
                transformed_data['temperature'],
                transformed_data['windspeed'],
                transformed_data['winddirection'],
                transformed_data['weathercode']
            ))

            conn.commit()
            cursor.close()
            conn.close()
            logging.info("Data successfully loaded into PostgreSQL.")

        except Exception as e:
            logging.error(f"Database operation failed: {e}")
            raise Exception(f"Database operation failed: {e}")

    # Define DAG dependencies (workflow)
    weather_data = extract_weather_data()
    transformed_data = transform_weather_data(weather_data)
    load_weather_data(transformed_data)
