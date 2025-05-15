from datetime import date

from Car import PassengerCar, Truck
from CarRentalCompany import CarRentalCompany

separator = "=" * 100

menu = f"""{separator}
Choose an option:
  1. Rent a car
  2. Cancel a rental
  3. Display all rentals
  4. Display all cars
  5. Exit
Selected option: """


def main():
    cars = [
        PassengerCar("Suzuki", "Swift", "ABC123", 40.0),
        PassengerCar("VW", "Golf", "BCD234", 50.0),
        Truck("Ford", "Transit", "XYZ987", 80.0),
    ]
    rental_company = CarRentalCompany("GDE Car Rental", cars)

    rental_company.rent("ABC123", date(2025, 10, 1))
    rental_company.rent("ABC123", date(2025, 10, 2))
    rental_company.rent("BCD234", date(2025, 10, 1))
    rental_company.rent("XYZ987", date(2025, 10, 3))

    while True:
        choice = input(menu)
        match choice:
            case "1":
                rent_car(rental_company)
            case "2":
                cancel_rental(rental_company)
            case "3":
                print(f"{separator}\nActive rentals:")
                for rental in rental_company.rentals:
                    print(f"  {rental}")
            case "4":
                print(f"{separator}\nAvailable cars:")
                for car in rental_company.cars:
                    print(f"  {car}")
            case "5":
                return
            case _:
                print(f"{separator}\nInvalid option. Please try again.")


def rent_car(rental_company: CarRentalCompany):
    license_plate = input("Enter the license plate of the car: ")
    rental_date = input("Enter the rental date (YYYY-MM-DD): ")
    try:
        rental_date = date.fromisoformat(rental_date)
    except ValueError:
        print(f"{separator}Invalid date format. Please use YYYY-MM-DD.")
    try:
        rental = rental_company.rent(license_plate, rental_date)
        print(f"{separator}\nRental created: {rental}")
    except ValueError:
        print(f"{separator}\nLicense plate not found. Please check the license plate and try again.")


def cancel_rental(rental_company: CarRentalCompany):
    try:
        rental_id = int(input("Enter rental id: "))
        success = rental_company.cancel_rental(rental_id)
        print(separator)
        print("Rental cancelled successfully." if success else "Rental not found. Check the id and try again.")
    except ValueError:
        print("Invalid input. Please enter a valid rental id.")


if __name__ == "__main__":
    main()
