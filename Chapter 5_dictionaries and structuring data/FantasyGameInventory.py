#Function that displays inventory
def displayInventory(inventory):
    print("Your Inventory:")
    item_total = 0
    for keys, values in inventory.items():
        item_total = item_total + inventory[keys]   #inventory[keys] = the associated number for that specific key in the loop
        print(f"{keys}: {values}")  #f-string is "super important", otherwhise output would be "key : value", the space between key and ":" is unneeded
    print(f"Total number of items: {item_total}")

def addToInventory(inventory,loot):     #addToInventory(someDictionary,someList)
    for items in loot:
        if items in inventory:          #if the item from that list is in my inventory already, add it on top of it
            inventory[items] += 1
        if items not in inventory:      #if the item from that list is not(!) in my inventory already, add it and give it a value of 1 (since we added it)
            inventory[items] = 1
        
myInventory = {'rope':1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 }

myLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'a miraculous job interview', 'a space pirate figurine']

displayInventory(myInventory)
addToInventory(myInventory,myLoot)
displayInventory(myInventory)