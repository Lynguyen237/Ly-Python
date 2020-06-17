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