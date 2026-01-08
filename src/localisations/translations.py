import os
from mylocale import TR
from flet_localisation import locale
import flet as ft


def ABOUTHEADER(page):
    trfile = f"{os.path.dirname(__file__)}/localisation.csv"
    myplatfom = str(page.platform)
    mylocale = str(locale(platform=myplatfom)).split("_")
    langcode = mylocale[0]
    region = mylocale[1]
    tr = TR(csv_file=trfile, langcode=langcode)
    return tr.tr(
        target_key="ABOUTHEADER",
        langcode=langcode,
    )


def ABOUT(page):
    trfile = f"{os.path.dirname(__file__)}/localisation.csv"
    myplatfom = str(page.platform)
    mylocale = str(locale(platform=myplatfom)).split("_")
    langcode = mylocale[0]
    region = mylocale[1]
    tr = TR(csv_file=trfile, langcode=langcode)
    return tr.tr(
        target_key="ABOUT",
        langcode=langcode,
    )
