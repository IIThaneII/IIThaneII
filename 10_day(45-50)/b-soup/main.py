from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_we_page = response.text

soup = BeautifulSoup(yc_we_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)
article_upvote = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

max_points_index = article_upvote.index(max(article_upvote))
print(article_texts[max_points_index])
print(article_links[max_points_index])