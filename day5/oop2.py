class Car:
    total_cars = 0  # Class attribute

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.total_cars += 1

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

    @classmethod
    def show_total_cars(cls):
        return f"Total cars created: {cls.total_cars}"

    @staticmethod
    def is_luxury_brand(brand):
        luxury_brands = ["BMW", "Mercedes", "Audi", "Lexus", "Jaguar"]
        return brand in luxury_brands

car1 = Car("BMW", "M5", 2020)
car2 = Car("Hyundai", "i20", 2022)
car3 = Car("Mercedes", "Maybach", 2023)

print(Car.show_total_cars())   # Class method

# Static method
print(Car.is_luxury_brand("BMW"))      # True
print(Car.is_luxury_brand("Suzuki"))   # False
