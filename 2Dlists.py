# 2D/Multidimensional lists = a list of lists

drinks = ["Coffee", "Soda", "Tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert] # this will add all the items from the lists to food list
print(food)
# you can access these lists like normal lists
print(food[0]) # will print the drinks list
print(food[0][0]) # will print Coffee from drinks lists, first item of first item
print(food[2][1])