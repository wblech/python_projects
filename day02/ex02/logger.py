import time
from random import randint


class CoffeeMachine():
    water_level = 100

    def log(func):
        def wrapper(self, *args, **kwargs):
            fd = open("machine.log", "a")
            name = self.__get_name(func)
            start_time = time.time()
            result = func(self, *args, **kwargs)
            exec_time = time.time() - start_time
            time_scale = "s"
            if exec_time < 0.001:
                exec_time *= 1000
                time_scale = "ms"
            fd.write(f"(wbertoni)Running: {name}\t")
            fd.write(f"[ exec-time = {exec_time:.3f} {time_scale}\t]\n")
            return result
        return wrapper

    @staticmethod
    def __get_name(func):
        name = func.__name__
        name = [i.capitalize() for i in name.split("_")]
        name = " ".join(name)
        return name

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
