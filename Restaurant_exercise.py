from bs4 import BeautifulSoup
import pandas as pd

with open("thewolfhound.html") as f:
    page = BeautifulSoup(f, "lxml")

#The URL used was https://www.thewolfhound.nl/

page.select("title")[0].get_text()
title = page.select("title")[0].get_text()
print(title)

page.select(".widget-text")[0].get_text()
description = page.select(".widget-text")[0].get_text()
print(description)

page.select(".footer_adres")[0].get_text()
contact = page.select(".footer_adres")[0].get_text()
print(contact)

page.select(".navigation_main__list")[0].get_text()
navigation = page.select(".navigation_main__list")[0].get_text()
print(navigation)

#The menu was a picture/pdf file and I was therefore unable to scrape it.
