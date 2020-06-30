# Write an algorithm that accepts a list of numbers. It should return pairs of indices whose elements multiply to the target.
# [1,2,3,9],9 = > 0,3

def product(arrayx, target):
  for i in range (len(arrayx)):
    for k in range (i+1, len(arrayx)):
      if arrayx[i]*arrayx[k] == target:
        return ([i,k])
  return False

print product ([2,3,4,5],6)