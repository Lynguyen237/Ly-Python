import re


######################
# Regular Expression #
######################
def find_string_between_substrings(text):
    result = re.search(':(.*){', text) # find a match between ":" and the last occurrence of "{"
    print("match till the last occurence of `{`: ", result.group(1))

    # place a lazy flag ? behind the zero-or-more quantifier * to change its behavior to lazy. 
    # This will cause it so match as few characters as possible while still complying with the rest of the expression.
    result = re.search(':(.*?){', text) # find a match between ":" and the first occurrence of "{"
    print("math till the first occurence: `{`", result.group(1))

test_str = "summary: Title {xyz} {abc}"
# find_string_between_substrings(test_str)
# match till the last occurence of `{`:  Title {xyz} 
# match till the first occurence of `{`:  Title 
# https://regexland.com/regex-to-match-everything-before-a-specified-character-or-symbol/

