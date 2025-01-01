import flet as ft
import os
import dotenv as dv
import quotesgeneratorapi_wrapper.quotesgenerator as quote
from mylist import mylist
from mylocale import tr
import locale

dv.load_dotenv()
API_KEY = os.getenv("API_NINJAS_KEY")
version = "2024.06.03"  # YYYY.MM.DD
lf = "assets/localisation.csv"  # localisationfile
lang = locale.getlocale()[0].split("_")[0]


def quote_tab(page: ft.Page):
    # dd = ft.Dropdown(
    #    value="age",
    #    # width=200,
    #    options=[ft.dropdown.Option(i) for i in mylist],
    # )

    page.update()
    q, a = quote.getQuotes(
        api_key=API_KEY,
    ).split(
        "\n\n"
    )  # category="age"
    quote_content = ft.Text(q)
    author = ft.Text(a)

    def newquotes(e):
        qnew, anew = quote.getQuotes(
            api_key=API_KEY,
        ).split(
            "\n\n"
        )  # category=dd.value
        quote_content.clean()
        quote_content.value = qnew
        quote_content.update()
        author.clean()
        author.value = anew
        author.update()
        body.update()
        page.update()
        # print("Funktioniert")

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.UPDATE, on_click=newquotes
    )

    body = ft.Column(
        controls=[
            quote_content,
            author,  # dd
            # ft.Row(
            #    controls=[
            #        dd,
            #        likebutton,
            #    ]
            # ),
        ]
    )  # author
    return body


def main(page: ft.Page):
    def open_aboutdialog(e):
        page.open(aboutdialog)
        page.update()

    page.title = "FTQuotes"
    page.appbar = ft.AppBar(
        title=ft.Text(page.title),
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        text=tr(csv_file=lf, target_key="ABOUTHEADER", langcode=lang),
                        on_click=open_aboutdialog,
                    )
                ]
            ),
        ],
    )
    # page.media = ft.PageMediaData()
    page.adaptive = True
    page.scroll = True
    aboutdialog = ft.AlertDialog(
        title=ft.Text(tr(csv_file=lf, target_key="ABOUTHEADER", langcode=lang)),
        content=ft.Text(
            f"{tr(csv_file=lf, target_key='ABOUT', langcode=lang)} + {version}"
        ),
        scrollable=True,
    )
    # page.navigation_bar = ft.NavigationBar(
    #    destinations=[
    #        ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Quotes"),
    #        ft.NavigationBarDestination(
    #            icon=ft.Icons.EMOJI_EMOTIONS, label="Random Quotes"
    #        ),
    #        ft.NavigationBarDestination(icon=ft.Icons.FAVORITE, label="Favorite"),
    #    ],
    #    adaptive=True,
    # )

    tabquotes = quote_tab(page=page)
    page.add(ft.SafeArea(tabquotes))


ft.app(main)
