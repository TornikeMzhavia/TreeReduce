import os

class Node():
    '''
    Node class for holding node identifier, data and children objects
    '''

    def __init__(self, id, data_list):
        self.id = id
        self.data = set(data_list)
        self.children = []

    def __repre__(self):
        return self.id

class Tree_Reducer():
    '''
    Tree simplifier class for building the tree from the source and simplifying it
    '''

    def __init__(self, data_source, output_directory):
        '''
        Initilize the object
        '''
        self.data_source = data_source
        self.output_directory = output_directory


    def run(self):
        '''
        Run the builder and simplifer methods
        '''

        self.__build_tree()
        self.__reduce_tree()

    
    def __build_tree(self):
        tree_map = {}
        self.head_node = None
    
        # read data O(n)
        for url, data in self.data_source:
            tree_map[url] = Node(url, set(data))

        # build tree O(n)
        for node in tree_map.values():            
            parent = self.__find_parent(node.id, tree_map)

            # if parent was found then the node is appended to it
            # if not then this node is the head of the tree
            if parent:
                parent.children.append(node)
            else:
                self.head_node = node

        return self.head_node


    def __reduce_tree(self):
        # open the utput stream and run the simplification recursion
        with open(self.output_directory, 'w') as output_file:
            self.__traverse_recursive(self.head_node, set(), output_file)


    def __traverse_recursive(self, node, parent_set, output_stream):
        # remove duplicate technologies with set difference
        node.data = node.data - parent_set

        # if node still has uniwue technologies than print the 
        if node.data:
            output_stream.write('{}\t -> {}\n'.format(node.id, ', '.join(sorted(node.data))))

        # traverse children nodes recursively
        for child in node.children:
            self.__traverse_recursive(child, node.data.union(parent_set), output_stream)


    def __find_parent(self, node_id, tree_map):
        id_elements = node_id.split('/')

        # look for parent directory
        for i in range(1, len(id_elements)):
            parent = tree_map.get('/'.join(id_elements[:-i]))
            if parent:
                return parent

        return None
