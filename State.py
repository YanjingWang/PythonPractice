# Object to define current state of sheeps and wolves , current direction and next direction
class State:
    def __init__(self,leftsheeps, rightsheeps, leftwolves, rightwolves,
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