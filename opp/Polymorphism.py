# parent class
class Device:
    def make_call(self):
        print("Making a call from a generic device.")

# child class

class Phone(Device):
    def make_call(self):
        print("Making a call from a Phone via SIM card.")

class Tablet(Device):
    def make_call(self):
        print("Making a call from a Tablet using VoIP.")

class Laptop(Device):
    def make_call(self):
        print("Making a call from a Laptop using Skype.")

# Polymorphism in Action
devices=[Phone(),Tablet(),Laptop()]

for device in devices:
    device.make_call()



