import peewee  # type: ignore
from wincpy.checks.utils import StandardChecks

__winc_id__ = "286787689e9849969c326ee41d8c53c4"


def check_db_init(student_module):
    """The database can be initialized properly"""
    setup_data(student_module.models)


def check_cheapest_dish(student_module):
    """`cheapest_dish` is implemented correctly"""
    StandardChecks.n_params(student_module.cheapest_dish, n_params=0)
    StandardChecks.n_params(student_module.models.Dish.select, n_params=1)

    dish = student_module.cheapest_dish()
    expected_dish = (
        student_module.models.Dish.select()
        .order_by(student_module.models.Dish.price_in_cents)
        .first()
    )
    assert dish == expected_dish, f"Expected the cheapest dish to be {expected_dish}."
    assert type(dish) == type(
        expected_dish
    ), f"Expected the cheapest dish to be {expected_dish}."


def check_vegetarian_dishes(student_module):
    """`vegetarian_dishes` is implemented correctly"""
    StandardChecks.n_params(student_module.vegetarian_dishes, n_params=0)
    StandardChecks.n_params(student_module.models.Dish.select, n_params=1)

    dishes = student_module.vegetarian_dishes()
    expected_dishes = set(
        [
            dish
            for dish in student_module.models.Dish.select()
            if all([i.is_vegetarian for i in dish.ingredients])
        ]
    )
    assert (
        set(dishes) == expected_dishes
    ), f"Expected vegetarian dishes to be {expected_dishes}"


def check_best_restaurant(student_module):
    """`best_average_rating` is implemented correctly"""
    StandardChecks.n_params(student_module.best_average_rating, n_params=0)

    restaurant = student_module.best_average_rating()
    expected_restaurant = (
        student_module.models.Restaurant.select(
            student_module.models.Restaurant,
            peewee.fn.AVG(student_module.models.Rating.rating).alias("average"),
        )
        .join(student_module.models.Rating)
        .group_by(student_module.models.Restaurant)
        .order_by(peewee.fn.AVG(student_module.models.Rating.rating).desc())
        .first()
    )
    assert (
        restaurant == expected_restaurant
    ), f"Expected the best restaurant to be {expected_restaurant}"
    assert type(restaurant) == type(
        expected_restaurant
    ), f"Expected the best restaurant to be {expected_restaurant}"


def check_add_rating(student_module):
    """`add_rating_to_restaurant` is implemented correctly"""
    StandardChecks.n_params(student_module.add_rating_to_restaurant, n_params=0)

    current_rating_count = student_module.models.Rating.select().count()
    student_module.add_rating_to_restaurant()
    new_rating_count = student_module.models.Rating.select().count()
    assert (
        current_rating_count < new_rating_count
    ), f"Expected number of ratings to go from {current_rating_count} to {current_rating_count + 1}"


def check_dinner_date_possible(student_module):
    """`dinner_date_possible` is implemented correctly"""
    StandardChecks.n_params(student_module.dinner_date_possible, n_params=0)

    date_restaurants = student_module.dinner_date_possible()
    expected_date_restaurants = [
        restaurant
        for restaurant in student_module.models.Restaurant.select()
        .where(student_module.models.Restaurant.opening_time <= "19:00")
        .where(student_module.models.Restaurant.closing_time >= "19:00")
        if any(
            [
                all([i.is_vegan for i in dish.ingredients])
                for dish in restaurant.dish_set.select()
            ]
        )
    ]
    assert set(date_restaurants) == set(
        expected_date_restaurants
    ), f"Expected dinner date restaurants to be {expected_date_restaurants}"


def check_add_dish_to_menu(student_module):
    """`add_dish_to_menu` is implemented correctly"""
    StandardChecks.n_params(student_module.add_dish_to_menu, n_params=0)

    new_dish = student_module.add_dish_to_menu()
    assert new_dish, "Expected the new dish to be returned"
    assert "cheese" in [
        x.name for x in new_dish.ingredients
    ], "Expected 'cheese' to be in the ingredients for the new dish"
    assert (
        student_module.models.Ingredient.select()
        .where(student_module.models.Ingredient.name == "cheese")
        .count()
        == 1
    ), "The ingredient 'cheese' was created twice"


def setup_data(models):
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
