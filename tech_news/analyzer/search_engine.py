from datetime import datetime
from tech_news.database import db


# Requisito 7
def search_by_title(title):
    try:
        result = db.news.find(
            {"title": {"$regex": title, "$options": "i"}},
            {"title": 1, "url": 1}
        )

        news_list = [(el["title"], el["url"]) for el in result]
        return news_list
    except Exception as error:
        raise error


# Requisito 8
def search_by_date(date):
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")  # NOQA
    except ValueError:
        raise ValueError("Data inválida")

    result = db.news.find(
        {"timestamp": formatted_date},
        {"title": 1, "url": 1}
    )

    news_list = [(news["title"], news["url"]) for news in result]

    return news_list


# Requisito 9
def search_by_category(category):
    try:
        result = db.news.find(
            {"category": {"$regex": category, "$options": "i"}},
            projection=["title", "url"]
        )

        news_list = [(el["title"], el["url"]) for el in result]
        return news_list

    except Exception as error:
        raise error
