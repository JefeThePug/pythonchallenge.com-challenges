# Challenge 15

import datetime
import requests
from bs4 import BeautifulSoup


def is_leap_year(year):
    try:
        datetime.date(year, 2, 29)
        return datetime.date(year, 1, 1).weekday() == 3
    except ValueError:
        return False


year = [year for year in range(1006, 2000, 10) if is_leap_year(year)][-2]
print(f"January 27, {year}")

url = "https://www.born-today.com/Today/01-27.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
people = soup.find_all("div", class_="person-info")

for person in people:
    if f"Born: {year}" in person.text:
        birthday = person.find("img").get("alt").split()[-1]

print(birthday)

####################
# OUTPUT:          #
#                  #
# January 27, 1756 #
# Mozart           #
####################
