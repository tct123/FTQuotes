import flet as ft
import os
import dotenv as dv
import quotesgeneratorapi_wrapper.quotesgenerator as quote
from mylist import mylist
from mylocale import TR
import locale
from pathlib import Path


def quote_tab(page: ft.Page, api_key):
    # dd = ft.Dropdown(
    #    value="age",
    #    # width=200,
    #    options=[ft.dropdown.Option(i) for i in mylist],
    # )

    page.update()
    q, a = quote.getQuotes(
        api_key=api_key,
    ).split(
        "\n\n"
    )  # category="age"
    quote_content = ft.Text(q)
    author = ft.Text(a)

    def newquotes(e, api_key):
        qnew, anew = quote.getQuotes(
            api_key=api_key,
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
        page.open(aboutdialog)
        page.update()

    dv.load_dotenv()
    API_KEY = os.getenv("API_NINJAS_KEY")
    path = Path(__file__).resolve().parent
    lf = os.path.join(path, "assets/localisation.csv")  # localisationfile
    try:
        lang = locale.getlocale()[0].split("_")[0]
    except:
        lang = ""
    tr = TR(langcode="en", csv_file=lf)
    page.title = "FTQuotes"
    page.appbar = ft.AppBar(
        title=ft.Text(page.title),
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        tooltip=tr.tr(target_key="ABOUTHEADER", langcode=lang),
                        on_click=open_aboutdialog,
                    )
                ]
            ),
        ],
    )
    # page.media = ft.PageMediaData()
    page.adaptive = True
    page.scroll = True
    version = ""
    aboutdialog = ft.AlertDialog(
        title=ft.Text(tr.tr(target_key="ABOUTHEADER", langcode=lang)),
        content=ft.Text(f"{tr.tr( target_key='ABOUT', langcode=lang)} + {version}"),
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
