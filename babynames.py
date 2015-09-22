'''
STEVE.KUO 9/21/15
for python 2.7
'''

class Graph(object):
   def __init__ (self):
      self.nodes = {}
class Node(object):
   def __init__ (self, name):
      self.name = name
      self.children = []

#start from name; traverse to its children; add it's childrens values
def traverseNode(name, nameGraph, seenNames, dictNames):
   if name in seenNames: return 0
   seenNames.append(name)
   if not(name in dictNames):
      tempTotal = 0
   else:
      tempTotal = dictNames[name]
   if not (name in nameGraph.nodes):
      return tempTotal
   for kidNode in nameGraph.nodes[name].children:
      if not(kidNode.name in seenNames):
         tempTotal += traverseNode (kidNode.name, nameGraph, seenNames, dictNames)
   return tempTotal

def babyNames (dictNames, synonyms):
   nameGraph = Graph()
   outputDict = {}
   seenNames = []
   for leftname, rightname in synonyms:
      if not(leftname in nameGraph.nodes):
         nameGraph.nodes[leftname] = Node(leftname)
      if not(rightname in nameGraph.nodes):
         nameGraph.nodes[rightname] = Node(rightname)
      nameGraph.nodes[leftname].children.append(nameGraph.nodes[rightname])
      nameGraph.nodes[rightname].children.append(nameGraph.nodes[leftname])
   for keyName, value in dictNames.iteritems():
      if keyName in seenNames:
         continue
      else:
         outputDict[keyName] = traverseNode(keyName, nameGraph, seenNames, dictNames)
   return outputDict

dictNames = {}
dictNames['John'] = 15
dictNames['Jon'] = 12
dictNames['Chris'] = 13
dictNames['Kris'] = 4
dictNames['Christopher'] = 19
synonyms = [('Jon', 'John'),('John', 'Johnny'),('Chris', 'Kris'),('Chris', 'Christopher')]
print babyNames(dictNames, synonyms)