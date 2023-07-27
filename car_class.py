class Car:
    def __init__(self, make, model, is_running=False):
        self.make = make
        self.model = model
        self.is_running = is_running

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model}: Engine started.")
        else:
            print(f"{self.make} {self.model}: Engine is already running.")


class ElectricCar(Car):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.battery_level = 100


class AnotherTypeOfCar(Car):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.hydrogen_level = 95


def perform_engine_action(car):
    car.start()


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = ElectricCar("Tesla", "Y")
car4 = AnotherTypeOfCar("Toyota", "X")

perform_engine_action(car1)
perform_engine_action(car2)
perform_engine_action(car3)
perform_engine_action(car4)

