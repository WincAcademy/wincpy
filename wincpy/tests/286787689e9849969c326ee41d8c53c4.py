import peewee
from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = "286787689e9849969c326ee41d8c53c4"


def run(student_module):
    try:
        setup_data(student_module.models)
    except peewee.ImproperlyConfigured:
        return [("Database can be initialized", False)]
    cheapest_dish = student_module.queries.cheapest_dish()
    vegetarian_dishes = student_module.queries.vegetarian_dishes()
    best_restaurant = student_module.queries.best_average_rating()
    current_rating_count = student_module.models.Rating.select().count()
    student_module.queries.add_rating_to_restaurant()
    new_rating_count = student_module.models.Rating.select().count()
    date_restaurants = student_module.queries.dinner_date_possible()
    new_dish = student_module.queries.add_dish_to_menu()

    result = [
        ("Models have correct mappings", True),
        (
            "Cheapest dish found",
            cheapest_dish
            == student_module.models.Dish.select()
            .order_by(student_module.models.Dish.price_in_cents)
            .first()
            if cheapest_dish
            else False,
        ),
        (
            "Vegetarian dishes found",
            set(vegetarian_dishes)
            == set(
                [
                    dish
                    for dish in student_module.models.Dish.select()
                    if all([i.is_vegetarian for i in dish.ingredients])
                ]
            )
            if vegetarian_dishes
            else False,
        ),
        (
            "Best average rating found",
            best_restaurant
            == (
                student_module.models.Restaurant.select(
                    student_module.models.Restaurant,
                    peewee.fn.AVG(student_module.models.Rating.rating).alias("average"),
                )
                .join(student_module.models.Rating)
                .group_by(student_module.models.Restaurant)
                .order_by(peewee.fn.AVG(student_module.models.Rating.rating).desc())
                .first()
            )
            if best_restaurant
            else False,
        ),
        ("A rating has been added", current_rating_count < new_rating_count),
        (
            "Date restaurants have been identified",
            set(date_restaurants)
            == set(
                [
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
            )
            if date_restaurants
            else False,
        ),
        ("New dish created", new_dish),
        (
            "New dish contains cheese",
            "cheese" in [x.name for x in new_dish.ingredients],
        ),
        (
            "Cheese not created twice",
            student_module.models.Ingredient.select()
            .where(student_module.models.Ingredient.name == "cheese")
            .count()
            == 1,
        ),
    ]
    return result


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
