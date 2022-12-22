"""Classes for melon orders."""
import math 

#create a super class for domestic and international melon orders
class AbstractMelonOrder:
    #create a function with a dunder init --> self, species, qty (maybe additional attributes?)
    def __init__(self, species, qty):
        # print("Calling parent init")
        self.species = species
        self.qty = qty


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        # if statement needed for xmas melon(species) will cost 1.5times of base
        if self.species == "christmas melon":
            base_price = base_price * 1.5
    
        total = (1 + self.tax) * self.qty * base_price

        return (f'{total: .2f}')

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        """Initialize melon order attributes."""
        # print("Setting internation attributes")
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        
    # if statement needed for international orders with qty <10 will +$3 to total
        if self.qty < 10: 
            total = total + 3
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    
    order_type = "government"
    tax = 0.0
    
    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        self.passed_inspection = passed
            
        