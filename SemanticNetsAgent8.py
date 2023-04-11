from queue import Queue
import copy
from collections import deque
class Node:
    def __init__(self,leftsheeps, rightsheeps, leftwolves, rightwolves,move_direction, movements):
        # Current number of sheeps and wolves
        self.leftsheeps = leftsheeps
        self.rightsheeps = rightsheeps
        self.leftwolves = leftwolves
        self.rightwolves = rightwolves
        self.move_direction = move_direction
        # Movements required to get to this state from initial
        self.movements = movements
        self.prestate = None

    # def finalState(self):
    #     if self.leftsheeps == 0 and self.leftwolves == 0 and self.move_directions == 'right':
    #             return True
    #     else:
    #         False
    def __eq__(self, other):
        # Check if its a State object
        if isinstance(other, Node):
            return (self.leftsheeps == other.leftsheeps and self.rightsheeps == other.rightsheeps
                    and self.leftwolves == other.leftwolves and self.rightwolves == other.rightwolves
                    and self.move_direction == other.move_direction )
class SemanticNetsAgent:
    def __init__(self):
        self.possibleMoves = ((1, 1), (1, 0), (0, 2), (0, 1), (2, 0),(0, 1),(0, 2),(0, 1),(0, 2))
        pass
    def nextNode (self,curr, move_direction , leftsheeps, rightsheeps, leftwolves, rightwolves, movements):
        # finalState = Node(0, initial_sheep, 0, initial_wolves, "left", [])
        # initialState = Node(initial_sheep, 0, initial_wolves, 0, "right", [])
        movements.append(curr)

        # print(curr)
        if move_direction  == "left":
            nextState = Node(leftsheeps + curr[0], rightsheeps - curr[0],
                             leftwolves + curr[1], rightwolves - curr[1], "right",movements)
            # if self.ValidState(nextState, unProductives):
            #     unProductives.append(nextState)
            #     statesQueue.put(nextState)
            #     # If result found, break loop and return movements
            #     if nextState == finalState:
            #         # print("found result")
            #         return nextState.movements
        else:
            nextState = Node(leftsheeps - curr[0], rightsheeps + curr[0],
                             leftwolves - curr[1], rightwolves + curr[1],"left", movements)
            # if self.ValidState(nextState, unProductives):
            #     unProductives.append(nextState)
            #     statesQueue.put(nextState)
            #     # If result found, break loop and return movements
            #     if nextState == finalState:
            #         # print("found result")
            #         return nextState.movements

        return nextState
    # This method return boolean , true in it's a valid state : number of sheeps vs wolves
    # are correct and it's not a previous state
    def ValidState(self, prestate, unProductives):
        # Illegal state : Negative number of sheeps or wolves
        if prestate.leftsheeps < 0 or prestate.rightsheeps < 0 or prestate.leftwolves < 0 or prestate.rightwolves < 0:
            return False
        # Illegal state : wolves outnumber sheeps on the left or wolves outnumber sheeps on the right side
        if prestate.leftwolves > prestate.leftsheeps > 0 or prestate.rightwolves > prestate.rightsheeps > 0:
            return False
        # unproductive state : current state is same to previous state
        for unProductive in unProductives:
            if unProductive == prestate:
                return False

        return True
    # the following code is from: <https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/> [Breadth First Search or BFS for a Graph]
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    # end citation
    def solve(self, initial_sheep, initial_wolves):
        # Assuming the initial state is valid, build matrix for initial state
        # Initialize right side with 0 sheep and 0 wolves
        movements = []
        finalState = Node(0,initial_sheep,0,initial_wolves,"left",movements)
        initialState = Node(initial_sheep,0,initial_wolves,0,"right",movements)
        statesQueue = Queue()
        pastResult = []
        unProductives = []
        unProductiveStates = []
        unProductiveStates.append([initial_sheep,0,initial_wolves,0])
        unProductives.append(initialState)
        # Add initial state to the traversedStates and queue
        statesQueue.put(initialState)
        # While there is states on the queue, there are still valid movement options
        while statesQueue.empty() is False:
            curr = statesQueue.get()
            # Define all the possible movements for current state
            for i in range (0, len(self.possibleMoves)):
                nextMovement = copy.deepcopy(curr.movements)
                nextState = self.nextNode(self.possibleMoves[i],curr.move_direction , curr.leftsheeps,curr.rightsheeps,curr.leftwolves,curr.rightwolves, nextMovement)
                # print(self.possibleMoves[i])
                if self.ValidState(nextState, unProductives):
                    unProductives.append(nextState)
                    statesQueue.put(nextState)
                    # result_parent = pastResult.parent
                    # If result found, break loop and return movements
                    if nextState == finalState:
                        return nextState.movements
                        # print("this is not the final state yet")
                    # else:
                    #     return nextState.movements

        return []

