import time

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


car1 = Car(2025, "Toyota")

print("=" * 60)
print(("CAR SPEED SIMULATOR").center(60))
print("=" * 60)

print(f"Year Model : 2025")
print(f"Make       : Toyota")
print(f"Speed      : {car1.get_speed()} km/h")

print("\n" + "=" * 60)
print("ACCELERATION TEST")
print("=" * 60)

for i in range(5):

    car1.accelerate()

    print(
        f"[{i+1}/5] Speed increased by 5 km/h "
        f"| Current Speed: {car1.get_speed()} km/h"
    )

    time.sleep(0.5)

print("\n" + "=" * 60)
print("BRAKING TEST")
print("=" * 60)

for i in range(5):

    car1.brake()

    print(
        f"[{i+1}/5] Speed decreased by 5 km/h "
        f"| Current Speed: {car1.get_speed()} km/h"
    )

    time.sleep(0.5)

print("\n" + "=" * 60)
print(("Simulation Completed Successfully").center(60))
print("=" * 60)