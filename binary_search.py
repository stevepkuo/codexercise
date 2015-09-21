import string
import os
#pagelist = [1,0]
pagelist = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0]


def binary_search(pagelist):
   beginning_index = 0
   end_index = len(pagelist)-1#=14
   midpoint = (end_index+beginning_index)/2 # rounds down to nearest integer => midpoint = 7

   #check the midpoint

   while(beginning_index < end_index):
      if (pagelist[midpoint] == 1): #we have hit a 1; search to the right of the midpoint = 7
         beginning_index = midpoint
         #end_index = end_index
         midpoint = (end_index+beginning_index)/2
      else: #we did not hit a 1; search to the left of the midpoint
         #beginning_index = beginning_index
         end_index = midpoint-1
         midpoint = (end_index+beginning_index)/2
      print 'beginning, mid, end  = ' + str( beginning_index) + ' ' + str(midpoint) + ' ' + str(end_index)
   #                                          10                          10                    11
      if beginning_index == (end_index-1):
         if pagelist[end_index] == 1:
            beginning_index = beginning_index + 1
            midpoint = (end_index+beginning_index)/2
         else:
            end_index = end_index -1
            midpoint = (end_index+beginning_index)/2
         break

   if pagelist[midpoint] != 1:
      print 'last 1 not found because it is invalid'
   else:
      print 'location of last 1 is at ' + str(midpoint)

binary_search(pagelist)
'''
def binary_search(pagelist, globalbeginning):
   beginning_index = 0
   end_index = len(pagelist)-1#=14
   midpoint = (end_index+beginning_index)/2 # rounds down to nearest integer => midpoint = 7

   print 'beginning, mid, end  = ' + str( beginning_index) + ' ' + str(midpoint) + ' ' + str(end_index)
   if beginning_index == (end_index-1):
      if pagelist[end_index] == 1:
         beginning_index = beginning_index + 1
         midpoint = (end_index+beginning_index)/2
      else:
         end_index = end_index -1
         midpoint = (end_index+beginning_index)/2
      return globalbeginning+midpoint

   if (pagelist[midpoint] == 1): #we have hit a 1; search to the right of the midpoint = 7
      beginning_index = midpoint
      #end_index = end_index
      return binary_search(pagelist[beginning_index:end_index+1], globalbeginning+beginning_index)
   else: #we did not hit a 1; search to the left of the midpoint
      #beginning_index = beginning_index
      end_index = midpoint-1
      return binary_search(pagelist[beginning_index:end_index+1], globalbeginning+beginning_index)

print str(binary_search(pagelist,0))
'''