# Given two strings, s and t, return true if t is an anagram of s

s = "bart"
t = "brat"

def check_anagram(string1, string2):
  if len(s) == len(t):
    for i in range(len(string1)):

      counter = 0

      for j in range(len(string2)):

        if string1[i] == string2[j]:

          counter += 1

          if counter == 2:
            return print("t is not an anagram of s, repeated letters")

      if counter == 0:
        return print("t is not an anagram of s, missing or incorrect letters")

    return print("t is an anagram of s")
  else:
    return print("s and t are not the same size")

check_anagram(s, t)
