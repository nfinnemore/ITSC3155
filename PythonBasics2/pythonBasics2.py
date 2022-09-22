# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

from asyncio.windows_events import NULL


def count_threes(n):
  multiples = 0
  if n % 3 == 0:
    for i in range(0,n,3):
      multiples += 1
  return multiples


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(stringS):
  longestChar = stringS[0]
  longest = 0
  for i in range (0,len(stringS)):
    count = 0
    for j in range(i+1,len(stringS)):
      if (stringS[i] == stringS[j]):
        count += 1
      else:
        break
    if count > longest:
      count = longest
      longestChar = stringS[i]
  return longestChar


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE

  return
