import sys
import argparse
import wj2
import search as s

# default searchers from aima.search to use
default_searchers = [s.breadth_first_tree_search,
                     s.breadth_first_graph_search,
                     s.depth_first_graph_search,
                     s.iterative_deepening_search,
                     s.astar_search]

def wj2solve(capacities, start, goal, searchers=default_searchers):
    problem = wj2.WJ2(capacities, start, goal)
    print("Solving {}\n".format(problem))
    print('\nReachable states:', problem.reachable_states())
    print()

    for alg in searchers:
        print('\n\nSearch algorithm:', alg.__name__)
        wj2.print_solution(alg(problem))

    print("\n\nSUMMARY: successors/goal tests/states generated/solution\n")
    s.compare_searchers([problem], [], searchers)

def convert(args):
    """ Returns tuple (g1,g2) after converting g1 and g2 to integers"""
    return (int(args[0]), int(args[1]))


# if called from the command line, call main()
if __name__ == "__main__":
    p = argparse.ArgumentParser(description='Test wj problem with several search algorithms')
    p.add_argument ('-c', '--capacities', nargs=2, type=int, default=[5,2])
    p.add_argument ('-s', '--start', nargs=2, type=int, default=[5,2])
    p.add_argument ('-g', '--goal', nargs=2, type=str, default=['0','1'])
    args = p.parse_args()
        
    wj2solve(tuple(args.capacities), tuple(args.start), convert(tuple(args.goal)))
        

