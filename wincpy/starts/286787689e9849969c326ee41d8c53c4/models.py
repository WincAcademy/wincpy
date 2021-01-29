import peewee

db = peewee.SqliteDatabase(":memory:")


class Ingredient(peewee.Model):
    name = peewee.CharField()
    is_vegetarian = peewee.BooleanField()
    is_vegan = ...
    is_glutenfree = peewee.BooleanField()

    class Meta:
        database = db


class Restaurant(peewee.Model):
    name = peewee.CharField()
    open_since = ...
    opening_time = ...
    closing_time = peewee.TimeField()

    class Meta:
        database = db


class Dish(peewee.Model):
    name = ...
    served_at = peewee.ForeignKeyField(Restaurant)
    price_in_cents = ...
    ingredients = peewee.ManyToManyField(Ingredient)

    class Meta:
        database = db


class Rating(peewee.Model):
    restaurant = peewee.ForeignKeyField(Restaurant)
    rating = ...
    comment = peewee.CharField(null=True)

    class Meta:
        database = db


DishIngredient = Dish.ingredients.get_through_model()