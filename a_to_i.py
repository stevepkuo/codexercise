'''
STEVE.KUO 8/31/15
for python 2.7
'''

#BACKGROUND #BACKGROUND #BACKGROUND #BACKGROUND #BACKGROUND #BACKGROUND
#input '1234' => 1234 is a clue that the function does something like 1000*1+100*2+10*3+1*4
#Where each Ascii digit is converted to Ascii table index and offset by a negative value
#such that '0', '1', '2' which are Ascii table index numbers 48,49,50 are offset to 0,1,2
#and then multiplied by a factor of 10 and then all added together
#The rightmost Ascii digit is multiplied by 1
#The 2nd Ascii digit from the right is multiplied by 10
#The 3rd Ascii digit from the right is multiplied by 100
#and so on....
#BACKGROUND #BACKGROUND #BACKGROUND #BACKGROUND #BACKGROUND #BACKGROUND

#ASSUMPTIONS #ASSUMPTIONS #ASSUMPTIONS #ASSUMPTIONS #ASSUMPTIONS #ASSUMPTIONS
#I'm assuming that while '1234' will return 1234, -1234 will return a different number because '-' is an Ascii itself
#even a space ' ' is an Ascii so I'm assuming that '-' and ' ' should be taken literally for its corresponding Ascii index
#I'm assuming that even leading spaces and trailing spaces should not be ignored because they are all Ascii characters
#I also assume that the input can come from extended ascii table which has extra characters in ascii index 128-255
#ASSUMPTIONS #ASSUMPTIONS #ASSUMPTIONS #ASSUMPTIONS #ASSUMPTIONS #ASSUMPTIONS

#atoi takes Ascii string input and returns integer representation that can either be positive, 0, or negative
#This atoi function seems similar to a hash function although it can return negative numbers
#Input: Ascii string like 'char123' or 'abcedfg' or '1234'
#Output: Integer version of the string; '1234' is straightforward and should become the number 1234
def atoi (askyString):
   #ERROR CHECK FOR BLANK STRING
   if len(askyString) == 0:
      errormessage = 'error: inputstring is blank'
      raise ValueError(errormessage)

   #initialize final value to return
   finalNum = 0

   #this FOR loop will step index backwards from last index in the string towards 0
   for index in range(0,len(askyString)):
      #get the Ascii char/digit
      askyChar = askyString[index]

      #try to get the Ascii version of the character
      #ord is a built-in python function to return Ascii table index value of a character
      #need to subtract 48 so that '0', '1', '2' which are Ascii table numbers 48,49,50 are offset to 0,1,2
      try:
         askyValue = ord(askyChar)
      except:
         errormessage = 'error: character could not be translated to number' + str(askyChar)
         raise ValueError(errormessage)
      #ADDITIONAL ERROR CHECKING HERE
      if askyValue < 0 or askyValue > 255:
         errormessage = 'error: character is not Ascii' + str(askyChar)
         raise ValueError(errormessage)
      #ADDITIONAL ERROR CHECKING ABOVE
      
      askyValue -= ord('0') #offset by subtracting by 48
      #update final value with result of current Ascii char/digit
      finalNum = finalNum*10 + askyValue
   return finalNum

#function to help test atoi function
def atoi_tester (askyString):
   try:
      result = atoi(askyString)
   except ValueError as err:
      print(str(err.args))
   except:
      print 'something other than ValueError went wrong'
   else:
      print str(result)

def main():
   #TEST CASES
   #invalid inputs
   atoi_tester(unichr(1000)) #unicode character of index 1000 that is not an Ascii character => error
   atoi_tester('') #blank string should return => error
   atoi_tester(' ') #make sure space is recognized as valid input
   atoi_tester('  ') #and multiple spaces as well

   #testing the legal bounds within Ascii
   atoi_tester(chr(0)) #NULL ascii character which is lowest index 0 of Ascii table; This should be -48 due to internal offset
   atoi_tester('/') # this should be -1
   atoi_tester('0') #this should be 0
   atoi_tester('0000000000000000000000000000000') #this should also be 0
   atoi_tester('1') #this should be 1
   atoi_tester(chr(254)) #ascii character which is 2nd highest index 254 of Ascii table => 206
   atoi_tester(chr(255)) #ascii character which is highest index 255 of Ascii table => 207

   #all integers
   atoi_tester('1') #one integer digit should return the same integer 1
   atoi_tester('1234567')#many integer digits should return the same integer 1234567
   #negative integer
   atoi_tester('-1')#should return different integer -29
   atoi_tester('-1234567')#many integer digits should return different integer -28765433

   #all letters
   atoi_tester('a') #one letter
   atoi_tester('abcdefg')# many letters

   #mix of integers and letters
   atoi_tester('1a2b3c4d')

   #testing the output capability of the function
   atoi_tester('/////////////////////////////////') #this should be a huge negative number
   atoi_tester('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') #this should be a huge positive number

if __name__ == "__main__":
    main()