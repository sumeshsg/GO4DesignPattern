class Node(object):

    def __init__(self, name):
        self.children = []
        self.sName = name

    def __repr__(self):
        return "<Node '{}'>".format(self.sName)

    def append(self, *args, **kwargs):
        self.children.append(*args, **kwargs)

    def traverses_tree_depth(self):
        print(self)
        for oChild in self.children:
            oChild.traverses_tree_depth()

    def traverses_tree_width(self):
        def gen(o):
            all_node = [o, ]
            while all_node:
                next_node = all_node.pop(0)
                all_node.extend(next_node.children)
                yield next_node

        for node in gen(self):
            print(node)

    def traverses_tree_width_my_version(self):
        all_node = [self]
        for node in all_node:
            all_node.extend(node.children)
            print(node)


if __name__ == '__main__':
    oRoot = Node("root")
    oChild1 = Node("child1")
    oChild2 = Node("child2")
    oChild3 = Node("child3")
    oChild4 = Node("child4")
    oChild5 = Node("child5")
    oChild6 = Node("child6")
    oChild7 = Node("child7")
    oChild8 = Node("child8")
    oChild9 = Node("child9")
    oChild10 = Node("child10")

    oRoot.append(oChild1)
    oRoot.append(oChild2)
    oRoot.append(oChild3)
    oChild1.append(oChild4)
    oChild1.append(oChild5)
    oChild2.append(oChild6)
    oChild3.append(oChild7)
    oChild3.append(oChild8)
    oChild4.append(oChild9)
    oChild6.append(oChild10)

    # oRoot.traverses_tree_depth()
    # oRoot.traverses_tree_width()
    oRoot.traverses_tree_width_my_version()
