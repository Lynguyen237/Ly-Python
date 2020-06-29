#Practice manipulating user input
#Ask user if they like cats. If not, ask them what do they like
like_cat = raw_input ("Do you like cats? Answer Y or N: ")
if like_cat == "Y":
  print "Great!"
else:
  answer_cat = raw_input ("What's your favorite animal? ")

#Ask user if they like coffee. If yes, do they want it with sugar. If not, ask what's their favorite morning drink.
like_kopi = raw_input ("Do you drink coffee? Answer Y or N: ")
if like_kopi == "Y":
  answer_sugar = raw_input ("Do you put sugar in it? ")
else:
  answer_drink = raw_input ("What's your favorite morning drink? ")

#Ask user if they like joke. If yes, tell a joke. If not, record the reason why they don't like joke
like_joke = raw_input ("Do you like jokes? Answer Y or N: ")
if like_joke == "Y":
  answer_joke = raw_input ("What kind of melons can't marry? ")
  print "Catelopes"
else:
  reason = raw_input ("Why don't you like jokes? ")

#Print out all of their answer
print
print "Summary of your answers:"
print "Like cats: ", like_cat
if like_cat == "N":
  print "Favorite animal if not cats: ", answer_cat
print "Drink coffee: ", like_kopi
if like_kopi == "Y":
  print "Add sugar to coffee: ", answer_sugar
else:
  print "Favorite morning drink: ", answer_drink
print "Like jokes:" , like_joke
if like_joke == "Y":
  print "Answer to the joke: ", answer_joke
else:
  print "Reasons for not liking joke: ", reason