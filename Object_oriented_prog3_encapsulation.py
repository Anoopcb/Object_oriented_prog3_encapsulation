## Encapsulation ## you have to put all your methods near your data
## abstraction== to hide complexcity
## some special naming convention## just to tell the programmer, this is private

## name mangling== we use __name

class Phone:

    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)
        self.complete_specification = f"{self.brand} {self.model_name} {self._price}"

    def make_a_call(self, phone_number):
        print(f"calling{phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def send_message(self):
        pass
## everthing in python is public and object

#__name__## dunder, they are also called magick mathods
phone1 = Phone("Iphone", "XR", 910000)
print(phone1._price)
phone1._price = -1000
print(phone1._price)
print(phone1.complete_specification)


l = [1, 2, 4, 3]
l.sort()## tim sort
print(l)



































