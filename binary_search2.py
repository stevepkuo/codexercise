import string
import os


def binary_search(low, high, numlist, searchfor):
   midway = (low + high)/2
   if low == high: #search in single item
      if numlist[low] == searchfor: return low
      else: return -1
   elif (high-low) ==1:
      if numlist[low] == searchfor: return low
      elif numlist[low] > searchfor: return -1
      else: return binary_search(high, high, numlist, searchfor)
   else: # searching within more than 2 elements
      if numlist[midway] == searchfor: return midway
      elif numlist[midway] < searchfor: return binary_search(midway+1, high, numlist, searchfor)
      else: return binary_search(low, midway-1, numlist, searchfor)

numlist = [1,2,3,4,5,6,7,8,9]
print binary_search(0, len(numlist)-1, numlist, 1)
print binary_search(0, len(numlist)-1, numlist, 9)
numlist = [1]
print binary_search(0, len(numlist)-1, numlist, 1)
print binary_search(0, len(numlist)-1, numlist, 0)
numlist = [1,2,3]
print binary_search(0, len(numlist)-1, numlist, 1)
print binary_search(0, len(numlist)-1, numlist, 0)
print binary_search(0, len(numlist)-1, numlist, 3)