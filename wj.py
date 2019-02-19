
# Classic two water jugs problem: given two jugs J1 and J2 with capacities C1 and C2, initially filled with W1 and W2.  Can you end up with exactly G1 liters in J1 and G2 liters in J2?  You're allowed the following actions: dump the contents of either jug onto the floor, or pour the contents of one jug into the other untill either the jug from which you are pouring is empty or the one you are filling is full.


# import the AIMA search code
import aima3.search as s

# Create WJ as a subclass of the generic Problem from the aima search.py, customizing the representation, goal test, heuristic function, actions, etc.


class WJ(s.Problem):
    """
    STATE: tuple like (3,2) if jug J1 has 3 liters and J2 2 liters
    GOAL: a state except with -1 representing a 'don't care', so
      valid goals include (1,1) and (-1,2).
    PROBLEM: Specify capacities of each jug, initial state and goal """

    def __init__(self, capacities=(9,4), initial=(9,4), goal=(7,-1)):
        self.capacities = capacities
        self.initial = initial
        self.goal = goal

    def __repr__(self):
        """ Returns a string representing the object """
        return "WJ({},{},{})".format(self.capacities, self.initial, self.goal)

    def goal_test(self, state):
        """ Returns True iff state is a goal state """
        G1, G2 = self.goal
        return (state[0] == G1 or G1 < 0) and                (state[1] == G2 or G2 < 0)

    def h(self, node):
        """ Estimate of cost of shortest path from node to a goal """
        return 0 if self.goal_test(node.state) else 1
    
    def actions(self, state):
        """ generates legal actions for state """
        (J1, J2) = state
        (C1, C2) = self.capacities
        if J1 > 0: yield 'dump:1'
        if J2>0: yield 'dump:2'
        if J2<C2 and J1>0: yield 'pour:1-2'
        if J1<C1 and J2>0: yield 'pour:2-1'

    def result(self, state, action):
        """ Returns the successor of state after doing action """
        (J1, J2) = state
        (C1, C2) = self.capacities
        if action == 'dump:1':
            return (0, J2)
        elif action == 'dump:2':
            return (J1, 0)
        elif action == 'pour:1-2':
            delta = min(J1, C2-J2)
            return (J1-delta, J2+delta)
        elif action == 'pour:2-1':
            delta = min(J2, C1-J1)
            return (J1+delta, J2-delta)
        else:
            raise ValueError('Unrecognized action: ' + action)

    def path_cost(self, c, state1, action, state2):
        """ Cost of path from start node to state1 assuming cost c to
        get to state1 and doing action to get to state2 """
        return c + 1


# The following function just prints the solution found in a more readible way

def print_solution(solution):
    """If a path to a goal was found, prints the cost and the sequence of actions
    and states on a path from the initial state to the goal found"""
    if not solution:
        print("No solution found")
    else:
        print("Path of cost", solution.path_cost, end=': ')
        for node in solution.path():
              if not node.action:  # None implies it's the initial state
                  print(node.state, end=' ')
              else:
                  print('--{}--> {}'.format(node.action, node.state), end=' ')


