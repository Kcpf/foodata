"""
Ifood-Scraping

This script aims to scrape IFood Website in order to get menu data from a restaurant.

Functionality:
    Install requirements.txt
    Run main.py
    Follow Steps in a CLI:
        Type Restaurant's Name
        Type a coordinate near the restaurant
        Select which resturant in the list given
        Select if you want to download images from Ifood
    
    Menu and images will be generated under assets folder
    End! 😀
    
Todo:
    * Complements section

@author: Fernando Franca
"""
import requests
import pandas as pd
from termcolor import colored
from pyfiglet import Figlet
import os

from Category import Category
from Product import Product
from Menu import Menu
from cli import *
from headers import *

# Logo Ifood Scraping

logo_render = Figlet(font='slant')
print(logo_render.renderText('Ifood Scraping'))

# Search Method

answers = prompt(questions_search, style=style)
if answers['searchSelector'] == "IFood Restaurant ID":
    answers = prompt(question_id, style=style)
    store_name = answers["restaurantName"]
    store_id = answers["restaurantId"]
else:
    # Prompting first questions
    answers = prompt(questions_initial, style=style)
    latitude_input = str(answers["latitude"])
    longitude_input = str(answers["longitude"])
    search_input = "+".join(answers["restaurantName"].split())

    # Searching for resturants with name near the coordinates

    url = f"https://marketplace.ifood.com.br/v2/search/merchants?latitude={latitude_input}&longitude={longitude_input}&channel=IFOOD&term={search_input}&size=100&page=0"

    response = requests.request("GET", url, headers=headers_first, data=payload).json()["merchants"]["data"]

    options = {merchant["name"]:merchant["id"] for merchant in response}

    for each in options:
        questions_restaurant[0]["choices"].append({
            'name':each
        })

    # Selecting restaurant

    answers = prompt(questions_restaurant, style=style)


    store_id = options[answers["restaurantSelector"]]
    store_name = answers["restaurantSelector"]

# Asking if user want to save images from menu

answer_image = prompt(questions_image, style=style)

os.mkdir(f"{os.getcwd()}/assets/{store_name}")

if answer_image["downloadImages"] == True:
    os.mkdir(f"{os.getcwd()}/assets/{store_name}/images")
    image_path = f"{os.getcwd()}/assets/{store_name}/images"

# Creating Menu

url = f"https://wsloja.ifood.com.br/ifood-ws-v3/restaurants/{store_id}/menu"

IMG_PRODUCT_BASE_URL = "https://static-images.ifood.com.br/image/upload/t_high/pratos/"
IMG_LOGO_BASE_URL = "https://static-images.ifood.com.br/image/upload/t_thumbnail/logosgde/"

# Products image base URL
# https://static-images.ifood.com.br/image/upload/t_low/pratos/
# https://static-images.ifood.com.br/image/upload/t_high/pratos/

response = requests.request("GET", url, headers=headers_second, data=payload)

data = response.json()["data"]

menu = data["menu"]

generated_menu = Menu()

# Creating Menu with class

for category in menu:
    cat = Category(category["name"])

    for product in category["itens"]:
        prod = Product(
            product["description"],
            product["details"],
            "",
            product["unitPrice"],
            cat
        )
        try:
            prod.setImage(IMG_PRODUCT_BASE_URL+product["logoUrl"])
        except Exception:
            print(colored(f"Product {product['description']} does not have image!", "yellow"))
        
        cat.addProduct(prod)
    
    generated_menu.addCategory(cat)

# For each product in class Menu get some information and save on Dataframe

dictionary = {}
for index, prod in enumerate(generated_menu.getAllProducts()):

    if answer_image['downloadImages'] == True and prod.getImage() != "":
        try:
            response = requests.get(prod.getImage())
            if response.status_code == 200:
                with open(f"{image_path}/{index}.jpg", 'wb') as f:
                    f.write(response.content)
        except Exception as e:
            print(colored(f"Could not save {prod.getName()} picture", "red"))
            print(e)
        finally:
            dictionary[index] = [
                prod.getCategory().name,
                prod.getName(),
                prod.getPrice(),
                f"{image_path}/{index}.jpg",
                prod.getDescription().strip()
            ]
    
    else:
        dictionary[index] = [
            prod.getCategory().name,
            prod.getName(),
            prod.getPrice(),
            prod.getImage(),
            prod.getDescription().strip()
        ]



df = pd.DataFrame.from_dict(dictionary, orient="index",
                            columns=["Category", "Name", "Price", "Image Path", "Description"])

restaurant_name = "_".join(store_name.split())

# Saving information from Dataframe on Excel

df.to_excel(f"{os.getcwd()}/assets/{store_name}/Menu_{restaurant_name}.xlsx")

print(colored(f"Generated Menu_{restaurant_name}.xlsx file", "green"))


