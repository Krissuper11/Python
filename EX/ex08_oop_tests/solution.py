class Factory:
    def __init__(self):
        self.large_cakes = self
        self.medium_cakes = self
        self.small_cake = self
        self.number_of_cakes = self

    def bake_cake(self, toppings: int, base: int) -> int:
        number_of_cakes = 0
        if toppings == base:
            number = toppings
            number_of_cakes += number // 5
            self.large_cakes = number_of_cakes
            number -= number // 5 * 5
            number_of_cakes += number // 2
            self.medium_cakes = number_of_cakes - self.large_cakes
            number -= number // 2 * 2
            number_of_cakes += number
            self.small_cake = number
            self.number_of_cakes = number_of_cakes
        return number_of_cakes

    def get_last_cakes(self, n: int) -> list:
        pass

    def get_cakes_baked(self) -> list:
        pass

    def __str__(self):
        if self.number_of_cakes == 1:
            return f"Factory with {self.number_of_cakes} cake."
        else:
            return f"Factory with {self.number_of_cakes} cakes."


class Cake:

    def __init__(self, base_amount, toppings_amount):
        pass

    @property
    def type(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass


class WrongIngredientsAmountException(Exception):
    pass
