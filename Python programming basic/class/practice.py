class Car:
    default_speed = 200

    def __init__(self, wheels = 4, chair = 4, engine = "V8", max_speed = default_speed):
        self.wheels = chair
        self.chair = chair
        self.engine = engine
        self.max_speed = 200

    def full_speed(self):
        print(self.max_speed)

prius = Car()
prius.default_speed = 300
print(prius.default_speed)