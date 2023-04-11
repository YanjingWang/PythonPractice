import queue
import copy
from collections import deque
class SemanticNetsAgent:
    move_directions = 'left'
    def __init__(self):
        self.possibleMoves = [(1, 1), (1, 0), (0, 2), (0, 1), (2, 0),(0, 1),(0, 2),(0, 1),(0, 2)]
        self.move_directions = 'left'
        pass
        # This method return boolean , true in it's a valid state : number of sheeps vs wolves
        # are correct and it's not a previous state
    def isValidState(self, prestate, unProductives):
        # unproductive state : current state is same to previous state
        for unProductive in unProductives:
            if unProductive == prestate:
                return False
        # Illegal state : Negative number of sheeps or wolves
        if prestate.leftsheeps < 0 or prestate.rightsheeps < 0 or prestate.leftwolves < 0 or prestate.rightwolves < 0:
            return False
        # Illegal state : wolves outnumber sheeps on the left or wolves outnumber sheeps on the right side
        if prestate.leftwolves > prestate.leftsheeps > 0 or prestate.rightwolves > prestate.rightsheeps > 0:
            return False
        return True

    # def finalState(self):
    #     if self.leftsheeps == 0 and self.leftwolves == 0 and self.move_directions == 'right':
    #             # and self.rightsheeps == initial_sheep and self.rightwolves == initial_wolves \
    #         return True
    #     else:
    #         False

    def solve(self, initial_sheep, initial_wolves):
        #Add your code here! Your solve method should receive
        #the initial number of sheep and wolves as integers,
        #and return a list of 2-tuples that represent the moves
        #required to get all sheep and wolves from the left
        #side of the river to the right.
        #
        #If it is impossible to move the animals over according
        #to the rules of the problem, return an empty list of
        #moves. return the list of moves or empty list for unsolvable


        class State:
            def __init__(self, leftsheeps, rightsheeps, leftwolves, rightwolves,
                         move_directions, movements):
                # Current number of sheeps and wolves
                self.leftsheeps = leftsheeps
                self.rightsheeps = rightsheeps
                self.leftwolves = leftwolves
                self.rightwolves = rightwolves
                # Current direction of the boat -- left or right
                self.move_directions = move_directions
                # Movements required to get to this state from initial
                self.movements = movements

            def __eq__(self, other):
                # Check if its a State object
                if isinstance(other, State):
                    return (self.leftsheeps == other.leftsheeps and self.rightsheeps == other.rightsheeps
                            and self.leftwolves == other.leftwolves and self.rightwolves == other.rightsheeps
                            and self.move_directions == other.move_directions)

            def finalState(self):
                if self.leftsheeps == 0 and self.leftwolves == 0 and self.move_directions == 'right' \
                    and self.rightsheeps == initial_sheep and self.rightwolves == initial_wolves: \
                    return True
                else:
                    False

            # def isValidState(self,prestate,unProductive):
            #     # unproductive state : current state is same to previous state
            #     # for unProductive in unProductives:
            #     #     if unProductive == prestate:
            #     #         return False
            #     # Illegal state : Negative number of sheeps or wolves
            #     if self.leftsheeps < 0 or self.rightsheeps < 0 or self.leftwolves < 0 or self.rightwolves < 0:
            #         return False
            #     # Illegal state : wolves outnumber sheeps on the left or wolves outnumber sheeps on the right side
            #     if self.leftwolves > self.leftsheeps > 0 or self.rightwolves > self.rightsheeps and self.rightsheeps > 0:
            #         return False
            #     return True



        # citation from: geeksforgeeks
        def nextNodes(curr,move_directions,leftsheeps, rightsheeps, leftwolves, rightwolves,next_State):
            nextState = []
            nextState.append(curr)
            possibleMoves = [(1, 1), (1, 0), (0, 2), (0, 1), (2, 0), (0, 1), (0, 2), (0, 1), (0, 2)]
            # movements.append(currentMovement)

            if move_directions == 'right': # move from right to left
                for currentMovement in possibleMoves:
                    next_State = State(leftsheeps - currentMovement[0], rightsheeps + currentMovement[0],
                             leftwolves - currentMovement[1], rightwolves + currentMovement[1],"left", nextState)
                    # if next_right_State.isValidState():
                    #     nextState.append(next_right_State)
                    #     next_right_State.movements = curr
                    # if next_State.isValidState(nextState, unProductives):
                    #     unProductives.append(nextState)
                    #     statesQueue.put(nextState)
                    #     # If result found, break loop and return movements
                    #     if nextState == finalState:
                    #         # print("found result")
                    #         return nextState.movements

            else:
                for move in possibleMoves:
                    next_State = State(leftsheeps + move[0], rightsheeps - move[0],
                             leftwolves + move[1], rightwolves - move[1], "right",nextState)
                    # if new_left_State.isValidState():
                    #     nextState.append(new_left_State)
                    #     new_left_State.movements = curr
                    # if next_State.isValidState(nextState, unProductives):
                    #     unProductives.append(nextState)
                    #     statesQueue.put(nextState)
                    #     # If result found, break loop and return movements
                    #     if nextState == finalState:
                    #         # print("found result")
                    #         return nextState.movements
            return next_State
        # end citation


        def bfs():  # breadth-first-search (BFS)
            initial_state = State(initial_sheep, initial_wolves, 0, 0, "left")  # root
            if initial_state.finalState():
                return initial_state
            queue = deque([])
            explored = []
            queue.append(initial_state)
            while queue:
                node = queue.popleft()
                if node.goal_state():
                    return node
                explored.append(node)
                node_children = nextNodes(node)
                for child in node_children:
                    if (child not in explored) and (child not in queue):
                        queue.append(child)
            return None

        statesQueue = queue.Queue()
        unProductives = []
        unProductiveStates = []
        unProductiveStates.append([initial_sheep, 0, initial_wolves, 0])
        finalState = State(0, initial_sheep, 0, initial_wolves, "left", [])
        initialState = State(initial_sheep, 0, initial_wolves, 0, "right", [])
        unProductives.append(initialState)
        statesQueue.put(initialState)

        while statesQueue.empty() is False:
            currentState = statesQueue.get()
            print("get:", currentState.leftsheeps, currentState.rightsheeps, currentState.leftwolves,
                  currentState.rightwolves, currentState.move_directions)
            # Define all the possible movements for current state
            for i in range(0, len(self.possibleMoves)):
                nextState = copy.deepcopy(currentState.movements)
                # print(self.possibleMoves[i])
                nextState = nextNodes(self.possibleMoves[i],currentState.move_directions,currentState.leftsheeps, currentState.rightsheeps, currentState.leftwolves,
                            currentState.rightwolves, nextState)  # nextState = nextMovements

            if self.isValidState(nextState, unProductives):
                unProductives.append(nextState)
                statesQueue.put(nextState)
                # If result found, break loop and return movements
                if nextState == finalState:
                    # print("found result")
                    return nextState.movements

        # pass
        return []
