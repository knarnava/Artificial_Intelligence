import numpy as np

class NodeInitialise:
    def __init__(self, state_of_node, parent_node, each_actionNode):
        self.state_of_node = state_of_node
        self.parent_node = parent_node
        self.each_actionNode = each_actionNode


class Stack_frontier_of_stack:
    def __init__(self):
        self.frontier_of_stack = []

    def add(self, node):
        """

        :param node:
        """
        self.frontier_of_stack.append(node)

    def contains_state_of_node(self, state_of_node):
        """
        check if node contains the state
        :param state_of_node:
        :return:
        """
        return any((node.state_of_node[0] == state_of_node[0]).all() for node in self.frontier_of_stack)

    def is_empty(self):
        """
        check tif frontier of stack is empty
        :return:
        """
        return len(self.frontier_of_stack) == 0

    def remove(self):
        """
        if frontier is not empty then removing the nodes
        :return:
        """
        if self.is_empty():
            raise Exception("Empty frontier_of_stack")
        else:
            node = self.frontier_of_stack[-1]
            self.frontier_of_stack = self.frontier_of_stack[:-1]
            return node


class Queuefrontier_of_stack(Stack_frontier_of_stack):
    def remove(self):
        """

        :return:
        """
        if self.is_empty():
            raise Exception("Empty frontier_of_stack")
        else:
            node = self.frontier_of_stack[0]
            self.frontier_of_stack = self.frontier_of_stack[1:]
            return node


class PuzzleProblem:
    def __init__(self, startingPoint, startingPointIndex, goal_of_the_problem, goal_of_the_problemIndex):
        self.startingPoint = [startingPoint, startingPointIndex]
        self.goal_of_the_problem = [goal_of_the_problem, goal_of_the_problemIndex]
        self.required_result = None

    def neighbours_of_node(self, state_of_node):
        """
        find the neighbours of the node
        :param state_of_node:
        :return:
        """
        matrix_puzzle, (puzzle_row, puzzle_col) = state_of_node
        resultant = []

        if puzzle_row > 0:
            matrix_puzzle1 = np.copy(matrix_puzzle)
            matrix_puzzle1[puzzle_row][puzzle_col] = matrix_puzzle1[puzzle_row - 1][puzzle_col]
            matrix_puzzle1[puzzle_row - 1][puzzle_col] = 0
            resultant.append(('up', [matrix_puzzle1, (puzzle_row - 1, puzzle_col)]))
        if puzzle_col > 0:
            matrix_puzzle1 = np.copy(matrix_puzzle)
            matrix_puzzle1[puzzle_row][puzzle_col] = matrix_puzzle1[puzzle_row][puzzle_col - 1]
            matrix_puzzle1[puzzle_row][puzzle_col - 1] = 0
            resultant.append(('left', [matrix_puzzle1, (puzzle_row, puzzle_col - 1)]))
        if puzzle_row < 2:
            matrix_puzzle1 = np.copy(matrix_puzzle)
            matrix_puzzle1[puzzle_row][puzzle_col] = matrix_puzzle1[puzzle_row + 1][puzzle_col]
            matrix_puzzle1[puzzle_row + 1][puzzle_col] = 0
            resultant.append(('down', [matrix_puzzle1, (puzzle_row + 1, puzzle_col)]))
        if puzzle_col < 2:
            matrix_puzzle1 = np.copy(matrix_puzzle)
            matrix_puzzle1[puzzle_row][puzzle_col] = matrix_puzzle1[puzzle_row][puzzle_col + 1]
            matrix_puzzle1[puzzle_row][puzzle_col + 1] = 0
            resultant.append(('right', [matrix_puzzle1, (puzzle_row, puzzle_col + 1)]))

        return resultant

    def print_resultant_matrix(self):
        required_result = self.required_result if self.required_result is not None else None
        print("starting Point state of the node:\n", self.startingPoint[0], "\n")
        print("goal of the problem state of node:\n", self.goal_of_the_problem[0], "\n")
        print("\nstates of the nodes explored_nodes: ", self.num_explored_nodes, "\n")
        print("required_resultant :\n ")
        for each_actionNode, each_cell in zip(required_result[0], required_result[1]):
            print("action node: ", each_actionNode, "\n", each_cell[0], "\n")
        print("goal of the problem Achieved!!")

    def state_of_node_missing(self, state_of_node):

        for st in self.explored_nodes:
            if (st[0] == state_of_node[0]).all():
                return False
        return True

    def solve_puzzle(self):
        self.num_explored_nodes = 0

        startingPoint = NodeInitialise(state_of_node=self.startingPoint, parent_node=None, each_actionNode=None)
        frontier_of_stack = Queuefrontier_of_stack()
        frontier_of_stack.add(startingPoint)

        self.explored_nodes = []

        while True:
            if frontier_of_stack.is_empty():
                raise Exception("There is No required result")

            node = frontier_of_stack.remove()
            self.num_explored_nodes += 1

            if (node.state_of_node[0] == self.goal_of_the_problem[0]).all():
                each_node_of_action = []
                every_cell = []
                while node.parent_node is not None:
                    each_node_of_action.append(node.each_actionNode)
                    every_cell.append(node.state_of_node)
                    node = node.parent_node
                each_node_of_action.reverse()
                every_cell.reverse()
                self.required_result = (each_node_of_action, every_cell)
                return

            self.explored_nodes.append(node.state_of_node)

            for each_actionNode, state_of_node in self.neighbours_of_node(node.state_of_node):
                if not frontier_of_stack.contains_state_of_node(state_of_node) and self.state_of_node_missing(state_of_node):
                    child = NodeInitialise(state_of_node=state_of_node, parent_node=node, each_actionNode=each_actionNode)
                    frontier_of_stack.add(child)


'''startingPoint = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
goal_of_the_problem = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])'''
startingPoint = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
goal_of_the_problem = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]])

startingPointIndex = (1, 1)
goal_of_the_problemIndex = (1, 0)

p = PuzzleProblem(startingPoint, startingPointIndex, goal_of_the_problem, goal_of_the_problemIndex)
p.solve_puzzle()
p.print_resultant_matrix()