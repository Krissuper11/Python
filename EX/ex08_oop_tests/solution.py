"""Ex08 (3)."""


class Factory:
    """Factory."""

    def __init__(self):
        """init."""
        self.large_cakes = self
        self.medium_cakes = self
        self.small_cake = self
        self.number_of_cakes = self
        self.cake_list = self
        self.number_of_cakes_total = 0

    def bake_cake(self, toppings: int, base: int) -> int:
        """Bake cake."""
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
            self.number_of_cakes_total += number_of_cakes
        return number_of_cakes

    def get_last_cakes(self, n: int) -> list:
        """Get list with last cakes."""
        last_cakes_list = []
        get_cake_list = []
        get_cake_list += Factory.get_cakes_baked(self)
        counter = 0 - n
        for i in range(n):
            try:
                last_cakes_list.append(get_cake_list[counter])
            except IndexError:
                pass
            counter += 1
        return last_cakes_list

    def get_cakes_baked(self) -> list:
        """Get list with baked cakes."""
        self.cake_list = []
        for i in range(self.large_cakes):
            new_cake = Cake(5, 5)
            self.cake_list.append(new_cake)
        for i in range(self.medium_cakes):
            new_cake = Cake(2, 2)
            self.cake_list.append(new_cake)
        for i in range(self.small_cake):
            new_cake = Cake(1, 1)
            self.cake_list.append(new_cake)
        return self.cake_list

    def __str__(self):
        """Describe."""
        if self.number_of_cakes_total == 1:
            return f"Factory with {self.number_of_cakes} cake."
        else:
            return f"Factory with {self.number_of_cakes_total} cakes."


class Cake:
    """Cake."""

    def __init__(self, base_amount, toppings_amount):
        """init, check for error."""
        self.base_amount = base_amount
        self.toppings_amount = toppings_amount
        if self.toppings_amount != self.base_amount or\
                self.toppings_amount not in (1, 2, 5) or self.base_amount not in (1, 2, 5):
            raise WrongIngredientsAmountException

    @property
    def type(self):
        """Give type."""
        if self.toppings_amount == 1 and self.base_amount == 1:
            return "basic"
        elif self.base_amount == 2 and self.toppings_amount == 2:
            return "medium"
        elif self.toppings_amount == 5 and self.base_amount == 5:
            return "large"

    def __repr__(self):
        """Give type."""
        if self.toppings_amount == 1 and self.base_amount == 1:
            return "Cake(basic)"
        elif self.base_amount == 2 and self.toppings_amount == 2:
            return "Cake(medium)"
        elif self.toppings_amount == 5 and self.base_amount == 5:
            return "Cake(large)"

    def __eq__(self, other):
        """Check if equal."""
        return self.base_amount == other.base_amount


class WrongIngredientsAmountException(Exception):
    """Exception."""

    pass
