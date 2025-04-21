import os
from dotenv import load_dotenv
import requests
import json

load_dotenv('config.env')
KEY = os.getenv('API_KEY')
ENDPOINT = 'https://api.spoonacular.com/recipes/findByIngredients'

api_header = {
    "x-api-key": KEY,
    "Content-type": "application/json",
}


def get_recipe_ingredients(*ingredients, **optional_params):
    """
    Fetches recipes based on ingredients provided by the user.


    ingredients: a tuple where a user can specify an unlimited amount of ingredients \n
    optional_params: list of optional things to query for:
        number: max amount of recipes returned
        ranking: whether to maximize used ingredients (1) or minimize missing ingredients (2) first
        ignorePantry: whether to ignore common pantry items, such as water, salt, oil etc
    """

    query_string = f'{ENDPOINT}?ingredients={',+'.join(ingredients)}'

    for param, value in zip(optional_params.keys(), optional_params.values()):
        if value != 0 or None or False:
            query_string += f'&{param}={value}'

    res = requests.get(query_string, headers=api_header)

    with open('return.json', 'w') as json_file:
        json.dump(res.json(), json_file)


if __name__ == '__main__':
    get_recipe_ingredients('minced beef', 'onions', 'tomato puree', number=1)
