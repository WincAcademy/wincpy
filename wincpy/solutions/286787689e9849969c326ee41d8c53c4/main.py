import models
import peewee
from typing import List


def cheapest_dish() -> models.Dish:
    """You want ot get food on a budget

    Query the database to retrieve the cheapest dish available
    """
    return models.Dish.select().order_by(models.Dish.price_in_cents).first()


def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    return [
        dish
        for dish in models.Dish.select()
        if all([i.is_vegetarian for i in dish.ingredients])
    ]


def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    return (
        models.Restaurant.select(
            models.Restaurant, peewee.fn.AVG(models.Rating.rating).alias("average")
        )
        .join(models.Rating)
        .group_by(models.Restaurant)
        .order_by(peewee.fn.AVG(models.Rating.rating).desc())
        .first()
    )


def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    restaurant = models.Restaurant.get_by_id(1)
    models.Rating.create(restaurant=restaurant, rating=5, comments=None)
    ...


def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    restaurants = (
        models.Restaurant.select()
        .where(models.Restaurant.opening_time <= "19:00")
        .where(models.Restaurant.closing_time >= "19:00")
    )
    return [
        restaurant
        for restaurant in restaurants
        if any(
            [
                all([i.is_vegan for i in dish.ingredients])
                for dish in restaurant.dish_set.select()
            ]
        )
    ]


def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    restaurant = models.Restaurant.get_by_id(1)
    cheese, _ = models.Ingredient.get_or_create(
        name="cheese",
        defaults={
            "is_vegetarian": True,
            "is_vegan": False,
            "is_glutenfree": True,
        },
    )
    tomato, _ = models.Ingredient.get_or_create(
        name="tomato",
        defaults={"is_vegetarian": True, "is_vegan": True, "is_glutenfree": True},
    )
    bacon, _ = models.Ingredient.get_or_create(
        name="bacon",
        defaults={
            "is_vegetarian": False,
            "is_vegan": False,
            "is_glutenfree": True,
        },
    )
    bread, _ = models.Ingredient.get_or_create(
        name="bread",
        defaults={
            "is_vegetarian": True,
            "is_vegan": True,
            "is_glutenfree": False,
        },
    )
    blt = models.Dish.create(served_at=restaurant, price_in_cents=1000, name="BLT")
    blt.ingredients.add([cheese, bacon, tomato, bread])
    return blt