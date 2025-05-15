from abc import ABC


class Car(ABC):
    def __init__(self, type: str, brand: str, model: str, license_plate: str, rental_fee: float):
        self.type = type
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.rental_fee = rental_fee

    def __str__(self):
        return f"{self.license_plate} - {self.brand} {self.model} ({self.type}) ${self.rental_fee:.2f}/day"


class PassengerCar(Car):
    def __init__(self, brand: str, model: str, license_plate: str, rental_fee: float):
        super().__init__("Passenger Car", brand, model, license_plate, rental_fee)


class Truck(Car):
    def __init__(self, brand: str, model: str, license_plate: str, rental_fee: float):
        super().__init__("Truck", brand, model, license_plate, rental_fee)
