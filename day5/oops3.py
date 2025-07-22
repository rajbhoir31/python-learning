class Car:
    total_cars = 0  # Class attribute

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self._price = price  # Protected attribute
        Car.total_cars += 1

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - ₹{self._price}"

    @classmethod
    def show_total_cars(cls):
        return f"Total cars created: {cls.total_cars}"

    @staticmethod
    def is_luxury_brand(brand):
        luxury_brands = ["BMW", "Mercedes", "Audi", "Lexus", "Jaguar"]
        return brand in luxury_brands

    @property
    def on_road_price(self):
        # Add 18% GST
        return self._price * 1.18

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 100000:
            raise ValueError("Price cannot be less than ₹100,000.")
        self._price = value

car1 = Car("BMW", "X5", 2024, 7500000)

print(car1)                         # __str__ output
print(f"On-road price: ₹{car1.on_road_price}")   # property

car1.price = 8000000                # uses setter
print(f"Updated on-road: ₹{car1.on_road_price}")

# Try setting a low price to see error
# car1.price = 50000   # ❌ Raises ValueError
