class Biscuits:
    def __init__(self,name,calories,place,sugar_level):
        self.name = name
        self.calories = calories
        self.place = place
        self.sugar_level = sugar_level
    def display(self):
        print("Biscuit Name: ",self.name)
        print("Calories: ",self.calories)
        print("Place: ",self.place)
        print("Sugar Level: ", self.sugar_level)
        print("----------------------------------")

a = Biscuits("Bourbon","479 kcal","Puducherry","39%")
a.display()
b= Biscuits("Parle-G","409 kcal","West Bengal","9%")
b.display()
