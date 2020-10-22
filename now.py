import requests
from bs4 import BeautifulSoup
import time

# Traffic-weather-News
link = "https://yandex.ru/"
response = requests.get(link).text
soup = BeautifulSoup(response, "lxml")

# Weather
weather = soup.find("div", "widget__content weather__content-outer")
weather_now = weather.find("a").get("aria-label")

# night-evening
weather_all = weather.find("div", "weather__forecast").text

# Traffic
traffic = soup.find("div", "traffic__content widget__content")
traffic_number = traffic.find("div", "traffic__rate-text").text
traffic_now = traffic.find("div", "traffic__forecast")
traffic_text = traffic_now.find("a").text

# News
new = soup.find("ol", "list news__list")
news_block = new.find_all("span", "news__item-content")

time_now = time.localtime()
with open("Now.txt", "w") as file:
    file.write(f"Сейчас:{weather_now},{weather_all}\n"
               f"Пробки:{traffic_number} балла "
               f"{traffic_text}\n")
    file.write("Новости:\n")
    x = 1
    for news in news_block:
        a = str(news).rstrip("</span>").lstrip('<span class="news__item-content">')
        file.write(f"{x}) {a}\n")
        x += 1
    file.write(f"{time_now.tm_hour}:"
               f"{time_now.tm_min}:{time_now.tm_sec}")

print(f"Completed! {time_now.tm_hour}:"
      f"{time_now.tm_min}:{time_now.tm_sec}")
