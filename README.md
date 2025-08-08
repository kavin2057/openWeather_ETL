🌦️ AWS Weather ETL Pipeline
This project builds an end-to-end ETL pipeline to fetch real-time weather data from the OpenWeatherMap API for all cities in Tamil Nadu, India, transform it into a clean CSV format, and upload it to an AWS S3 bucket using a scheduled cron job on an EC2 instance.

🚀 Features
✅ Extract weather data via OpenWeatherMap API

✅ Transform JSON to CSV

✅ Save weather data daily with date-wise filenames

✅ Upload to AWS S3 using boto3

✅ Fully automated via Scheduling job using Apache Airflow on EC2

✅ Cost-effective: Built entirely on AWS Free Tier

📁 Project Structure

aws_etl/
│
├── cities.py             # Tamil Nadu cities list
├── weather_etl.py        # Main ETL logic
├── config.py             # API key and S3 bucket config
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation (you’re here!)


🛠️ Tech Stack
Component	Tool
Programming	Python
Cloud Platform	AWS (S3 + EC2)
Scheduler	Cron (on Ubuntu EC2 instance)
Storage Format	CSV
Data Source	OpenWeatherMap API

🧩 Setup Instructions
1️⃣ Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/aws-weather-etl.git
cd aws-weather-etl
2️⃣ Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Configure Settings
Edit config.py with your API key and S3 bucket:

python
Copy
Edit
API_KEY = "your_openweather_api_key"
BUCKET_NAME = "your-s3-bucket-name"
4️⃣ Run the Script Manually (for testing)
bash
Copy
Edit
python3 weather_etl.py
⏰ Automate with Cron (on EC2)
Edit your crontab:

bash
Copy
Edit
crontab -e
Add the following line to run the ETL script daily at 7:30 AM:


30 7 * * * /usr/bin/python3 /home/ubuntu/aws_etl/weather_etl.py >> /home/ubuntu/aws_etl/cron.log 2>&1
🧪 Output Example
CSV Output:

csv

city,temperature,humidity,weather,datetime
Chennai,32.5,65,Clear,2025-08-08 07:30:00
Madurai,33.2,60,Cloudy,2025-08-08 07:30:00


📦 Sample S3 File Structure
arduino

s3://your-bucket-name/
├── weather_data/
│   ├── weather_2025-08-08.csv
│   ├── weather_2025-08-09.csv
│   └── ...


📌 Why This Project Matters
This mini project demonstrates how real-world Data Engineering works:

Real-time data fetching

Data cleaning and transformation

Cloud storage and automation

Infrastructure and cost-awareness

Perfect as a beginner-friendly portfolio project for data engineers and cloud learners!

📚 Credits
OpenWeatherMap API — openweathermap.org

AWS Free Tier — EC2, S3

🙌 Author
Kavin — Aspiring Cloud Data Engineer
