class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkListClass:
	
	def __init__(self):
		self.head = None

	def addNode_at_Beg(self,  value):
		node_obj = Node(value)
		node_obj.next =  self.head
		self.head = node_obj

	def addNode_at_End(self,  value):
		node_obj = Node(value)
		current  = self.head
		while current.next:
			current  = current.next

		current.next   =  node_obj

	def printLinkList(self):
		current = self.head

		while current:
			print (current.data)
			current = current.next

if __name__ == '__main__':
	linklist = LinkListClass()
	import ipdb;ipdb.set_trace()