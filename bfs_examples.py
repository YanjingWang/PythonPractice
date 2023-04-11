from queue import Queue


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    def build_tree(self):
        node_1 = TreeNode(1)
        node_2 = TreeNode(2)
        node_3 = TreeNode(3)

        node_1.left = node_2
        node_1.right = node_3

        return node_1

    def bfs_levelOrderBottom(self, root):
        res = []
        if not root:
            return

        que = Queue(maxsize=0)  # maxsize = 0 means queue is infinately large
        que.put(root)

        while not que.empty():
            n = que.qsize()
            temp = []
            for i in range(n):  # range is an iterator storing objects
                cur = que.get()
                temp.append(cur.val)
                # print(cur.val, end=' ')
                if cur.left:
                    que.put(cur.left)
                if cur.right:
                    que.put(cur.right)
            # print()  # change level
            res.append(temp)
        return print(list(reversed(res)))  # reversed() returns an interator instead of list

    def zigzagLevelOrder(self, root):
        lists = []
        # exception
        if not root:
            return lists

        # use two stack, store nodes
        stack = []
        next_stack = []

        stack.append(root)
        # current level nodes storing order
        left_to_right = True
        # bfs
        while len(stack) != 0:
            # current level nodes
            nodes = []
            # get out all nodes of current level, and expand next level and store nodes in next_stack
            while len(stack) != 0:
                # pop a node
                curr_node = stack.pop()
                if curr_node is None:
                    continue
                # if not None, expand left and right two sub nodes
                nodes.append(curr_node.val)
                # current level interation direction
                if left_to_right:
                    next_stack.append(curr_node.left)
                    next_stack.append(curr_node.right)
                else:
                    next_stack.append(curr_node.right)
                    next_stack.append(curr_node.left)
            # reverse direction
            left_to_right = not left_to_right
            # if nodes is not empty
            if len(nodes) > 0:
                lists.append(nodes)
            # stack interation
            stack = next_stack
            next_stack = []
        return print(lists)

    def add_to_lists(self, lists, curr_level, value):
        # if curr is not in level
        if curr_level == len(lists):
            lists.append([])
        # save answer
        lists[curr_level].append(value)

    def dfs(self, node, lists):
        # recursion exit
        if node is None:
            # return - to make father node 's level 0
            return -1
        # recursion split
        left_level = self.dfs(node.left, lists)
        right_level = self.dfs(node.right, lists)

        curr_level = max(left_level, right_level) + 1
        self.add_to_lists(lists, curr_level, node.val)
        return curr_level

    def findLeaves(self, root):
        lists = []
        # exception
        if root is None:
            return lists
        self.dfs(root, lists)
        return print(lists)


# input1 = TreeNode({1,2,3})
# input1.bfs_levelOrderBottom({1})
# input1 = TreeNode({1, 2, 3})
input1 = TreeNode({1, 2, 3})
root = input1.build_tree()
# input1.bfs_levelOrderBottom(root)
# input1.zigzagLevelOrder(root)  # [[1],[2, 3]]
input1.findLeaves(root)
