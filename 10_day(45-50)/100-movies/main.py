import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
the_100_mv_page = response.text

soup = BeautifulSoup(the_100_mv_page, "html.parser")
movies_list = soup.find_all(name="h3", class_="title")
movies_list_reverse = movies_list.reverse()

with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/10_day(45-50)/100-movies/list.txt", mode="w", encoding="utf-8") as f:
    for movie in movies_list:
        f.write(f"{movie.getText()}\n")