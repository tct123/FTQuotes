import flet as ft
import os
import dotenv as dv
import quotesgeneratorapi_wrapper.quotesgenerator as quote
from mylist import mylist
from mylocale import TR
from pathlib import Path
from flet_localisation import locale
from localisations import *


def quote_tab(page: ft.Page, api_key):
    # dd = ft.Dropdown(
    #    value="age",
    #    # width=200,
    #    options=[ft.dropdown.Option(i) for i in mylist],
    # )

    page.update()
    q, a = str(
        quote.getQuotes(
            api_key=api_key,
        )
    ).split(
        "\n\n"
    )  # category="age"
    quote_content = ft.Text(q)
    author = ft.Text(a)

    def newquotes(e, api_key):
        qnew, anew = str(
            quote.getQuotes(
                api_key=api_key,
            )
        ).split(
            "\n\n"
        )  # category=dd.value
        quote_content.value = qnew
        quote_content.update()
        author.value = anew
        author.update()
        body.update()
        page.update()
        # print("Funktioniert")

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.UPDATE, on_click=lambda e: newquotes(e=e, api_key=api_key)
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
        page.show_dialog(aboutdialog)
        page.update()

    path = Path(__file__).resolve().parent
    dotenv_path = os.path.join(path, ".env")
    dv.load_dotenv(dotenv_path=dotenv_path)
    API_KEY = os.getenv("API_NINJAS_KEY")
    lf = os.path.join(path, "localisations/localisation.csv")  # localisationfile
    lang = locale(platform=str(page.platform))
    tr = TR(langcode="en", csv_file=lf)
    page.title = "FTQuotes"
    page.appbar = ft.AppBar(
        title=ft.Text(page.title),
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        tooltip=ABOUTHEADER(page=page),
                        on_click=open_aboutdialog,
                    )
                ]
            ),
        ],
    )
    # page.media = ft.PageMediaData()
    page.adaptive = True
    page.scroll = ft.ScrollMode.ALWAYS
    version = ""
    aboutdialog = ft.AlertDialog(
        title=ft.Text(ABOUTHEADER(page=page)),
        content=ft.Text(f"{ABOUT(page=page)} + {version}"),
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

    tabquotes = quote_tab(page=page, api_key=API_KEY)
    page.add(ft.SafeArea(tabquotes))


ft.run(main)
