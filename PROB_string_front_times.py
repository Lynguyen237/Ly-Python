#Problem 5: https://codingbat.com/prob/p165097
# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
# front_times('Chocolate', 2)  'ChoCho'
# front_times('Chocolate', 3)  'ChoChoCho'
# front_times('Abc', 3)  'AbcAbcAbc'

#SOLUTION #1
print 
def front_times(str, n):
  char = ""
  if len (str) >= 3:
    char = str[0]+str[1]+str[2]
  else:
    char = str
  outcome = ""
  for y in range (n):
    outcome = outcome + char
  # print outcome
  return outcome
print front_times ("ab", 5)

#I made a mistake when setting char == str instead of "=". "==" should be understood as "Is" while "=" is used to assign value to a variable.

#SOLUTION #2

print
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  print result
  return result

a = front_times("ab", 2)
# print a
print front_times("ab", 2)
