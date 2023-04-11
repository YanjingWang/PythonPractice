import queue
import copy
from collections import deque
class SemanticNetsAgent:
    move_directions = 'left'
    def __init__(self):
        self.possibleMoves = [(1, 1), (1, 0), (0, 2), (0, 1), (2, 0),(0, 1),(0, 2),(0, 1),(0, 2)]
        # self.move_directions = 'left'
        pass
        # This method return boolean , true in it's a valid state : number of sheeps vs wolves
        # are correct and it's not a previous state
    # def isValidState(self, prestate, unProductives):
    #     # unproductive state : current state is same to previous state
    #     for unProductive in unProductives:
    #         if unProductive == prestate:
    #             return False
    #     # Illegal state : Negative number of sheeps or wolves
    #     if prestate.leftsheeps < 0 or prestate.rightsheeps < 0 or prestate.leftwolves < 0 or prestate.rightwolves < 0:
    #         return False
    #     # Illegal state : wolves outnumber sheeps on the left or wolves outnumber sheeps on the right side
    #     if prestate.leftwolves > prestate.leftsheeps > 0 or prestate.rightwolves > prestate.rightsheeps > 0:
    #         return False
    #     return True


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
            def __init__(self, leftsheeps, leftwolves, rightsheeps,  rightwolves,
                         move_directions):
                # Current number of sheeps and wolves
                self.leftsheeps = leftsheeps
                self.rightsheeps = rightsheeps
                self.leftwolves = leftwolves
                self.rightwolves = rightwolves
                # Current direction of the boat -- left or right
                self.move_directions = move_directions
                # Movements required to get to this state from initial
                self.movements = None

            def __eq__(self, other):
                # Check if its a State object
                if isinstance(other, State):
                    return (self.leftsheeps == other.leftsheeps and self.rightsheeps == other.rightsheeps
                            and self.leftwolves == other.leftwolves and self.rightwolves == other.rightsheeps
                            and self.move_directions == other.move_directions)
                else:
                    False

            def finalState(self):
                if self.leftsheeps == 0 and self.leftwolves == 0 and self.move_directions == 'right' \
                    and self.rightsheeps == initial_sheep and self.rightwolves == initial_wolves: \
                    return True
                else:
                    False

            def isValidState(self):
                # unproductive state : current state is same to previous state
                # for unProductive in unProductives:
                #     if unProductive == prestate:
                #         return False
                # Illegal state : Negative number of sheeps or wolves
                if self.leftsheeps < 0 or self.rightsheeps < 0 or self.leftwolves < 0 or self.rightwolves < 0:
                    return False
                # Illegal state : wolves outnumber sheeps on the left or wolves outnumber sheeps on the right side
                if self.leftwolves > self.leftsheeps > 0 or self.rightwolves > self.rightsheeps and self.rightsheeps > 0:
                    return False
                return True



        # citation from: geeksforgeeks
        def nextNodes(curr):
            nextState = []
            # nextState.append(curr)
            possibleMoves = [(1, 1), (1, 0), (0, 2), (0, 1), (2, 0), (0, 1), (0, 2), (0, 1), (0, 2)]
            # movements.append(currentMovement)

            if curr.move_directions == 'right': # move from right to left
                for currentMovement in possibleMoves:
                    next_State = State(curr.leftsheeps + currentMovement[0], curr.rightsheeps - currentMovement[0],
                             curr.leftwolves - currentMovement[1], curr.rightwolves + currentMovement[1],"left")
                    if next_State.isValidState():
                        nextState.append(next_State)
                        next_State.movements = curr
                    # if next_State.isValidState(nextState, unProductives):
                    #     unProductives.append(nextState)
                    #     statesQueue.put(nextState)
                    #     # If result found, break loop and return movements
                    #     if nextState == finalState:
                    #         # print("found result")
                    #         return nextState.movements

            else:
                for move in possibleMoves:
                    next_State = State(curr.leftsheeps + move[0], curr.rightsheeps - move[0],
                             curr.leftwolves + move[1], curr.rightwolves - move[1], "right")
                    if next_State.isValidState():
                        nextState.append(next_State)
                        next_State.movements = curr
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
                if node.finalState():
                    return node
                explored.append(node)
                node_children = nextNodes(node)
                for child in node_children:
                    if (child not in explored) and (child not in queue):
                        queue.append(child)
            return None

        def find_moves(result):
            path = []
            final_path = []
            result_parent = result.movements
            while result_parent:
                move = (abs(result.left_missionaries - result_parent.left_missionaries),
                        abs(result.left_cannibals - result_parent.left_cannibals))
                path.append(move)
                result = result_parent
                result_parent = result.movements
            for i in range(len(path)):
                final_result = path[len(path) - 1 - i]
                final_path.append(final_result)
            return final_path

        solution = bfs()
        if solution:
            return find_moves(solution)
        else:
            return []



