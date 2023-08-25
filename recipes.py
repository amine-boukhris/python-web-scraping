from bs4 import BeautifulSoup
import requests

def getAllRecipesLinks():
    allrecipes_url="https://www.allrecipes.com/recipes/79/desserts/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0"}

    html_text = requests.get(allrecipes_url, headers=headers).text
    soup = BeautifulSoup(html_text, "lxml")

    recipes_grids_grid = soup.find("div", class_="comp mntl-taxonomysc-article-list-group mntl-block")
    recipes_grids = recipes_grids_grid.find_all("div", class_="comp tax-sc__recirc-list card-list mntl-document-card-list mntl-card-list mntl-block")

    count = 0
    for recipes_grid in recipes_grids:
        recipes = recipes_grid.find_all("a", class_="comp mntl-card-list-items mntl-document-card mntl-card card card--no-image")
        for recipe in recipes:
            count+=1
            print(recipe['href'])
    print(count)

getAllRecipesLinks()