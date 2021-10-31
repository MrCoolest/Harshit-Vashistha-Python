# Exercise 1 

class Laptop:
    def __init__(about,brand,model,price):
        about.brand_name = brand
        about.model_name = model
        about.price_value = price
        about.laptop_name = brand + ' ' + model + ' ' + str(price)


Lap1 = Laptop('Lenovo','Xyz',70000)
lap2 = Laptop('Dell','abc',90000)

print(Lap1.model_name,Lap1.brand_name)
print(lap2.brand_name,lap2.price_value)
print(lap2.laptop_name)
