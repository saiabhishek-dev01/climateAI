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
```bash
git clone https://github.com/saiabhishek-dev01/climateAI.git
cd climateAI

