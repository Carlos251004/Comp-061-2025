# 1. Car Class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
      
    def get_car_info(self):
        return f"{self.year} {self.make} {self.model}"
        pass


# 2. Owner Class
class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cars_owned = []
    

    def purchase_car(self, car):
        self.cars_owned.append(car)
        print(f"{self.name} just purchased a {car.get_car_info()}.")
        pass

    def show_owned_cars(self):
        print(f"{self.name} owns the following cars:")
        for car in self.cars_owned:
            print(f" - {car.get_car_info()}")
        pass


# 3. Main Demonstration Function
def main():
    owner1 = Owner("Alice", 30)
    owner2 = Owner("Bob", 45)
    
    car1 = Car("Toyota", "Camry", 2010)
    car2 = Car("Honda", "Civic", 2018)
    car3 = Car("Ford", "Mustang", 2022)
    car4 = Car("Chevrolet", "Malibu", 2015)

    owner1.purchase_car(car1)
    owner1.purchase_car(car2)
    owner2.purchase_car(car3)
    owner2.purchase_car(car4)

    owner1.show_owned_cars()
    owner2.show_owned_cars()
    
    pass


# 4. Execution
if __name__ == "__main__":
    main()