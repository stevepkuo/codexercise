'''
STEVE.KUO 9/17/15
for python 2.7
'''

def count2s (inputNum):
   howMany2s = 0
   for index in range (0, inputNum+1):
      if howMany2sInNum(index) > 0: print index
      howMany2s += howMany2sInNum(index)
   return howMany2s

def howMany2sInNum(inputNum):
   tempNum = inputNum
   tempCount = 0
   while (tempNum > 0):
      if (tempNum%10) == 2: tempCount += 1
      tempNum = tempNum / 10
   return tempCount
   
print count2s(10)
print count2s(143)
#print count2s(1000)
#print count2s(1000000)