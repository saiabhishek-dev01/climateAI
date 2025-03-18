# 🌍⚡ Multi-Source ETL Pipeline for Weather & Air Quality Data  

🚀 **A Scalable Data Sciene Pipeline Integrating Multiple APIs to Aggregate Weather & Air Quality Data into PostgreSQL**  

---

## 🏗 Project Overview  
This project is an **end-to-end multi-source ETL pipeline** that **automates the extraction, transformation, validation and loading (ETL) of weather and air quality data** from multiple sources into **PostgreSQL** using **Apache Airflow**.  

This **scalable data pipeline** integrates information from:  

✅ **Open-Meteo API** → Temperature, Wind Speed, Weather Code  
✅ **NOAA API** → Humidity, Precipitation, Wind Speed  
✅ **NASA POWER API** → Solar Radiation, Cloud Coverage  
✅ **IQAir API** → Air Quality Index (AQI), PM2.5, PM10, CO Levels  

🔹 Designed to handle **real-time and historical data**  
🔹 Implements **data validation & consistency checks**  
🔹 Uses **PostgreSQL for structured storage**  
🔹 Fully **automated with Apache Airflow DAGs**  

---

## 📸 Flow of the project  
### 🔹 ETL DAG Workflow in Apache Airflow  
<img width="523" alt="image" src="https://github.com/user-attachments/assets/3555dc46-33bb-49ac-9577-72f242ceb75d" />



---

## 🏗 Project Architecture  
### 🔹 End-to-End ETL Pipeline Architecture  

                      +--------------+
                      |    User      |
                      +------+-------+
                             |
                             v
             +--------------------------------+
             |       Airflow Scheduler       |
             +--------------------------------+
               |        |        |       |
               v        v        v       v
    +----------+   +----------+   +----------+   +----------+
    | OpenMeteo |  |   NOAA   |   |  NASA    |   |  IQAir   |
    +----------+   +----------+   +----------+   +----------+
               |        |        |       |
               v        v        v       v
             +--------------------------------+
             |       Data Transformation      |
             +--------------------------------+
                             |
                             v
                  +--------------------+
                  | PostgreSQL Database |
                  +--------------------+


---

## ⚙ Tech Stack  
- **Apache Airflow** (Orchestrating the ETL pipeline)  
- **PostgreSQL** (Storing the structured data)  
- **Python** (Data extraction, transformation, and validation)  
- **Docker** (Containerizing the Airflow instance)  
- **APIs:** Open-Meteo, NOAA, NASA POWER, IQAir  

---

## 🚀 Installation & Setup  
### **1️⃣ Clone the Repository**  
git clone https://github.com/saiabhishek-dev01/climateAI.git
cd climateAI


### **2️⃣ Set Up Environment Variables**
Before running the ETL pipeline, configure Airflow Connections:

Go to **Apache Airflow** UI (http://localhost:8080)
Navigate to **Admin → Connections**
Add the following connections:

Conn ID	Conn Type	Host URL	Extra (if needed)

**open_meteo_api** :	http	https://api.open-meteo.com/	-
**noaa_api** :	http	https://api.weather.gov/	-
**nasa_power_api** :	http	https://power.larc.nasa.gov/	-
**iqair_api** :	http	https://api.airvisual.com/	{"apikey": "your_api_key_here"}
**postgres_default** :	Postgres	your_postgres_host	Database: postgres, Login: postgres, Password: **your_password** Port: 5432

### **3️⃣ Start the Airflow Scheduler & Webserver**

astro dev start


### **4️⃣ Trigger the DAG**

Go to **Apache Airflow UI** (http://localhost:8080) → **DAGs** → **multi_source_weather_pipeline** → **Trigger DAG**.

---




