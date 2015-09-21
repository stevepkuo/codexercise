#merge sort;
#recursively divide an array in half into its smallest elements
#then put each pair together in order until the entire array is built

def mergesort (inputList):
   if len(inputList) == 0: #blank list
      return inputList
   elif len(inputList) == 1: #1 element list
      return inputList
   middle = (len(inputList)-1)/2
   lefthalf = inputList[0:middle+1]
   righthalf = inputList[middle+1:]
   lefthalf = mergesort(lefthalf)
   righthalf = mergesort(righthalf)
   finalList = combine(lefthalf, righthalf)

   return finalList

def combine (leftList, rightList):
   if len(leftList) == 0 and len(rightList) == 0:
      return []
   elif len(leftList) == 0:
      return rightList
   elif len(rightList) == 0:
      return leftList

   i = 0
   j = 0
   newList = []
   while (i < len(leftList)) and (j < len(rightList)):
      if leftList[i] < rightList[j]:
         newList.append(leftList[i])
         i += 1
      else:
         newList.append(rightList[j])
         j += 1
   while (i < len(leftList)):
      newList.append(leftList[i])
      i += 1
   while (j < len(rightList)):
      newList.append(rightList[j])
      j += 1
   return newList

#how test?
#BLACK BOX BOUNDARY CASES
#ILLEGAL: 'string'
#blank list: []
#1 element list: 2
#all same values: 3 3 3
#completely in order
#completely reverse order
#left half already sorted
#right helf already sorted

#WHITE BOX, KNOWLEDGE OF INTERNALS
#2 element list
   #=> 1, 4
   #=> 4, 1
#3 element list: left is 2 element; right is 1 element
   #Combine 2 element, and 1 element list together
   #1,2,     3 => will need to exercise the 3rd loop to deal with 1 remaining item in right list
   #1,3,     2 => will need to exercise the 2nd loop to deal with 1 remaining item in left list
   #2,1,     3 => will need to exercise the 3rd loop to deal with 1 remaining item in right list
   #2,3,     1 => will need to exercise the 2nd loop to deal with 1 remaining item in left list
   #3,1,     2 => will need to exercise the 2nd loop to deal with 1 remaining item in left list
   #3,2,     1 => will need to exercise the 2nd loop to deal with 1 remaining item in left list


list = [5,6,10,11,13,100]
print mergesort(list)
list = [100,10,9,8,7,6]
print mergesort(list)