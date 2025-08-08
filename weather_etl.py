import requests
import json
import boto3
import csv
import os
from datetime import datetime
from config import API_KEY, BUCKET_NAME

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
CITIES_FILE = "cities/tamilnadu_cities.txt"
LOG_FILE = "logs/etl.log"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {msg}\n")

def extract(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        filename = f"{RAW_DIR}/{city}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump(data, f)
        return data
    except Exception as e:
        log(f"❌ Error extracting for {city}: {str(e)}")
        return None

def transform(data_list):
    csv_data = []
    for data in data_list:
        if data:
            row = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "weather": data["weather"][0]["main"],
                "datetime": datetime.utcnow().isoformat()
            }
            csv_data.append(row)
    return csv_data

def save_csv(data):
    filename = f"{PROCESSED_DIR}/weather_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return filename

def upload_to_s3(filename):
    s3 = boto3.client("s3")
    key = f"weather_data/{os.path.basename(filename)}"
    s3.upload_file(filename, BUCKET_NAME, key)
    log(f"✅ Uploaded {filename} to S3 as {key}")

def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    with open(CITIES_FILE) as f:
        cities = [line.strip() for line in f if line.strip()]

    all_data = []
    for city in cities:
        data = extract(city)
        if data and data.get("cod") == 200:
            all_data.append(data)
        else:
            log(f"⚠️ Invalid data for {city}")

    if all_data:
        transformed = transform(all_data)
        csv_file = save_csv(transformed)
        upload_to_s3(csv_file)

if __name__ == "__main__":
    main()
