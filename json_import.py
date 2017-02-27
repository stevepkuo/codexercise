'''
STEVE.KUO 10/6/15
for python 2.7
'''

import json

json_string = '{"firstname":"Earl", "lastname":"Duke"}'
decodeddict = json.loads(json_string)

#pretty printing
print json.dumps(decodeddict, sort_keys=True, indent=4)

#accessing the json object's elements
print decodeddict['firstname']
print decodeddict['lastname']


#with open('data.json') as data_file:    
#  decodeddict = json.load(data_file)

#with open(file, 'r') as textfile:
#  for currentline in textfile: #go through each line in the file

#with open(descriptorTranslationFile, 'rb') as csvfile:
#   reader = csv.reader(csvfile)
#      for row in reader:



#with open('textfile.txt', 'a') as rawlog:
#   rawlog.write(str(item))