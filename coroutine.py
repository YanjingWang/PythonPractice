# https://www.geeksforgeeks.org/coroutine-in-python/

# Python3 program for demonstrating
# coroutine execution
"""
The execution of the coroutine is similar to the generator. When we call coroutine nothing happens, it runs only in response to the next() and sends () method. 
This can be seen clearly in the above example, as only after calling __next__() method, our coroutine starts executing. 
After this call, execution advances to the first yield expression, now execution pauses and waits for the value to be sent to corou object. 
When the first value is sent to it, it checks for prefix and print name if prefix present. 
After printing the name, it goes through the loop until it encounters the name = (yield) expression again. 
"""


def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)


# calling coroutine, nothing will happen
corou = print_name("Dear")

# This will start execution of coroutine and
# Prints first line "Searching prefix..."
# and advance execution to the first yield expression
corou.__next__()

# sending inputs
corou.send("Atul")
corou.send("Dear Atul")

"""
Closing a Coroutine

Coroutine might run indefinitely, to close coroutine close() method is used. When a coroutine is closed it generates GeneratorExit exception which can be caught in the except usual way. 
After closing the coroutine, if we try to send values, it will raise the StopIteration exception. Following is a simple example : 
"""
# Python3 program for demonstrating
# closing a coroutine


def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")


corou = print_name("Dear")
corou.__next__()
corou.send("Atul")
corou.send("Dear Atul")
corou.close()

"""
Chaining coroutines for creating pipeline

Coroutines can be used to set pipes. We can chain together coroutines and push data through the pipe using send() method. A pipe needs :  

An initial source(producer) derives the whole pipeline. The producer is usually not a coroutine, it’s just a simple method.
A sink, which is the endpoint of the pipe. A sink might collect all data and display it.
"""
# Python3 program for demonstrating
# coroutine chaining


def producer(sentence, next_coroutine):
    '''
    Producer which just split strings and
    feed it to pattern_filter coroutine
    '''
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    '''
    Search for pattern in received token
    and if pattern got matched, send it to
    print_token() coroutine for printing
    '''
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering!!")


def print_token():
    '''
    Act as a sink, simply print the
    received tokens
    '''
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine=pt)
pf.__next__()

sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)
