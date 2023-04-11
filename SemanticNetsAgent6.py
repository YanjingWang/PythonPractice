from collections import deque
import queue
import copy


# class State:
#     def __init__(self, leftsheeps, rightsheeps, leftwolves, rightwolves,
#                  move_direction, movements):
#         # Current number of sheeps and wolves
#         self.leftsheeps = leftsheeps
#         self.rightsheeps = rightsheeps
#         self.leftwolves = leftwolves
#         self.rightwolves = rightwolves
#         # Current direction of the boat -- left or right
#         self.move_direction = move_direction
#         # Movements required to get to this state from initial
#         self.movements = movements
#
#     def __eq__(self, other):
#         # Check if its a State object
#         if isinstance(other, State):
#             return (self.leftsheeps == other.leftsheeps and self.rightsheeps == other.rightsheeps
#                     and self.leftwolves == other.leftwolves and self.rightwolves == other.rightwolves
#                     and self.move_direction == other.move_direction)
class SemanticNetsAgent():
    def __init__(self):
        self.possibleMovements = ((1, 1), (1, 0), (0, 2), (0, 1), (2, 0),(0, 1),(0, 2),(0, 1),(0, 2))
        self.S = self.State()

    def ValidState(self, prestate, unProductives):
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
    def solve(self, initial_sheep, initial_wolves):
        class State():
            def __init__(self, leftsheeps, rightsheeps, leftwolves, rightwolves,
                         move_direction, movements):
                # Current number of sheeps and wolves
                self.leftsheeps = leftsheeps
                self.rightsheeps = rightsheeps
                self.leftwolves = leftwolves
                self.rightwolves = rightwolves
                # Current direction of the boat -- left or right
                self.move_direction = move_direction
                # Movements required to get to this state from initial
                self.movements = movements

            def __eq__(self, other):
                # Check if its a State object
                if isinstance(other, State):
                    return (self.leftsheeps == other.leftsheeps and self.rightsheeps == other.rightsheeps
                            and self.leftwolves == other.leftwolves and self.rightwolves == other.rightwolves
                            and self.move_direction == other.move_direction)

        # Apply movement and get counts of sheeps and wolves
        # Apply movement and get counts of sheeps and wolves
        def getNextState(self, currentMovement, move_direction, leftsheeps, rightsheeps, leftwolves, rightwolves,
                         movements):
            movements.append(currentMovement)
            # print(currentMovement)
            if move_direction == "right":
                newState = State(leftsheeps - currentMovement[0], rightsheeps + currentMovement[0],
                                 leftwolves - currentMovement[1], rightwolves + currentMovement[1], "left", movements)
            else:
                newState = State(leftsheeps + currentMovement[0], rightsheeps - currentMovement[0],
                                 leftwolves + currentMovement[1], rightwolves - currentMovement[1], "right", movements)
            return newState
        # Assuming the initial state is valid, build matrix for initial state
        # Initialize right side with 0 sheep and 0 wolves
        statesQueue = queue.Queue()
        nonProductives = []
        nonProductiveStates = []
        nonProductiveStates.append([initial_sheep,0,initial_wolves,0])
        finalState = State(0,initial_sheep,0,initial_wolves,"left",[])
        initialState = State(initial_sheep,0,initial_wolves,0,"right",[])
        nonProductives.append(initialState)
        # Add initial state to the traversedStates and queue
        statesQueue.put(initialState)
        # While there is states on the queue, there are still valid movement options
        while not statesQueue.empty():
            currentState = statesQueue.get()
            print ("get:", currentState.leftsheeps, currentState.rightsheeps,currentState.leftwolves, currentState.rightwolves, currentState.move_direction)
            # Define all the possible movements for current state
            for i in range (0, len(self.possibleMovements)):
                nextMovement = copy.deepcopy(currentState.movements)
                nextState = self.getNextState(self.possibleMovements[i],
                                              currentState.move_direction, currentState.leftsheeps,
                                              currentState.rightsheeps,
                                              currentState.leftwolves,
                                              currentState.rightwolves, nextMovement)
                # print(self.possibleMovements[i])
                if self.ValidState(nextState, nonProductives):
                    nonProductives.append(nextState)
                    statesQueue.put(nextState)
                    # If result found, break loop and return movements
                    if nextState == finalState:
                        # print("found result")
                        return nextState.movements
        return []

# outer = SemanticNetsAgent()
# inner = outer.S
# Apply movement and get counts of sheeps and wolves
        def getNextState (self,currentMovement, move_direction, leftsheeps, rightsheeps, leftwolves, rightwolves, movements):
            movements.append(currentMovement)
            # print(currentMovement)
            if move_direction == "right":
                newState = State(leftsheeps - currentMovement[0], rightsheeps + currentMovement[0],
                                 leftwolves - currentMovement[1], rightwolves + currentMovement[1],"left", movements)
            else:
                newState = State(leftsheeps + currentMovement[0], rightsheeps - currentMovement[0],
                                 leftwolves + currentMovement[1], rightwolves - currentMovement[1], "right",movements)
            return newState