import requests
from bs4 import BeautifulSoup

image_number = 0
storage_number = 1
link = f"https://zastavok.net"
# Названия прогона
run = "ц"
# Кол-во страниц для парсинга
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

        print(f"Изображение номер:{image_number} скачено")
        image_number += 1
    storage_number += 1