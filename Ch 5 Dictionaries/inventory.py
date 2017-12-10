mybag = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def printInventory(bag):
    print('Inventory:')
    itemTotal = 0
    for k, v in bag.items():
        print(str(v) + ' ' + str(k))
        itemTotal += v
    print('Total Number of Items: ' + str(itemTotal))


def addInventory(inventory, additems):
    for item in additems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

printInventory(mybag)
addInventory(mybag, dragonLoot)
printInventory(mybag)
