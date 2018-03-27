class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):

        return self.value

    def getCost(self):

        return self.calories

    def density(self):

        return self.getValue() / self.getCost()

    def __str__(self):
        # why not __repr__(slef)?

        return self.name + ': < ' + str(self.value)\
                + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):

    """ names , values, calories list of same length.
    name a ist of strings
    value and calories lists of numbers 
    return list of Foods"""

    menu = []

    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))

    return menu 


def greedy(items, maxCost, keyFunction):

    """Assumes items a list , maxCost > 0, 
    keyFunction maps elements of items to numbers"""

    itemsCopy = sorted(items, key = keyFunction, 
                        reverse  = True)

    result = []
    totalValue , totalCost = 0.0 , 0.0

    for i in range(len(itemsCopy)):
        if(totalCost + itemsCopy[i].getCost()) <= maxCost:
            
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):

    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of itmes taken = ', val)

    for item in taken:
        print('   ' , item)

def testGreedys(foods, maxUnits):
    print('User greedy by value to allocate', maxUnits,
            'calorires')
    testGreedy(foods, maxUnits, Food.getValue)
    print('User greed by cost to allocate', maxUnits,
            'calories')
    testGreedy(foods, maxUnits,
                lambda x: 1/Food.getCost(x))
    print('User greedy by density to allocate', maxUnits, 
            'calories')
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 
        'cola', 'apple', 'donut', 'cake']

values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
        
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)


'''
KeyFunction ! 

how to map name to number ?

'''
