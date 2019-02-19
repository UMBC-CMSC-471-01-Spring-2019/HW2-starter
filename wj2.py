"""
A variation on the class water jugs problem. Given two jugs J1 and
J2 with capacities C1 and C2, initially filled with water in amounts
W1 and W2 liters.  Can you end up with exactly G1 liters in J1 and
G2 liters in J2?

You're allowed the following six actions: dump the contents of
either jug onto the floor, pour the contents of one jug into the
other until either the jug from which you are pouring is empty or
the one you are filling is full, and filling either jug that is not
yet full from a faucet until the it is full.

The cost of each action is 1 plus the amount of water it uses (if any)
from the faucet.  For example, the action of emptying J1 costs 1, and
toping off J1 if it has capacity five liters but only two liters of
water costs 4.
"""

import search as s

class WJ2(s.Problem):
    """
    STATE: tuple like (3,2) if jug J1 has 3 liters and J2 2 liters
    GOAL: a state except with -1 representing a 'don't care', so
      valid goals include (1,1) and (-1,2).
    PROBLEM: Specify capacities of each jug, initial state and goal """

    def __init__(self, capacities=(9,4), initial=(0,0), goal=(0,4)):
        self.capacities = capacities
        self.initial = initial
        self.goal = goal

    def __repr__(self):
        """ Returns a string representing the object """
        return "WJ2({},{},{})".format(self.capacities, self.initial, self.goal)

    def goal_test(self, state):
        """ Returns True iff state is a goal state """
        G1, G2 = self.goal
        return (state[0] == G1 or G1 < 0) and (state[1] == G2 or G2 < 0)

    def h(self, node):
        """ Estimate of cost of shortest path from node to a goal """
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # replace the pass statement with code to return an integer
        # that is an estimate of how far the nearest goal state is
        # your estimate shiuld be admissable, i.e., it should never
        # overestimate the distance
        pass
    
    def actions(self, state):
        """ generates legal actions for state """
        (J1, J2) = state
        (C1, C2) = self.capacities
        if J1>0: yield 'dump:1'
        if J2>0: yield'dump:2'
        if J2<C2 and J1>0: yield 'pour:1-2'
        if J1<C1 and J2>0: yield 'pour:2-1'
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # add code for actions where you fill a jug from the faucet
        

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
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # add code to handle the actions you added to the actions() method
        else:
            raise ValueError('Unrecognized action: ' + action)

    def reachable_states(self):
        """Returns a set of the states that can be reached from the initial state"""
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # replace the pass statement with code to return a set of reachable states
        pass
        
    def path_cost(self, c, state1, action, state2):
        """ Cost of path from start node to state1 assuming cost c to
        get to state1 and doing action to get to state2 """
        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # replace the pass statement with the cost
        pass


def print_solution(solution):
    """If a path to a goal was found, prints the cost and the sequence of actions
    and states on a path from the initial state to the goal found"""
    if not solution:
        print("No solution found 🙁")
    else:
        print("Path of cost", solution.path_cost, end=': ')
        for node in solution.path():
              if not node.action:  # None implies it's the initial state
                  print(node.state, end=' ')
              else:
                  print('--{}--> {}'.format(node.action, node.state), end=' ')
