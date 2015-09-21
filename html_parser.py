'''
STEVE.KUO 9/10/15
for python 2.7
'''

#1. This is a *test*. This is a <b>test</b>.
#2. This is a \*test\*. => This is a *test*.

def stringConvertor (inputString):
   openBold = True
   encounteredEscape = False
   stringBuilder = ''
   
   for index in range(0, len(inputString)):
      currentChar = inputString[index]
      if encounteredEscape == True: #escape was previously encountered
         stringBuilder += currentChar
         encounteredEscape = False
      elif currentChar == '\\': #new escape encountered
         encounteredEscape = True
      elif currentChar != '*':
         stringBuilder += currentChar
      elif currentChar == '*':
         if openBold:
            stringBuilder += '<b>' #open bold
            openBold = False
         else:
            stringBuilder += '</b>' #close bold
            openBold = True
   return stringBuilder

print stringConvertor('hello')
print stringConvertor('This is a *test*.')
print stringConvertor('This is a \*test\*.')
print stringConvertor('\\\\\\')
print stringConvertor('***')