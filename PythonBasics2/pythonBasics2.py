# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add 
# what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes a string and
# returns the multiples of 3 that occurs most in a string
# to n (including n).

from asyncio.windows_events import NULL


def count_threes(n):
  multiples = {
    'numThrees' : 0,
    'numSix' : 0,
    'numNine' : 0
  }
  for i in range(0,len(n)):
    i = int(i)
    if int(n[i]) % 3 == 0:
      if int(n[i]) / 3 == 1:
        multiples['numThrees'] += 1
      elif int(n[i]) / 3 == 2:
        multiples['numSix'] += 1
      elif int(n[i]) / 3 == 3:
        multiples['numNine'] += 1
  
  if multiples['numThrees'] > multiples['numSix'] and multiples['numThrees'] > multiples['numNine']:
    return 3
  elif multiples['numSix'] > multiples['numThrees'] and multiples['numSix'] > multiples['numNine']:
    return 6
  elif multiples['numNine'] > multiples['numThrees'] and multiples['numNine'] > multiples['numSix']:
    return 9


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(stringS):
  longestChar = stringS[0]
  longest = 0
  longestChars = {
    
  }
  for i in range (0,len(stringS)):
    count = 0
    for j in range(i+1,len(stringS)):
      if (stringS[i] == stringS[j]):
        count += 1
      else:
        break
    if count > longest:
      count = longest
      longestChars['longest'] = stringS[i]
    if i == len(stringS):
      if count == longest:
        longestChars[i] = longestChar
  valueList= list(longestChars.values())
  return valueList


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  isPal = True
  s = s.lower().replace(" ","")
  for i in range (0,int(len(s)/2)):
    if s[i] != s[-i-1]:
      isPal = False
      break
  return isPal
