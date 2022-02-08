import util

### Model (search problem)

class TransportationProblem(object):
    def __init__(self, N):
        # N = number of blocks
        self.N = N
    def startState(self):
        return 1
    def isEnd(self, state):
        return state == self.N
    def succAndCost(self, state):
        # return list of (action, newState, cost) triples
        result = []
        if state+1<=self.N:
            result.append(('walk', state+1, 1))
        if state*2<=self.N:
            result.append(('tram', state*2, 2))
        return result

### Algorithms

def printSolution(solution):
    totalCost, history = solution
    print('totalCost: {}'.format(totalCost))
    for item in history:
        print(item)

def uniformCostSearch(problem):
    frontier = util.PriorityQueue()
    frontier.update(problem.startState(), 0)
    while True:
        # Move from frontier to explored
        state, pastCost = frontier.removeMin()
        if problem.isEnd(state):
            return (pastCost, [])
        # Push out on the frontier
        for action, newState, cost in problem.succAndCost(state):
            frontier.update(newState, pastCost+cost)

### Main

problem = TransportationProblem(N=40)
# print(problem.succAndCost(3))
printSolution(uniformCostSearch(problem))
