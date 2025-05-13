class Person:
    def __init__(self, name, money, mood="neutral", health_rate="100%"):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    def sleep(self, hours):
        """Update mood based on sleep hours"""
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"
        print(f"{self.name}'s mood is now {self.mood} after sleeping {hours} hours.")

    def eat(self, meals):
        """Update health rate based on meals"""
        health_rates = {3: "100%", 2: "75%", 1: "50%"}
        self.health_rate = health_rates.get(meals, "50%")
        print(f"{self.name}'s health rate is now {self.health_rate} after {meals} meals.")

    def buy(self, items):
        """Deduct money for purchased items"""
        cost = items * 10
        if self.money >= cost:
            self.money -= cost
            print(f"{self.name} bought {items} items. Remaining money: {self.money} LE")
        else:
            print(f"{self.name} doesn't have enough money to buy {items} items.")


class Car:
    def __init__(self, name, fuel_rate=100, velocity=0):
        self.name = name
        self.fuel_rate = min(max(fuel_rate, 0), 100)  # Ensure between 0-100
        self.velocity = min(max(velocity, 0), 200)     # Ensure between 0-200

    @property
    def fuel_rate(self):
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, value):
        self._fuel_rate = min(max(value, 0), 100)

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = min(max(value, 0), 200)

    def run(self, velocity, distance):
        """Start the car and consume fuel"""
        self.velocity = velocity
        print(f"{self.name} is moving at {self.velocity} km/h for {distance} km.")
        
        fuel_consumed = distance * 0.1  # 10% per 10 km
        if fuel_consumed > self.fuel_rate:
            actual_distance = self.fuel_rate * 10
            self.fuel_rate = 0
            self.stop(distance - actual_distance)
        else:
            self.fuel_rate -= fuel_consumed
            self.stop(0)

    def stop(self, remaining_distance):
        """Stop the car and show status"""
        self.velocity = 0
        if remaining_distance > 0:
            print(f"{self.name} stopped. {remaining_distance} km remaining (out of fuel).")
        else:
            print(f"{self.name} arrived at destination and stopped.")


class Employee(Person):
    def __init__(self, emp_id, car, email, salary, distance_to_work, **kwargs):
        super().__init__(**kwargs)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work

    def work(self, hours):
        """Update mood based on work hours"""
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"
        print(f"{self.name}'s mood is now {self.mood} after working {hours} hours.")

    def drive(self, distance=None, velocity=None):
        """Drive to work with optional parameters"""
        distance = distance or self.distance_to_work
        velocity = velocity or self.car.velocity
        
        print(f"{self.name} is driving to work...")
        self.car.run(velocity, distance)

    def refuel(self, gas_amount=100):
        """Refuel the car"""
        self.car.fuel_rate += gas_amount
        print(f"{self.name} refueled the car. Current fuel: {self.car.fuel_rate}%")

    def send_mail(self, to, subject, body):
        """Send email to someone"""
        print(f"""
        From: {self.email}
        To: {to}
        Subject: {subject}
        Body: {body}
        """)


class Office:
    employees_num = 0  # Class variable to track total employees

    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        """Hire a new employee"""
        self.employees.append(employee)
        Office.employees_num += 1
        print(f"Hired {employee.name} at {self.name}. Total employees: {Office.employees_num}")

    def fire(self, emp_id):
        """Fire an employee by ID"""
        for emp in self.employees:
            if emp.id == emp_id:
                self.employees.remove(emp)
                Office.employees_num -= 1
                print(f"Fired employee {emp_id}. Total employees: {Office.employees_num}")
                return
        print(f"Employee {emp_id} not found!")

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        """Check if employee will be late"""
        if velocity == 0:
            return True
        travel_time = distance / velocity
        return (move_hour + travel_time) > target_hour

    def check_lateness(self, emp_id, move_hour, target_hour=9.0):
        """Check and handle late employees"""
        emp = next((e for e in self.employees if e.id == emp_id), None)
        if not emp:
            print(f"Employee {emp_id} not found!")
            return

        is_late = self.calculate_lateness(
            target_hour,
            move_hour,
            emp.distance_to_work,
            emp.car.velocity
        )

        if is_late:
            emp.salary -= 10
            print(f"{emp.name} is late! 10 LE deduction. New salary: {emp.salary}")
        else:
            emp.salary += 10
            print(f"{emp.name} is on time! 10 LE reward. New salary: {emp.salary}")