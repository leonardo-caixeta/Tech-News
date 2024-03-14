from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import patch


@patch("tech_news.database.find_news")
def test_reading_plan_group_news(mock_find_news):
    mock_find_news.return_value = [
        {"title": "Notícia 1", "reading_time": 4},
        {"title": "Notícia 2", "reading_time": 3},
        {"title": "Notícia 3", "reading_time": 10},
        {"title": "Notícia 4", "reading_time": 15},
        {"title": "Notícia 5", "reading_time": 12},
    ]

    expected_result = {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    ("Notícia 1", 4),
                    ("Notícia 2", 3),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    ("Notícia 3", 10),
                ],
            },
        ],
        "unreadable": [
            ("Notícia 4", 15),
            ("Notícia 5", 12),
        ],
    }

    service = ReadingPlanService()
    result = service.group_news_for_available_time(10)
    assert result == expected_result
