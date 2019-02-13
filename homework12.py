# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:25:18 2019

@author: zaghalayini
"""
#Task 1
class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0,-4.5)
print(x.r)
print(x.i)


#Task 2
class Bag:
    def __init__(self):
        self.data = []
        
    def add(self,x):
         self.data.append(x)
    def addtwice(self,x):
        self.add(x)
        self.add(x)
        
baggy = Bag()
baggy.add("backpack")
baggy.addtwice("packback")

#Task 3

class Box:
    def __init__(self,width = 0,length = 0):
        self.w = width
        self.l = length
    def area(self):
        return self.w * self.l

boxie = Box(5,3)
print(boxie.area())

#Task 4

class Student:
    def __init__(self, name = "empty",branch = "NA",year = "0000"):
        self.n = name
        self.b = branch
        self.y = year
        print("A student object is created")
    def print_details(self):
        print("\n Name: %s \n Branch: %s \n Year: %s \n" % (self.n,self.b,self.y))
    
studentie = Student("katty","CO","2017")
studentie.print_details()


#Task 5
class bank:
    def __init__(self,initial_balance = 0):
        self.i_b = initial_balance
        print(self)
    def withdrawl(self,x):
        if x > self.i_b:
            print("Amount greater than available balance.")
        else:
            self.i_b -= x
            print(self)
    def deposit(self,x):
        self.i_b += x
        print(self)
    def __str__(self):
        return "\nCurrent balance: $%.1f" % (self.i_b)
    
Jack = bank(100)
Jack.deposit(100)
Jack.withdrawl(40)
print(Jack)


























