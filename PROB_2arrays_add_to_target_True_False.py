# Write an algorithm that takes in 2 arrays and an integer, and return true if any of the number (one from each array) adds up to the integer

def sum_integer (array1, array2, integer):
  for i in range (len(array1)):
    for k in range (len(array2)):
      if array1[i] + array2[k] == integer:
        return True
  return False

print sum_integer([1,2,3],[0,9,8],10)