from tree import Node  # Imports the Node object used to construct trees
# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = Node(8,     # root
             Node(2,    # left child of root 
                  Node(1),      # left child
                  Node(5)),     # right leaf
             Node(10))  # right child of root  
tree2 = Node(7,     # root 
             Node(2,    # left child of root 
                  Node(1),  # left leaf 
                  Node(5,       # right child
                       Node(4),     # left child leaf
                       Node(6))),   #right child leaf
             Node(9,    # right child of root
                  Node(8),  # left leaf
                  Node(10)))# right leaf
tree3 = Node(5,     # root      
             Node(3,    # left child of root 
                  Node(2),  # left leaf
                  Node(4)), # right leaf
             Node(14,   # right child of root
                  Node(12),     # left leaf
                  Node(21,      # right child  
                       Node(19),    # left child leaf 
                       Node(26))))  # right child leaf

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # intialization section
    right_max = 0
    left_max = 0
    
    # base case
    # checks if tree is just the leaf
    if tree.get_left_child() == None and tree.get_right_child() == None:
        #print("this is the base case")
        return 0    # returns a height of 0
    
    # checks for a left child
    if tree.get_left_child() != None:
        #print("I'm the left child")
        #print(tree.get_left_child())
        
        # recursive call to only look at left child
        left_max = find_tree_height(tree.get_left_child())  # finds max height of left tree with recursion
    
    # checks for a right child
    if tree.get_right_child() != None:
        #print("I'm the right child")
        #print(tree.get_right_child())
        
        # recursive call to only look at right child
        right_max = find_tree_height(tree.get_right_child())    # finds max height of right tree with recursion
    
    # returns the max of the right and left trees and increments by one to include height of the parent
    return 1 + max(left_max, right_max)
        
def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. compare_func(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 compare_func(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # initialization section
    left_tree = True
    right_tree = True
    #print(f"this is the tree: {tree}")    
    #print("this is tree")
    #print(tree)
    
    # checks to see if there is no tree
    if tree == None:
        return True     # Base case and defaults to True, nothing to compare so must be true
    
    parent_value = tree.get_value() # gets the parent value
    
    # checks for a left child, then finds value
    if type(tree.get_left_child()) != None:
        #print("this is left child:")
        #print(tree.get_left_child())
        child = tree.get_left_child()    # gets left child
        # checks to make sure left child has a value
        # checks to see if comparison function is true
        if child == None or compare_func(child.get_value() , parent_value) == True:
            # recursive call to make sure left tree is true for every comparison
            left_tree = is_heap(tree.get_left_child(), compare_func)
        
        # comparison function is false for any parent and child pairing then return false
        else:
            return False
            
    # checks for a right child, then finds value
    if type(tree.get_right_child()) != None:
        child = tree.get_right_child()   # gets  right child  
        # checks to make sure right child has a value
        # checks to see if comparison function returns False
        if child == None or compare_func(child.get_value(), parent_value) ==  True:
            # recursive call to make sure right tree is true for every comparison
            right_tree = is_heap(tree.get_right_child(), compare_func)
        # comparison funtion is false for any parent and child pairing then return false
        else:
            return False
    
    # compares the left and right trees to make sure comparison is true for entire tree
    return left_tree and right_tree 
        
        
    #return is_heap(c, compare_func) and is_heap(tree, compare_func)

if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    #pass
    print(find_tree_height(tree2))
