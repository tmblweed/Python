
class Node:
    def __init__(self,key):
        self.key =key
        self.children = []

    def _find_child_by_key(self,key):
        for child in self.children:
            if child.key == key:
                return child
        return None  #no node, i.e a key was found with the given value


    def _add_child(self,key):
        child = Node(key)
        self.children.append(child)
        return child


    def insertChild(self,words):
        if len(words)==0:
            return

        first_item = words[0]
#the following three lines will create a node key if it doesnt exist and if does exist, get the key in it
        found_child = self._find_child_by_key(first_item)
        if found_child == None:
            found_child = self._add_child(first_item)

        found_child.insertChild(words[1:])


    def printNode(self,depth=0):
        print " "*depth + self.key 
        for child in self.children:
            child.printNode(depth+3)



my_node = Node('')

# my_node.insertChild(['user','friends','lists'])
# my_node.insertChild(['user1','friends1','lists1'])

my_node.insertChild(['user'])
my_node.insertChild(['friends'])
my_node.insertChild(['list1'])

my_node.insertChild(['user','blah'])

my_node.printNode()
