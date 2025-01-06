def alternateCharacter(string):
  """
  Converts the given string to alternate case, 
  where every other character is uppercase.

  Args:
    string: The input string.

  Returns:
    The string with alternate case.
  """
  result = "" 
  for i, character in enumerate(string):  # Enumerate provides both index and character
    if i % 2 == 0:                        # Check if the index is even
      result += character.upper()         # Convert to uppercase
    else:
      result += character.lower()         # Convert to lowercase
  return result

def alternateWord(string):
  """
  Converts the given string to alternate word case, 
  where every other word is uppercase.

  Args:
    string: The input string.

  Returns:
    The string with alternate word case.
  """
  words = string.split()               # Split the string into a list of words
  result = []
  for i, word in enumerate(words):     # Enumerate provides both index and word
    if i % 2 == 0:                     # Check if the index is even
      result.append(word.lower())      # Convert to lowercase
    else:
      result.append(word.upper())      # Convert to uppercase
  return " ".join(result)              # Join the list of words back into a string

string = "I am enjoying the Data Science bootcamp"

print(alternateCharacter(string)) 
print(alternateWord(string))