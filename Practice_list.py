# Part 1
print "Part 1"
travel1 = raw_input ("Where would you like travel to? ")
travel2 = raw_input ("What is another place you would like to travel to? ")
travel3 = raw_input ("What is one more place you would like travel to? ")
travel_list = []
travel_list.append (travel1)
travel_list.append (travel2)
travel_list.append (travel3)

travel_list.sort ()
print "Places you would like to go are:"
print travel_list[0]
print travel_list[1]
print travel_list[2]

# Part 2
print
print "Part 2"
fun_words = ["elephant", "balloon", "macchiato", "angostura"]
first_letters = []
third_letters = []
word1 = fun_words [0]
print fun_words [0]
word1_first_letter = word1 [0]
print word1_first_letter [0]
first_letters_list = []
first_letters_list.append (word1_first_letter)

#Part 3
print
print "Part 3"
websites = ["facebook", "twitter", "buzzfeed"]
fruits = ["apple", "banana", "mango", "berry"]
names = ["Bob", "Alice", "Henry", "Rick", "Carl"]
list_length =[]
list_length.append (len (websites))
list_length.append (len (fruits))
list_length.append (len (names))
print list_length

#part 4
print
print "Part 4"
numbers = range (25)
print range (25)
print numbers [0] #print the first number
print numbers [4] #print the 5th number
print numbers [9] #print the 10th number
print numbers [14] #print the 14th number