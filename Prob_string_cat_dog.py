#Cat_dog https://codingbat.com/prob/p164876
# Return True if the string "cat" and "dog" appear the same number of times in the given string.
# cat_dog('catdog')  True
# cat_dog('catcat')  False
# cat_dog('1cat1cadodog')  True

def cat_dog(str):
  cat_count = 0
  dog_count = 0
  for i in range (len(str)-2):
    #without len(str)-2, where will be an out of range error
    #For eg: len("catdog") is 6, range (6) is [0,1,2,3,4,5]
    #if iterate i in [0,1,2,3,4,5], then when i=5, i+3 = 8, that's longer than the length of the string "catdog" itself.
    if str[i:i+3] == "cat":
      cat_count += 1
    if str[i:i+3] == "dog":
      dog_count += 1
  if cat_count == dog_count:
    return True
  return False

print cat_dog("cats and dogs can live in the same catdog house")
#answer true