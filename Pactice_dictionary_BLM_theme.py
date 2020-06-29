#Check if a key exist in the dictionary
my_pets = {'cats': 2, 'dog':5}
if 'elephant' in my_pets:
  elephant_count = my_pets ['elephant']
else:
  elephant_count = 0
print 'Number of elephants I have: ', elephant_count
print my_pets

for animal in my_pets:
  animal_count = my_pets [animal]
  print animal, 'count: ', animal_count

#Sentence example
print
word_lengths = {}
sentence = 'Black Lives Matter'
sentence_words = sentence.split()
for word in sentence_words:
  word_len = len (word)
  if word_len not in word_lengths:
    word_lengths[word_len]=[]
  word_lengths[word_len].append(word)
print word_lengths

#practice section
print
soccer_team = {}
soccer_team ['team_name'] = 'social justice'
soccer_team ['team_ranking'] = 1
soccer_team ['player_names'] = ['Breanna', 'George', 'Trevor']
soccer_team ['team_ranking'] += 1
soccer_team['player_names'].append ('Nadie!')

print soccer_team
if soccer_team ['team_ranking'] <= 3:
  print "Congrats, we are making progress!"
else:
  print "Can't let setbacks discourage us!"

print
for player_name in soccer_team ['player_names']:
  print player_name

#9
soccer_team ['team_color'] = 'blue'
if 'team_color' in soccer_team:
  print "team color is: ", soccer_team ['team_color']
else:
  print "The team is currently colorless"

soccer_team ['movies']= 'The last black man in SF'
soccer_team ['book'] = 'Between the world and me'
soccer_team ['article'] = '20 ways to be an Asian ally'

print
print "All team attributes are below:"
for attribute in soccer_team:
  attribute_value = soccer_team [attribute]
  print attribute , ':', attribute_value