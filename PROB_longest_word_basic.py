#Print the longest word in a sentence
#==========
#SOLUTION 1: Longest word - Long way:
#==========

#sentence = raw_input("Give me a sentence: ")
sentence = "Black Lives Matter"
sentence_word = sentence.split()

word_length_dict = {}
for word in sentence_word:
  word_len = len(word)
  if word_len not in word_length_dict:
    word_length_dict [word_len] = []
    word_length_dict [word_len].append (word)
print word_length_dict

word_len_list = []
for length in word_length_dict:
  word_len_list.append (length)
longest_word_index = max (word_len_list)
print word_length_dict [longest_word_index]

#==========
#SOLUTION 2: Longest word - SHORTER way:
#==========
print
sentence = "Life is beautiful"
sentence_word = sentence.split()
longest_word = ""

for word in sentence_word:
  if len(word) > len (longest_word):
    longest_word = word
print longest_word
