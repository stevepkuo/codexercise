#merge sort;
#recursively divide an array in half into its smallest elements
#then put each pair together in order until the entire array is built

def mergesort (inputList, min, max):
   if (max-min) <= 0: #blank list or 1 element list
      return
   middle = (max+min)/2
   print str(min) + ' ' + str(middle) + ' ' + str(max)
   mergesort(inputList, min, middle)
   mergesort(inputList, middle+1, max)
   combine(inputList, min, middle, max)

def combine (inputList, min, middle, max):
   if (middle-min) < 0 or (max-middle) < 0:
      return
   if (max-min) <= 0:
      return

   i = min
   j = middle+1
   k = 0
   tempList = [0]*(max-min+1)
   while (i < (middle+1)) and (j < (max+1)):
      if inputList[i] < inputList[j]:
         tempList[k]=inputList[i]
         i += 1
         k += 1
      else:
         tempList[k]=inputList[j]
         j += 1
         k += 1
   while (i < (middle+1)):
      tempList[k] = inputList[i]
      i += 1
      k += 1
   while (j < (max+1)):
      tempList[k] = inputList[j]
      j += 1
      k += 1
   for tempIndex in range(0, max-min+1):
      inputList[tempIndex+min] = tempList[tempIndex]
   return

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
   ##2,1,     3 => will need to exercise the 3rd loop to deal with 1 remaining item in right list
   #2,3,     1 => will need to exercise the 2nd loop to deal with 2 remaining item in left list
   ##3,1,     2 => will need to exercise the 2nd loop to deal with 1 remaining item in left list
   ##3,2,     1 => will need to exercise the 2nd loop to deal with 1 remaining item in left list

list = []
mergesort(list, 0, len(list)-1)
print(list)
list = [5,6,10,11,13,100]
mergesort(list, 0, len(list)-1)
print(list)
list = [100,10,9,8,7,6]
mergesort(list, 0, len(list)-1)
print(list)