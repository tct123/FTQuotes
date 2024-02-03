import flet as ft
import os
import dotenv as dv
import quotesgeneratorapi_wrapper as quote


dv.load_dotenv()


def main(page: ft.Page):
    API_KEY = os.getenv("API_NINJAS_KEY")
    page.appbar = ft.AppBar(
        title=ft.Text("FTQuotes"),
    )
    page.navigation_bar = ft.NavigationBar(
       destinations=[
           ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Quotes"),
           ft.NavigationDestination(icon=ft.icons.EMOJI_EMOTIONS, label="Random Quotes"),
           ft.NavigationDestination(icon=ft.icons.FAVORITE, label="Favorite"),
       ],
       # bgcolor=ft.colors.RED,
    )
    dd = ft.Dropdown(
        value="age",
        width=200,
        options=[
            ft.dropdown.Option("age"),
            ft.dropdown.Option("alone"),
            ft.dropdown.Option("amazing"),
            ft.dropdown.Option("anger"),
            ft.dropdown.Option("architecture"),
            ft.dropdown.Option("art"),
            ft.dropdown.Option("attitude"),
            ft.dropdown.Option("beauty"),
            ft.dropdown.Option("best"),
            ft.dropdown.Option("birthday"),
            ft.dropdown.Option("business"),
            ft.dropdown.Option("car"),
            ft.dropdown.Option("change"),
            ft.dropdown.Option("communication"),
            ft.dropdown.Option("computers"),
            ft.dropdown.Option("cool"),
            ft.dropdown.Option("courage"),
            ft.dropdown.Option("dad"),
            ft.dropdown.Option("dating"),
            ft.dropdown.Option("death"),
            ft.dropdown.Option("design"),
            ft.dropdown.Option("dreams"),
            ft.dropdown.Option("education"),
            ft.dropdown.Option("environmental"),
            ft.dropdown.Option("equality"),
            ft.dropdown.Option("experience"),
            ft.dropdown.Option("failure"),
            ft.dropdown.Option("faith"),
            ft.dropdown.Option("family"),
            ft.dropdown.Option("famous"),
            ft.dropdown.Option("fear"),
            ft.dropdown.Option("fitness"),
            ft.dropdown.Option("food"),
            ft.dropdown.Option("forgiveness"),
            ft.dropdown.Option("freedom"),
            ft.dropdown.Option("friendship"),
            ft.dropdown.Option("funny"),
            ft.dropdown.Option("future"),
            ft.dropdown.Option("god"),
            ft.dropdown.Option("good"),
            ft.dropdown.Option("government"),
            ft.dropdown.Option("graduation"),
            ft.dropdown.Option("great"),
            ft.dropdown.Option("happiness"),
            ft.dropdown.Option("health"),
            ft.dropdown.Option("history"),
            ft.dropdown.Option("home"),
            ft.dropdown.Option("hope"),
            ft.dropdown.Option("humor"),
            ft.dropdown.Option("imagination"),
            ft.dropdown.Option("inspirational"),
            ft.dropdown.Option("intelligence"),
            ft.dropdown.Option("jealousy"),
            ft.dropdown.Option("knowledge"),
            ft.dropdown.Option("leadership"),
            ft.dropdown.Option("learning"),
            ft.dropdown.Option("legal"),
            ft.dropdown.Option("life"),
            ft.dropdown.Option("love"),
            ft.dropdown.Option("marriage"),
            ft.dropdown.Option("medical"),
            ft.dropdown.Option("men"),
            ft.dropdown.Option("mom"),
            ft.dropdown.Option("money"),
            ft.dropdown.Option("morning"),
            ft.dropdown.Option("movies"),
            ft.dropdown.Option("success"),
        ],
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
    body = ft.Column(controls=[quote_content, ft.Row(controls=[dd,ft.IconButton(icon=ft.icons.FAVORITE)])]) # author
    page.add(ft.SafeArea(body))


ft.app(main)
