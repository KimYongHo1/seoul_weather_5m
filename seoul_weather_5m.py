# 5분마다 한 번식 서울의 기온 정보를 csv형태로 저장
import requests
import csv
from datetime import datetime
import os

MY_API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Seoul"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={MY_API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

temp = data["main"]["temp"]
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

csv_filenam = "seoul_weather.csv"
header = ["time", "temp"]

file_exist = os.path.isfile(csv_filename)
with open(csv_filename, "a", newline="") as file:
  writer = csv.writer(file)

  if not file_exist:
    writer.writerow(header)

  writer.writerow([time, temp])

  print("서울 기온 저장 완료!!")


