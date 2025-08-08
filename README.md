# 🌦️ AWS ETL Weather Data Pipeline

This project is an **ETL (Extract, Transform, Load)** pipeline built in **Python**, designed to fetch real-time weather data for cities in Tamil Nadu using the **OpenWeatherMap API**, transform the JSON into structured CSV format, and store it on **AWS S3**.

---

## 📌 Features

- 🔄 Scheduled daily with **cron** on an EC2 instance
- ☁️ Connects to **OpenWeather API** to fetch weather data
- 🔧 Transforms JSON → CSV
- 📤 Uploads clean data to **AWS S3**
- 📦 Designed with portability and simplicity

---

## 🏗️ Architecture

```plaintext
+-------------+        +---------------------+        +----------------+
|  EC2 Server | ---->  |  Python ETL Script  | ---->  |     AWS S3     |
+-------------+        +---------------------+        +----------------+
       |                         |                            |
       |                                                      |
       |                Fetch weather data                    |
       |                         |                            |
       |                                                      |
       |              Transform JSON → CSV                    |
       |                         |                            |
       |                                                      |
       |__            Upload to S3 bucket                   __|



🧪 Tech Stack
Language: Python 3.x

Cloud Services: AWS EC2, AWS S3

Scheduler: cron

API: OpenWeatherMap

File Formats: JSON, CSV


📁 Project Structure

aws_etl/
├── weather_etl.py           # Main ETL script
├── config.py                # Contains API keys and settings
├── utils.py                 # Helper functions (optional)
├── cities.txt               # List of Tamil Nadu cities
├── cron.log                 # Logs from cron jobs
├── requirements.txt         # Dependencies
└── venv/                    # Python virtual environment



⚙️ Setup Instructions
1. ✅ Prerequisites
AWS account with:

An S3 bucket created

An EC2 instance (Ubuntu recommended)

An API key from OpenWeatherMap


2. 💻 Installation
SSH into your EC2 and follow:

sudo apt update && sudo apt install python3-pip -y
git clone <your-repo-url>
cd aws_etl
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


3. 🔑 Configuration
Edit config.py:

API_KEY = "your_openweather_api_key"
S3_BUCKET = "your-s3-bucket-name"
REGION = "your-aws-region"


4. 📆 Schedule via Cron
Open crontab:

crontab -e
Add this line to run the ETL script daily at 2:30 AM:

30 2 * * * /home/ubuntu/aws_etl/venv/bin/python /home/ubuntu/aws_etl/weather_etl.py >> /home/ubuntu/aws_etl/cron.log 2>&1
📊 Sample Output
Uploaded file in S3:


weather_tamilnadu_2025-08-08.csv
Sample rows:

City	Temp (°C)	Weather	Humidity (%)	Wind Speed
Chennai	32.5	Clear	60	3.5 m/s
Madurai	30.2	Cloudy	65	2.8 m/s
Coimbatore	29.8	Rain	70	4.2 m/s

🚀 Future Improvements
Add Airflow or Prefect for scheduling instead of cron

Store in AWS RDS or Redshift for queryable analytics

Add email notifications on job success/failure

Include data validation and unit tests

🧠 Learnings
✅ How to build a full ETL pipeline
✅ How to interact with REST APIs in Python
✅ How to use cron and automate on EC2
✅ How to store structured data in S3
