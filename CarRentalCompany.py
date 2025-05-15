from datetime import date

from Car import Car


class CarRentalCompany:
    def __init__(self, name: str, cars: list):
        self.name = name
        self.cars = cars
        self.rentals = []

    def rent(self, license_plate: str, date):
        for car in self.cars:
            if car.license_plate.lower() == license_plate.lower():
                rental = CarRental(car, date)
                self.rentals.append(rental)
                return rental
        raise ValueError("Invalid license_plate")

    def cancel_rental(self, id: int):
        for rental in self.rentals:
            if rental.id == id:
                self.rentals.remove(rental)
                return True
        return False

    def rentals(self):
        return self.rentals

    def cars(self):
        return self.cars


class CarRental:
    _id_counter = 0

    def __init__(self, car: Car, rental_date: date):
        CarRental._id_counter += 1
        self.id = CarRental._id_counter
        self.car = car
        self.date = rental_date

    def __str__(self):
        return f"{self.id}: {self.car.license_plate} - {self.date} ({self.car.brand} {self.car.model})"
