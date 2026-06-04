class Car:

    def __init__(self, year_model, make):

        if year_model <= 0:
            raise ValueError("Invalid year model.")

        if make == "":
            raise ValueError("Make cannot be empty.")

        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):

        if self.__speed < 5:
            raise ValueError("Cannot brake below zero.")

        self.__speed -= 5

    def get_speed(self):
        return self.__speed


# Create Car object
car1 = Car(2025, "Toyota")

print("=== Accelerating ===")

for i in range(5):
    car1.accelerate()
    print(f"Speed after acceleration {i+1}: {car1.get_speed()}")

print("\n=== Braking ===")

for i in range(5):
    car1.brake()
    print(f"Speed after braking {i+1}: {car1.get_speed()}")