#Let's figure out what's the quantity for each ingridient to make 2 cakes
cake_ingredients = {'butter': 1, 'shorterning': 0.5, 'sugar':3, 'egg substitue': 1.5, 'flour': 3, 'milk': 1, 'salt': 0.01, 'baking power': 0.01}

print "To make two cakes, you need:"
for x in cake_ingredients:
  cake_ingredients [x] = cake_ingredients [x]*2
  print cake_ingredients[x], "cups of", x

input = raw_input("What ingredient would you like to know about for 1 cake? ")

if input in cake_ingredients:
  print "One cake has", cake_ingredients [input]/2,"cups of", input
else:
  print "This cake does not contain", input


#Modification - get input on the number of cakes then print the ingredient list accordingly
print
print "Let's go big!"
no_of_cake = raw_input("How many cakes do you want to make? ")
no_of_cake_int = int (no_of_cake)

print "To make", no_of_cake, "cakes, you need:"

for y in cake_ingredients:
  cake_ingredients[y] = cake_ingredients[y]/2 * no_of_cake_int
  print cake_ingredients [y], "cups of", y