import models
import peewee


def cheapest_dish():
    """You want ot get food on a budget

    Query the database to retrieve the cheapest dish available.
    Return a single instance of models.Dish, it must be the instance
    with the lowest price
    """
    ...


def vegetarian_dishes():
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    Return a list of instances of models.Dish, all instance must contain
    vegetarian ingredients only.
    """
    ...


def best_average_rating():
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average.
    Return a single instance of models.Restaurant, the instance must have the
    best rating.
    """
    ...


def add_rating_to_restaurant():
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    You do not have to return anything
    """
    ...


def dinner_date_possible():
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    Return a list of instances of models.Restaurant
    """
    ...


def add_dish_to_menu():
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish - a single instance of models.Dish
    """
    ...