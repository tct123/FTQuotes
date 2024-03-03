import flet as ft
import os
import dotenv as dv
import quotesgeneratorapi_wrapper as quote
from mylist import mylist


dv.load_dotenv()
API_KEY = os.getenv("API_NINJAS_KEY")


def rand_quote(page: ft.page):
    dd = ft.Dropdown(
        value="age",
        width=200,
        options=[ft.dropdown.Option(i) for i in mylist],
    )

    page.update()
    q = quote.getQuotes(api_key=API_KEY, category="age")
    quote_content = ft.Text(q)
    author = ft.Text()

    def newquotes(e):
        qnew = quote.getQuotes(api_key=API_KEY, category=dd.value)
        quote_content.clean()
        quote_content.update()
        quote_content.value = qnew
        quote_content.update()
        body.update()
        page.update()
        # print("Funktioniert")

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.UPDATE, on_click=newquotes
    )
    body = ft.Column(
        controls=[
            quote_content,
            ft.Row(controls=[dd, ft.IconButton(icon=ft.icons.FAVORITE)]),
        ]
    )  # author
    return body


def quote_tab(page: ft.Page):
    dd = ft.Dropdown(
        value="age",
        width=200,
        options=[ft.dropdown.Option(i) for i in mylist],
    )

    page.update()
    q = quote.getQuotes(api_key=API_KEY, category="age")
    quote_content = ft.Text(q)
    author = ft.Text()

    def newquotes(e):
        qnew = quote.getQuotes(api_key=API_KEY, category=dd.value)
        quote_content.clean()
        quote_content.update()
        quote_content.value = qnew
        quote_content.update()
        body.update()
        page.update()
        # print("Funktioniert")

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.UPDATE, on_click=newquotes
    )
    body = ft.Column(
        controls=[
            quote_content,
            ft.Row(controls=[dd, ft.IconButton(icon=ft.icons.FAVORITE)]),
        ]
    )  # author
    return body


def main(page: ft.Page):
    page.appbar = ft.AppBar(title=ft.Text("FTQuotes"))
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Quotes"),
            ft.NavigationDestination(
                icon=ft.icons.EMOJI_EMOTIONS, label="Random Quotes"
            ),
            ft.NavigationDestination(icon=ft.icons.FAVORITE, label="Favorite"),
        ],
        adaptive=True,
    )

    tabquotes = quote_tab(page=page)
    page.add(ft.SafeArea(tabquotes))


ft.app(main)
