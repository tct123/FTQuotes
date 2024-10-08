import flet as ft
import os
import dotenv as dv
import quotesgeneratorapi_wrapper.quotesgenerator as quote
from mylist import mylist
from mylocale.TR import tr
import locale

dv.load_dotenv()
API_KEY = os.getenv("API_NINJAS_KEY")
version = "2024.06.03"  # YYYY.MM.DD
lf = "assets/localisation.csv"  # localisationfile
lang = locale.getlocale()[0].split("_")[0]
print(lang)


def rand_quote(page: ft.Page):
    dd = ft.Dropdown(
        value="age",
        # width=200,
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
        # width=200,
        options=[ft.dropdown.Option(i) for i in mylist],
    )

    page.update()
    q, a = quote.getQuotes(api_key=API_KEY, category="age").split("\n\n")
    quote_content = ft.Text(q)
    author = ft.Text(a)

    def newquotes(e):
        qnew, anew = quote.getQuotes(api_key=API_KEY, category=dd.value).split("\n\n")
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
        icon=ft.icons.UPDATE, on_click=newquotes
    )

    def add_remove_favourite(e):
        if likebutton.icon == ft.icons.FAVORITE_OUTLINE:
            likebutton.icon = ft.icons.FAVORITE
            page.client_storage.set("QUOTE", quote_content.value)
            page.client_storage.set("AUTHOR", author.value)
            likebutton.update()
            body.update()
            page.update()
        else:
            likebutton.icon = ft.icons.FAVORITE_OUTLINE
            likebutton.update()
            page.client_storage.remove(quote_content.value)
            page.client_storage.remove(author.value)
            body.update()
            page.update()

    likebutton = ft.IconButton(
        icon=ft.icons.FAVORITE_OUTLINE, on_click=lambda e: add_remove_favourite(e=e)
    )
    body = ft.Column(
        controls=[
            quote_content,
            author,
            dd,
            likebutton,
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
    #        ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Quotes"),
    #        ft.NavigationBarDestination(
    #            icon=ft.icons.EMOJI_EMOTIONS, label="Random Quotes"
    #        ),
    #        ft.NavigationBarDestination(icon=ft.icons.FAVORITE, label="Favorite"),
    #    ],
    #    adaptive=True,
    # )

    tabquotes = quote_tab(page=page)
    page.add(ft.SafeArea(tabquotes))


ft.app(main)
