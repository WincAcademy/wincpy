import peewee

db = peewee.SqliteDatabase(":memory:")


class Ingredient(peewee.Model):
    name = ...
    is_vegetarian = ...
    is_vegan = ...
    is_glutenfree = ...

    class Meta:
        database = db


class Restaurant(peewee.Model):
    name = ...
    open_since = ...
    opening_time = ...
    closing_time = peewee.TimeField()

    class Meta:
        database = db


class Dish(peewee.Model):
    name = ...
    served_at = ...
    price_in_cents = ...
    ingredients = ...

    class Meta:
        database = db


class Rating(peewee.Model):
    restaurant = ...
    rating = ...
    comment = peewee.CharField(null=True)

    class Meta:
        database = db


DishIngredient = Dish.ingredients.get_through_model()