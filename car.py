class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5

    def get_speed(self):
        return self.__speed


car1 = Car(2025, "Toyota")

print("Accelerating")

for i in range(5):
    car1.accelerate()
    print(car1.get_speed())

print("Braking")

for i in range(5):
    car1.brake()
    print(car1.get_speed())