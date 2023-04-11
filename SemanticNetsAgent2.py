import copy
class SemanticNetsAgent:
    leftSheep = 0
    leftWolves = 0
    rightSheep = 0
    rightWolves = 0
    onLeftSide = 0
    prevState = None
    def __init__(self, lS=0, lW=0, rS=0, rW=0):
        # If you want to do any initial processing, add it here.
        self.leftSheep = lS
        self.leftWolves = lW
        self.rightSheep = rS
        self.rightWolves = rW
        self.onLeftSide = 0 # 0:left , 1=right
        self.actionT = []
    def isValid(self):
        if (self.leftSheep < 0 or self.leftWolves < 0 or self.rightSheep < 0 or
        self.rightWolves < 0):
            return False
        if (0 < self.leftSheep < self.leftWolves or 0 < self.rightSheep <
        self.rightWolves):
            return False
        return True
    def __eq__(self, other):
        return (self.leftSheep == other.leftSheep and self.leftWolves ==
        other.leftWolves and self.rightSheep == other.rightSheep and
        self.rightWolves == other.rightWolves and self.onLeftSide ==
        other.onLeftSide)
    def __hash__(self):
        return hash((self.leftSheep, self.leftWolves, self.onLeftSide,
        self.rightSheep, self.rightWolves))
    def isGoal(self):
        return ((self.onLeftSide == 1) and (self.leftSheep == 0) and
        (self.leftWolves == 0))
    def nextStates(self, current):
        nodes = []
        for sheeps in range(0, 3):
            for wolves in range(max(0, 1 - sheeps), 3 - sheeps):
                nextState = copy.deepcopy(current)
                nextState.prevState = current
                nextState.onLeftSide = 1 - (current.onLeftSide)
            # Moving from left to right
                if (current.onLeftSide == 0):
                    nextState.rightSheep += sheeps
                    nextState.rightWolves += wolves
                    nextState.leftSheep -= sheeps
                    nextState.leftWolves -= wolves
                # Moving from right to left
                else:
                    nextState.rightSheep -= sheeps
                    nextState.rightWolves -= wolves
                    nextState.leftSheep += sheeps
                    nextState.leftWolves += wolves
                if nextState.isValid():
                    nodes.append(nextState)
                    nextState.actionT.append((sheeps, wolves))
            return nodes

    # referred bfs from geeksforgeeks
    def bfs(self, root):
        if root.isGoal():
            return root

        visited = set()
        queue = [root]

        while queue:
            state = queue.pop()
            if state.isGoal():
                return state
            visited.add(state)
            for child in state.nextStates(state):
                if not (child in visited) and child not in queue:
                    queue.append(child)

    def solve(self, initial_sheep, initial_wolves):

        # Add your code here! Your solve method should receive
        # the initial number of sheep and wolves as integers,
        # and return a list of 2-tuples that represent the moves
        # required to get all sheep and wolves from the left
        # side of the river to the right.
        #
        # If it is impossible to move the animals over according
        # to the rules of the problem, return an empty list of
        # moves.
        valid = self.isValid()
        if (not (valid)):
            return []
        initial_state = SemanticNetsAgent(initial_sheep, initial_wolves)
        state = self.bfs(initial_state)

        path = []
        while state:
            path.append(state)
            state = state.prevState
        path = path[::-1]
        if (len(path) > 0):
            lastState = path[-1]
            return lastState.actionT
        else:
            return path