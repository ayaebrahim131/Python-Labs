from classes import Person, Employee, Car, Office

def main():
    # Create a car
    samy_car = Car(name="Fiat 128", fuel_rate=50, velocity=60)

    # Create an employee
    samy = Employee(
        emp_id=1,
        car=samy_car,
        email="samy@iti.com",
        salary=5000,
        distance_to_work=20,
        name="Samy",
        money=1000
    )

    # Create an office
    iti_office = Office("ITI Smart Village")

    # Hire the employee
    iti_office.hire(samy)

    # Test functionalities
    samy.sleep(6)
    samy.eat(2)
    samy.buy(3)
    samy.drive()
    samy.work(8)
    iti_office.check_lateness(1, 8.5)  # Check if Samy is late when leaving at 8:30 AM

if __name__ == "__main__":
    main()