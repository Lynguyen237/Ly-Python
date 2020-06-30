#Given a list of integers, make a function that takes that list as input and returns the sum of the even numbers as output.
#[1,2,3,4,5,6] = > 2+4+6 = 12

#Shorter way
def even_sum (list_integers):
  sums = 0
  for i in list_integers:
    if i % 2 == 0:
      sums += i
  return sums

print even_sum([1,2,4,5])

#Longer way
def even_sum2(list_integers):
  sum_value = 0
  for i in range (len(list_integers)):
    if list_integers[i] % 2 == 0:
      sum_value = sum_value + list_integers[i]
  return sum_value

print even_sum2 ([3,7,8,0])