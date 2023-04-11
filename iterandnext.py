# Python code demonstrating
# basic use of iter()
listA = ['a', 'e', 'i', 'o', 'u']

iter_listA = iter(listA)

try:
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))  # StopIteration error
except:
    pass


# Python code demonstrating
# basic use of iter()
lst = [11, 22, 33, 44, 55]

iter_lst = iter(lst)
while True:
    try:
        print(iter_lst.__next__())
    except:
        break


# Python code demonstrating
# basic use of iter()

listB = ['Cat', 'Bat', 'Sat', 'Mat']


iter_listB = listB.__iter__()

try:
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())  # StopIteration error
except:
    print(" \nThrowing 'StopIterationError'",
          "I cannot count more.")


# Python code showing use of iter() using OOPs

class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1


# Driver code
if __name__ == '__main__':

    a, b = 2, 5

    c1 = Counter(a, b)
    c2 = Counter(a, b)

    # Way 1-to print the range without iter()
    print("Print the range without iter()")

    for i in c1:
        print("Eating more Pizzas, counting ", i, end="\n")

    print("\nPrint the range using iter()\n")

    # Way 2- using iter()
    obj = iter(c2)
    try:
        while True:  # Print till error raised
            print("Eating more Pizzas, counting ", next(obj))
    except:
        # when StopIteration raised, Print custom message
        print("\nDead on overfood, GAME OVER")
