def BinaryTree(root_value):
	""" Binary 
	"""
	return [root_value, [], []]

def insertLeft(root,newNode):
    
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newNode,t,[]])
    else:
        root.insert(1, [newNode, [], []])
    return root

def insertRight(root,newNode):
    
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newNode,[],t])
    else:
        root.insert(2, [newNode,[],[]])
    return root

def setRoot(root, value):	
	root[0] = value
	return root

def getLeftvalue(root):
	""" getLeftvalue 
	"""
	return root[1]

def getRightvalue(root):
	""" getRightvalue
	"""
	return root[2]


if __name__ == '__main__':
	import ipdb; ipdb.set_trace()
	print ("<<<<<  ---  Tree DataStructure  --->>>>>>")
















