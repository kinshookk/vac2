"""

AA0 to FF9
structure : 1.year of manufacture 2.material 3.quantity
functions : 1. add data 2. bb1 to cc6 information retrival 
bb1 to bb9-> 9
cc0 to cc6 -> 7 
16


An automobile company has serial number for engine parts starting from AA0 to FF9.
The other characteristics of parts to be specified in a structure are: Year of manufacture,
material and quantity manufactured. (a) Specify a structure to store information
corresponding to a part. (b) Write a program to retrieve information on parts with serial
numbers between BB1 and CC6.
"""
import random
class Parts:
    def __init__(self,year,material,quantity):
        self.year=year
        self.material=material
        self.quantity=quantity
class Collection_of_Parts:
    def __init__(self):
        self.first=64
        self.collection={}
        j=0
        for i in range(0,60):
            if i%10==0:
                self.first+=1
                self.index=chr(self.first)+chr(self.first)
            temp=self.index+str(j)
            j=(j+1)%10
            self.collection[temp]=None
    def addpart(self,year,material,quantity,serialNumber:str):
        new_part=Parts(year,material,quantity)
        self.collection[serialNumber]=new_part
    def printdata(self):
        first=66
        index=chr(first)+chr(first)
        j=0
        for i in range(0,17):
            if i==10:
                first+=1
                index=chr(first)+chr(first)
            temp=index+str(j)
            j=(j+1)%10
            print(f"{temp}-> Year of Manufacture : {self.collection[temp].year} Material : {self.collection[temp].material} Quantity : {self.collection[temp].quantity}")

Collection = Collection_of_Parts()
letters = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF']
all_serial_numbers = []
for letter in letters:
    for num in range(10):
        serial = f"{letter}{num}"
        all_serial_numbers.append(serial)
for serial in all_serial_numbers:
    Collection.addpart(2024, "Random Material", random.randint(1, 10), serial)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Printing value of engine part from BB1 to CC6")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Collection.printdata()


