class ElectronicDevice:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"{self.brand} device is powering on.")

class SmartFunctionality:
    def __init__(self, os):
        self.os = os

    def run_app(self, app_name):
        print(f"Running {app_name} on {self.os}.")

class SmartTV(ElectronicDevice, SmartFunctionality):
    def __init__(self, brand, os, screen_size):
        ElectronicDevice.__init__(self, brand)
        SmartFunctionality.__init__(self, os)
        self.screen_size = screen_size

    def display_info(self):
        print(f"Smart TV: {self.brand}, OS: {self.os}, Screen Size: {self.screen_size} inches")

# Example Usage
my_tv = SmartTV("Samsung", "Tizen", 55)
my_tv.power_on()
my_tv.run_app("Netflix")
my_tv.display_info()