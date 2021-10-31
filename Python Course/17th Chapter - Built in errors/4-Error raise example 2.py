# Error raise example 2

class Mobile:
    def __init__(self, brand):
        self.brand = brand

class Mobile_Store:
    def __init__(self):
        self.mobiles = []

    def add_mob(self, New):
        if isinstance(New,Mobile):
            self.mobiles.append(New)
        else :    
            raise TypeError('This is not instance of mobile class')

oneplus = Mobile('Oneplus 6')
sumsung = 'sumsung xyz'
mobilesto = Mobile_Store()
print(mobilesto.mobiles)
mobilesto.add_mob(oneplus)
x = mobilesto.mobiles
print(x[0].brand)