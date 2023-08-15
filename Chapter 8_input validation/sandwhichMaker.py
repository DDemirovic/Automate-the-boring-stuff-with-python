#! python 3
#Sandwhich Maker program

import pyinputplus as pyip
import re 

def sandwhichProcess():
    ingredients = sandwhichOrder()
    priceCalculator(ingredients)
    return

def sandwhichOrder():
    listOfIngredients = []
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered = True, prompt = "Which bread do you want?\n")
    listOfIngredients.append(bread)
    protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], numbered = True, prompt = "Which protein do you want?\n")
    listOfIngredients.append(protein)
    cheeseQuestion = pyip.inputYesNo("Do you want cheese on your sandwhich (Yes or No)? ")
    if cheeseQuestion:
        cheese = pyip.inputMenu(["cheddar", "swiss", "mozzarella"], numbered = True, prompt = "Which cheese do you want?\n")
        listOfIngredients.append(cheese)
    toppingsQuestion = pyip.inputYesNo("Do you want mayo, mustard, lettuce or tomato?\n")
    if toppingsQuestion:
        toppings = pyip.inputMenu(["mayo", "mustard", "lettuce", "tomato"], numbered = True, prompt = "What exactly do you want to have on top?\n")
        while toppings != "I'm good, thanks.":
            if toppings != "I'm good, thanks.":
                listOfIngredients.append(toppings)
                toppings = pyip.inputMenu(["mayo", "mustard", "lettuce", "tomato", "I'm good, thanks."], numbered = True, prompt = "Do you want more?\n")
    howManySandwhiches = pyip.inputInt("How many sandwhiches do you want? ", min = 1)
    return listOfIngredients

def priceCalculator(listOfIngredients):
    totalCost = 0
    priceList = {
        #bread
        "wheat": 0.50, "white": 0.50, "sourdough": 0.60,
        #protein
        "chicken": 1.1, "turkey": 1.15, "ham": 0.9, "tofu": 0.75,
        #cheese
        "cheddar": 0.35, "swiss": 0.3, "mozzarella": 0.35,
        #toppings
        "mayo": 0.1, "mustard": 0.1, "lettuce": 0.2, "tomato": 0.15
        }
    #print(myPriceList["protein"]["chicken"])
    print(f"Total cost: {totalCost}")
    return 

sandwhichOrder()