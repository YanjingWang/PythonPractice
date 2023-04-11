from myLinkedList import ListNode
from queue import Queue


class MyQueue():
    def __init__(self):
        self.count = 0  # how many values now
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        if self.head is None:
            raise Exception('this is an empty queue')
        cur = self.head
        self.head = cur.next
        self.count -= 1
        return cur.val

    def is_empty(self):
        return self.head is None  # self.count == 0

    def size(self):
        return self.count


if __name__ == '__main__':
    # my_queue = MyQueue()
    # for i in range(50):
    #     my_queue.enqueue(i)
    #
    # while not my_queue.is_empty():
    #     print(my_queue.dequeue(),end = ' ')

    que = Queue()
    for i in range(50):
        que.put(i)

    while not que.empty():
        print(que.get(), end=' ')
    print()
    print(que.qsize())

