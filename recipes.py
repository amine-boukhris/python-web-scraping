from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import csv

def getAllRecipesLinks():
    allrecipes_url="https://www.allrecipes.com/recipes/79/desserts/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0"}

    html_text = requests.get(allrecipes_url, headers=headers).text
    soup = BeautifulSoup(html_text, "lxml")

    recipes_grids_grid = soup.find("div", class_="comp mntl-taxonomysc-article-list-group mntl-block")
    recipes_grids = recipes_grids_grid.find_all("div", class_="comp tax-sc__recirc-list card-list mntl-document-card-list mntl-card-list mntl-block")

    links_list = []
    for recipes_grid in recipes_grids:
        recipes = recipes_grid.find_all("a", class_="comp mntl-card-list-items mntl-document-card mntl-card card card--no-image")
        for recipe in recipes:
            links_list.append(recipe['href'])
    
    return links_list

links = getAllRecipesLinks()
link = links[0]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0"}
html_text = requests.get(link, headers=headers).text
soup = BeautifulSoup(html_text, "lxml")

recipe_title = soup.find("h1", class_="comp type--lion article-heading mntl-text-block")
recipe_desc = soup.find("p", class_="comp type--dog article-subheading")
recipe_prep_details = soup.find_all("div", class_="mntl-recipe-details__value")

recipe_prep_details = {
    "prep time": recipe_prep_details[0].text,
    "cook time": recipe_prep_details[1].text,
    "cool time": recipe_prep_details[2].text,
    "total time": recipe_prep_details[3].text,
    "servings": recipe_prep_details[4].text
}
# turn dict into List[Tuple]
data = [(key, value) for key, value in recipe_prep_details.items()]
print(tabulate(data, headers=["key", "value"], tablefmt="grid"))

# for key, value in recipe_prep_details.items():
#     print(f"{key}: {value}")
