import requests
import csv
import os
from bs4 import BeautifulSoup

url = "https://hashtagbasketball.com/fantasy-basketball-projections"
players = []


def print_csv(player):
    fieldnames = [
        "RANK",
        "ADP",
        "NAME",
        "POSITION",
        "TEAM",
        "GP",
        "MPG",
        "FG",
        "FT",
        "3PT",
        "PTS",
        "REB",
        "AST",
        "ST",
        "BLK",
        "TO",
        "TOTAL",
    ]
    rows = []
    rows.append(player)
    with open('fantasy.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(rows)



def scrap_fantasy(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    page = soup.find("table", {"id": "ContentPlaceHolder1_GridView1"})

    rows = page.find_all("tr")

    for row in rows:
        bodies = row.find_all("td")
        if not bodies:
            continue
        
        if bodies[0].text.strip() == "R#":
            continue
        
        player = {
            "RANK": bodies[0].text.strip(),
            "ADP": bodies[1].text.strip(),
            "NAME": bodies[2].text.strip(),
            "POSITION": bodies[3].text.strip(),
            "TEAM": bodies[4].text.strip(),
            "GP": bodies[5].text.strip(),
            "MPG": bodies[6].text.strip(),
            "FG": bodies[7].text.strip(),
            "FT": bodies[8].text.strip(),
            "3PT": bodies[9].text.strip(),
            "PTS": bodies[10].find('span').text.strip(),
            "REB": bodies[11].find('span').text.strip(),
            "AST": bodies[12].find('span').text.strip(),
            "ST": bodies[13].find('span').text.strip(),
            "BLK": bodies[14].find('span').text.strip(),
            "TO": bodies[15].find('span').text.strip(),
            "TOTAL": bodies[16].find('span').text.strip(),
        }
        print_csv(player)


scrap_fantasy(url=url)
