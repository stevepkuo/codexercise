class TreeNode (object):
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.parent = None

def createBinary(inputList):
   if len(inputList) == 0: return None
   if len(inputList) == 1: return TreeNode(inputList[0])
   median = (len(inputList)-1)/2
   value = inputList[median]
   newNode = TreeNode(value)
   newNode.left = createBinary(inputList[0:median])
   if newNode.left != None: newNode.left.parent = newNode
   newNode.right = createBinary(inputList[median+1:])
   if newNode.right != None: newNode.right.parent = newNode
   return newNode

hitOriginal = False

def findNextRec(rootNode, origNode):
   global hitOriginal
   print rootNode.value
   result = None
   if rootNode == None:
      return None
   if rootNode.left != None:
      result = findNextRec(rootNode.left, origNode)
      if result != None: return result
   if hitOriginal: return rootNode
   elif rootNode is origNode: hitOriginal = True
   if rootNode.right != None:
      result = findNextRec(rootNode.right, origNode)
   return result

def findNext(startNode):
   global hitOriginal
   if startNode == None: return None
   tempNode = startNode
   while(tempNode.parent != None):
      tempNode = tempNode.parent
   print 'parent node is found to be ' + str(tempNode.value)
   hitOriginal = False
   resultNode = findNextRec(tempNode, startNode)
   print 'hitOriginal is now ' + str(hitOriginal)
   return resultNode

topTreeNode = createBinary([1,2,3,4,5,6,7,8,9,10])
startingNode = topTreeNode.right.right.right
print 'starting node is ' + str(startingNode.value)
result = findNext(startingNode)
print result.value