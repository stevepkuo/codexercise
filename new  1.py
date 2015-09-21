#'Barclay Oudersluys is nearly three-quarters of the way through Forrest Gump's \n
#cross-country run from the Santa Monica Pier in California, to the lighthouse in \n
#Rockland, Maine. Oudersluys admits the Tom Hanks movie is a favorite, but his goal \n
#is to raise enough money for the Hall Steps Foundation to build a well in Mozambique.'


paragraph = /|\

start_index = 0
current_endline = paragraph.find('\n', beg = start_index)
if current_endline == -1:
   current_endline = len(paragraph)
#start of paragraph => first occurance of '\n'
current_line = paragraph[start_index:current_endline]
while(current_line != ''):
   

   do something with the current_line


   if current_endline == len(paragraph)-1:
      break
	start_index = current_endline+1
   current_endline = paragraph.find('\n', beg = start_index)
   if current_endline == -1:
      current_endline = len(paragraph)
   current_line = paragraph[start_index:current_endline]
   
   
#########################################################

with open ('c:\downloads\file.txt') as f:
   for line in f:
      do something with line
#########################################################


paragraph = /|\
alternate_paragraph = ''
for counter in range(0,len(paragraph)):
   if paragraph[counter] == ' ':
       continue
   alternate_paragraph = alternate_paragraph + paragraph[counter]
paragraph = alternate_paragraph
       
#########################################################

#Given a paragraph of text, write a program to find the first shortest sub-segment that contains each of the
#given k words at least once. A segment is said to be shorter than other if it contains less number of words

