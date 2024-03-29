"""Classes for melon orders."""
import random


class AbstractMelonOrder():

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):

        return random.randint(5, 9)

    def get_total(self):

        base_price = self.get_base_price()

        if self.species == "Christmas melons":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.country_code = country_code
        super().__init__(species, qty, "international", 0.17)
   
    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder (AbstractMelonOrder):

    passed_inspection = False

    def __init__(self, species, qty):
        super().__init__(species, qty, "government", 0)

    def mark_inspection(self, passed):
        self.passed_inspection = passed
        print(self.passed_inspection)
