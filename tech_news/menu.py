import sys


from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)


from tech_news.scraper import get_tech_news


def handle_action_0():
    quantity = int(input("Digite quantas notícias serão buscadas:"))

    return get_tech_news(quantity)


def handle_action_1():
    title = input("Digite o título:")

    return search_by_title(title)


def handle_action_2():
    date = input("Digite a data no formato aaaa-mm-dd:")

    return search_by_date(date)


def handle_action_3():
    category = input("Digite a categoria:")

    return search_by_category(category)


def handle_action_4():
    return top_5_categories()


def handle_action_5():
    return print("Encerrando script\n")


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair."
    )

    menu_actions = {
        "0": handle_action_0,
        "1": handle_action_1,
        "2": handle_action_2,
        "3": handle_action_3,
        "4": handle_action_4,
        "5": handle_action_5,
    }

    try:
        return menu_actions[option]()

    except Exception:
        return print("Opção inválida", file=sys.stderr)
