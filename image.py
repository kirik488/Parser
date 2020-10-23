import requests
from bs4 import BeautifulSoup
import time

print("By default, two pages are download(36 image)")
image_number = 1
storage_number = 1
link = f"https://zastavok.net"
# Name run
run = time.strftime("%d.%b.%y.")
# Pages for parsing
for storage in range(2):
    response = requests.get(f"{link}/{storage_number}").text
    soup = BeautifulSoup(response, "lxml")
    block = soup.find("div", "block-photo")
    all_image = block.find_all("div", "short_full")

    for image in all_image:
        image_link = image.find("a").get("href")
        download = requests.get(f"{link}{image_link}").text
        download_soup = BeautifulSoup(download, "lxml")
        download_block = download_soup.find("div","image_data").find("div", "block_down")
        result_link = download_block.find("a").get("href")

        image_bytes = requests.get(f"{link}{result_link}").content

        with open(f"image/{run}{image_number}.jpg","wb") as file:
            file.write(image_bytes)

        print(f"Image: {run}{image_number} downloaded")
        image_number += 1
    storage_number += 1
print("End!")
