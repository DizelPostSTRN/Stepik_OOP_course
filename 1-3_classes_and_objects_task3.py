# Declare an empty class named Car. Use the setattr() function to add attributes to this class:
# model: "Тойота"
# color: "Розовый"
# number: "П111УУ77"
# Display the value of the color attribute using the __dict__ dictionary of the Car class.


class Car:
    pass


setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "П111УУ77")

print(Car.__dict__['color'])
