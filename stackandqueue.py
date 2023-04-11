class MyQueue():
    def __init__(self):
        # before_head.next is the head of queue
        self.before_head = LinkedListNode(-1)  # create a dummy
        self.tail = self.before_head

        """
        @param: item an integer
        @return: nothing
        """

    def enqueue(self, item):
        # put all nodes at the end
        self.tail.next = LinkedListNode(item)
        # put end pointer backward
        self.tail = self.tail.next

        """
        @return: an integer
        """

    def dequeue(self):
        # if dequeue is empty, return -1
        if self.before_head.next is None:
            return -1

        # count the value of queue head
        head_val = self.beofre_head.next.val
        # put pointer backwards
        self.before_head = self.before_head.next

        return head_val



class LinkedListNode:
    def __init__(self, val):
        self.val = val
