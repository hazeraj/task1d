import random


class Vehicle:
    vehicle_id = 0
    vehicles_sold = []

    def __init__(self, year, mileage, purchase_price, serial_number):
        self.__year = year
        self.__mileage = mileage
        self.__purchase_price = purchase_price
        self.__serial_number = serial_number
        self.__vehicle_id = self.generate_vehicle_id(self)
        Vehicle.vehicle_id += 1

        try:
            i = int(self.__year)
            j = int(self.__mileage)
            k = int(self.__purchase_price)
        except ValueError:
            print("Error: Year, mileage and purchase price need to be numbers.")

    def __str__(self):
        return self.get_id()

    @staticmethod
    def generate_vehicle_id(self):
        return Vehicle.vehicle_id+100000

    def get_id(self):
        return str(self.__vehicle_id)


class Car(Vehicle):
    def __init__(self, year, mileage, purchase_price, serial_number, doors):
        super().__init__(year, mileage, purchase_price, serial_number)
        self.__doors = doors
        self.__wheels = 4


class Lorry(Vehicle):
    def __init__(self, year, mileage, purchase_price, serial_number, wheels, doors=2):
        super().__init__(year, mileage, purchase_price, serial_number)
        self.__wheels = wheels
        self.__doors = doors


class Motorcycle(Vehicle):
    classic_count = 0

    def __init__(self, year, mileage, purchase_price, serial_number, classic=False):
        super().__init__(year, mileage, purchase_price, serial_number)
        self.__classic = classic
        if classic:
            self.classic_count += 1


class Customer:
    def __init__(self, name):
        self.__name = name
        self.__score = self.credit_score()

    def __str__(self):
        return "Customer: {}".format(self.__name)

    def credit_score(self):
        integer = random.randint(0,100)
        if integer > 60:
            return True
        else:
            return False

    def get_score(self):
        return self.__score


class VIP_Customer(Customer):
    def credit_score(self):
        return True


class Employee:
    emp_id = 0

    def __init__(self, name):
        self.__name = name
        self.__id = self.emp_id+1

    def __str__(self):
        return "Employee: {} is of type {}.".format(self.__name, self.get_title())

    def get_name(self):
        return self.__name

    def get_title(self):
        return "Subordinate"


class Salesman(Employee):
    sales = {}

    def sale(self, Vehicle, sales_price, customer):
        if customer.credit_score():
            self.sales[Salesman.get_name(self)] = sales_price
        else:
            print("The customer does not have enough credit score.")


class Manager(Employee):
    def get_title(self):
        return "Manager"

    def get_sales_report(self, Salesman):
        try:
            print("{}'s current cumulative sales: {}".format(Salesman.get_name(), Salesman.sales[Salesman.get_name()]))
        except KeyError:
            print("{} has no sales yet.".format(Salesman.get_name()))





