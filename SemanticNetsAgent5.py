import queue
import copy


class State:
    def __init__(self, leftsheeps, rightsheeps, leftwolves, rightwolves,
                 currentDirection, movements):
        # Current number of sheeps and wolves
        self.leftsheeps = leftsheeps
        self.rightsheeps = rightsheeps
        self.leftwolves = leftwolves
        self.rightwolves = rightwolves
        # Current direction of the boat -- left or right
        self.currentDirection = currentDirection
        # Movements required to get to this state from initial
        self.movements = movements

    def __eq__(self, other):
        # Check if its a State object
        if isinstance(other, State):
            return (self.leftsheeps == other.leftsheeps and self.rightsheeps == other.rightsheeps
                    and self.leftwolves == other.leftwolves and self.rightwolves == other.rightwolves
                    and self.currentDirection == other.currentDirection)

    def finalState(self):
        if self.leftsheeps == 0 and self.leftwolves == 0 and self.move_directions == 'right':
                return True
        else:
            False
    def validstate(self, state, nonProductives):
        for nonProductive in nonProductives:
            if nonProductive == state:
                return False
        if state.leftsheeps < 0 or state.rightsheeps < 0 or state.leftwolves < 0 or state.rightwolves < 0:
            return False
        # More wolves that sheeps on the left
        if (state.leftwolves > state.leftsheeps and state.leftsheeps > 0):
            return False
        # More wolves that sheeps on the right
        if (state.rightwolves > state.rightsheeps and state.rightsheeps > 0):
            return False
        return True

class SemanticNetsAgent:
    def __init__(self):
        self.possibleMovements = ((1, 1), (1, 0), (0, 2), (0, 1), (2, 0),(0, 1),(0, 2),(0, 1),(0, 2))
        pass

    # This method return boolean , true in it's a valid state : number of sheeps vs wolves
    # are correct and it's not a previous state
    # def validstate(self, state, nonProductives):
    #     for nonProductive in nonProductives:
    #         if nonProductive == state:
    #             return False
    #     if state.leftsheeps < 0 or state.rightsheeps < 0 or state.leftwolves < 0 or state.rightwolves < 0:
    #         return False
    #     # More wolves that sheeps on the left
    #     if (state.leftwolves > state.leftsheeps and state.leftsheeps > 0):
    #         return False
    #     # More wolves that sheeps on the right
    #     if (state.rightwolves > state.rightsheeps and state.rightsheeps > 0):
    #         return False
    #     return True
    def solve(self, initial_sheep, initial_wolves):


        # Apply movement and get counts of sheeps and wolves
        # Apply movement and get counts of sheeps and wolves
        # def getNextState(self, currentMovement, currentDirection, leftsheeps, rightsheeps, leftwolves, rightwolves,
        #                  movements):
        #     movements.append(currentMovement)
        #     # print(currentMovement)
        #     if currentDirection == "right":
        #         newState = State(leftsheeps - currentMovement[0], rightsheeps + currentMovement[0],
        #                          leftwolves - currentMovement[1], rightwolves + currentMovement[1], "left", movements)
        #     else:
        #         newState = State(leftsheeps + currentMovement[0], rightsheeps - currentMovement[0],
        #                          leftwolves + currentMovement[1], rightwolves - currentMovement[1], "right", movements)
        #     return newState
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
            print ("get:", currentState.leftsheeps, currentState.rightsheeps,currentState.leftwolves, currentState.rightwolves, currentState.currentDirection)
            # Define all the possible movements for current state
            for i in range (0, len(self.possibleMovements)):
                nextMovement = copy.deepcopy(currentState.movements)
                nextState = self.getNextState(self.possibleMovements[i],
                                              currentState.currentDirection, currentState.leftsheeps,
                                              currentState.rightsheeps,
                                              currentState.leftwolves,
                                              currentState.rightwolves, nextMovement)
                # print(self.possibleMovements[i])
                if State.validstate(nextState, nonProductives):
                    nonProductives.append(nextState)
                    statesQueue.put(nextState)
                    # If result found, break loop and return movements
                    if nextState == finalState:
                        # print("found result")
                        return nextState.movements
        return []
    # Apply movement and get counts of sheeps and wolves
    def getNextState (self,currentMovement, currentDirection, leftsheeps, rightsheeps, leftwolves, rightwolves, movements):
        movements.append(currentMovement)
        # print(currentMovement)
        if currentDirection == "right":
            newState = State(leftsheeps - currentMovement[0], rightsheeps + currentMovement[0],
                             leftwolves - currentMovement[1], rightwolves + currentMovement[1],"left", movements)
        else:
            newState = State(leftsheeps + currentMovement[0], rightsheeps - currentMovement[0],
                             leftwolves + currentMovement[1], rightwolves - currentMovement[1], "right",movements)
        return newState