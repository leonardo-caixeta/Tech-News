import re
from bs4 import BeautifulSoup
from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    time.sleep(1)
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news_urls = selector.xpath("//header/h2/a/@href").getall()  # NOQA
    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.xpath(
        '//*[@id="main"]/div/nav/div/a[3]/@href'
    ).get()  # NOQA
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    url = soup.find("link", {"rel": "canonical"})["href"]
    title = soup.find("h1", {"class": "entry-title"}).text.strip()
    timestamp = soup.find("li", {"class": "meta-date"}).text
    writer = soup.find("span", {"class": "author"}).a.text
    reading_time_str = soup.find("li", {"class": "meta-reading-time"}).text
    reading_time_int = int(re.search(r"\d+", reading_time_str).group())
    summary = soup.find("div", {"class": "entry-content"}).p.text.strip()
    category = soup.find("span", {"class": "label"}).text.strip()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time_int,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    all_news = []

    while len(all_news) < amount:
        response = fetch(url)
        news_links = scrape_updates(response)

        for link in news_links:
            news_content = fetch(link)
            news_data = scrape_news(news_content)
            all_news.append(news_data)

            if len(all_news) == amount:
                break

        if len(all_news) < amount:
            url = scrape_next_page_link(response)

    create_news(all_news)
    return all_news
