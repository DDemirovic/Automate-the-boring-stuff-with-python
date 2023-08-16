#! python 3
#Sandwhich Maker program

import pyinputplus as pyip
import re 

#function that is called, which is responsible for taking the order and calculating the price
def sandwhichProcess():
    sandwhichPriceList = {
        #bread
        "wheat": 0.5, "white": 0.5, "sourdough": 0.6,
        #protein
        "chicken": 1.1, "turkey": 1.1, "ham": 0.9, "tofu": 0.7,
        #cheese
        "cheddar": 0.3, "swiss": 0.3, "mozzarella": 0.2,
        #toppings
        "mayo": 0.1, "mustard": 0.1, "lettuce": 0.2, "tomato": 0.1
        }
    ingredients = sandwhichOrder()
    priceCalculator(ingredients, sandwhichPriceList)
    return

#function that takes the order for a sandwhich
def sandwhichOrder():
    listOfIngredients = []
    howManySandwhiches = pyip.inputInt("How many sandwhiches do you want? ", min = 1)
    for _ in range(howManySandwhiches):
        bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered = True, prompt = "Which bread do you want?\n")
        listOfIngredients.append(bread)
        protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], numbered = True, prompt = "Which protein do you want?\n")
        listOfIngredients.append(protein)
        cheeseQuestion = pyip.inputYesNo("Do you want cheese on your sandwhich? ")
        if cheeseQuestion:
            cheese = pyip.inputMenu(["cheddar", "swiss", "mozzarella"], numbered = True, prompt = "Which cheese do you want?\n")
            listOfIngredients.append(cheese)
        toppingsQuestion = pyip.inputYesNo("Do you want mayo, mustard, lettuce or tomato?\n")
        if "Yes" == toppingsQuestion or "Y" == toppingsQuestion or "yes" == toppingsQuestion or "y" == toppingsQuestion:
            toppings = pyip.inputMenu(["mayo", "mustard", "lettuce", "tomato"], numbered = True, prompt = "What exactly do you want to have on top?\n")
            while toppings != "I'm good, thanks.":
                if toppings != "I'm good, thanks.":
                    listOfIngredients.append(toppings)
                    toppings = pyip.inputMenu(["mayo", "mustard", "lettuce", "tomato", "I'm good, thanks."], numbered = True, prompt = "Do you want more?\n")
    return listOfIngredients

#function that calculates the price - it needs a list of something and a corresping dictionary (ideally with prices hehe)
def priceCalculator(listOfIngredients, priceList):
    totalCost = 0
    #adding up each ingredient to get totalCost
    for ingredient in listOfIngredients:
        totalCost += priceList[ingredient]
    print(f"Total cost: {totalCost}")
    return 

sandwhichProcess()