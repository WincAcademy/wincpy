import models
import os

"""
Use this file to create/delete a database for testing your functions in main.py.
Be sure to delete the database before running wincpy check.
Alternatively you can use :memory: in models.py to prevent wincpy from using your database.
"""


def main():
    """
    Comment out the fuction you are not using and run the file.
    """
    setup_data()
    # delete_database()


def setup_data():
    """
    Creates the database and fills it with data.
    """
    models.db.connect()
    models.db.create_tables(
        [
            models.Ingredient,
            models.Restaurant,
            models.Dish,
            models.Rating,
            models.DishIngredient,
        ]
    )

    ingredient_data = [
        ("milk", True, False, True),
        ("flour", True, True, False),
        ("eggs", True, False, True),
        ("bread", True, True, False),
        ("beef", False, False, True),
        ("tomato", True, True, True),
        ("cheese", True, False, True),
        ("jellybeans", True, False, True),
        ("cod", True, False, True),
        ("potato", True, True, True),
        ("banana", True, True, True),
        ("peanutbutter", True, True, True),
        ("aquafaba", True, True, True),
        ("eggplant", True, True, True),
        ("zuchinni", True, True, True),
        ("mushrooms", True, True, True),
    ]

    restaurant_data = [
        (
            ("Flavortown", "2012-01-01", "15:00", "23:30"),
            [
                ("Pancakes a la mode", 700, ("milk", "flour", "eggs")),
                ("Bacon burger", 1200, ("bread", "beef", "tomato", "cheese")),
                ("Omelette du Fromage", 800, ("eggs", "cheese")),
                ("Milk steak", 1000, ("beef", "milk", "jellybeans")),
            ],
            [
                (5, None),
                (3, "weird menu"),
                (2, "my milk steak was not boiled over hard"),
                (4, None),
                (5, None),
            ],
        ),
        (
            ("Freddies Fish", "2016-03-01", "11:00", "18:30"),
            [
                ("Fish n Chips", 900, ("cod", "flour", "eggs", "potato")),
                ("Ketchup-filled fries", 300, ("potato", "tomato")),
                ("Fish Fries", 800, ("potato", "cod")),
            ],
            [
                (4, None),
                (3, None),
                (3, None),
                (3, None),
                (1, None),
                (1, None),
                (2, None),
                (1, None),
            ],
        ),
        (
            ("Petes Peanutbutter Palace", "2019-08-02", "10:00", "17:30"),
            [
                ("Banana Pancakes", 700, ("milk", "flour", "eggs", "banana")),
                ("Elvis burger", 1200, ("bread", "beef", "banana", "peanutbutter")),
                ("Vegan Pancakes", 800, ("banana", "aquafaba", "peanutbutter")),
            ],
            [
                (5, None),
                (3, None),
                (5, "i love peanut butter"),
                (4, "not much choice"),
                (4, None),
            ],
        ),
        (
            ("Chique Food Boutique", "2020-01-01", "18:00", "23:30"),
            [
                ("Fancy Frittata", 1700, ("eggs", "flour", "cheese", "tomato")),
                ("Ratatouille", 3200, ("tomato", "zuchinni", "eggplant")),
                ("Boeuf Bourguignon", 3300, ("beef", "mushrooms", "potato")),
            ],
            [
                (5, None),
                (5, "expensive but real good"),
                (5, None),
                (5, None),
                (5, None),
                (5, None),
            ],
        ),
    ]

    ingredient_map = {
        n: models.Ingredient.create(
            name=n, is_vegetarian=is_v, is_vegan=is_vv, is_glutenfree=is_g
        )
        for n, is_v, is_vv, is_g in ingredient_data
    }

    for restaurant, dishes, ratings in restaurant_data:
        restaurant = models.Restaurant.create(
            name=restaurant[0],
            open_since=restaurant[1],
            opening_time=restaurant[2],
            closing_time=restaurant[3],
        )
        for dish_data in dishes:
            dish = models.Dish.create(
                name=dish_data[0],
                served_at=restaurant,
                price_in_cents=dish_data[1],
            )
            dish_ingredients = [ingredient_map[x] for x in dish_data[2]]
            dish.ingredients.add(dish_ingredients)
        for rating in ratings:
            models.Rating.create(
                restaurant=restaurant, rating=rating[0], comment=rating[1]
            )


def delete_database():
    """
    Delete the database.
    """
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "database.db")
    if os.path.exists(database_path):
        os.remove(database_path)


if __name__ == "__main__":
    main()
