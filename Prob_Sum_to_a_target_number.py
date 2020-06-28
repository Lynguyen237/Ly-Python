# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

#===========================
#SOLUTION 1 - Loop with list
#===========================
def sum_target (int_array,target):
   for i in range (len(int_array)):
     for k in range (i+1, len(int_array)):
       if int_array[i]+int_array[k] == target:
         return [i,k]

print sum_target ([2,7,11,15],9)

#=================================
#SOLUTION 2 - Loop with dictionary
#=================================
def sum_target (int_array, target):
  dictionary = {}
  for i in range (len(int_array)):
    secondNumber = target - int_array [i]
    if secondNumber in dictionary.keys():
      secondIndex = int_array.index(secondNumber)
      if i != secondIndex:
        return [i, secondIndex]
    dictionary.update({int_array [i]:i})

print sum_target ([2,11,7,15],9)