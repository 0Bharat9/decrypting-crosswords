from solver.BPSolver import BPSolver
from solver.Crossword import Crossword
from solver.Utils import convert_puz
from solver.Utils import print_grid

puzzle_file = '../crosswordsolver/puzzles/LA_times/20240214.puz'


def solve(crossword):
    solver = BPSolver(crossword, max_candidates=500000)
    solution = solver.solve(num_iters=10, iterative_improvement_steps=5)
    print("*** Solver Output ***")
    print_grid(solution)
    print("*** Gold Solution ***")
    print_grid(crossword.letter_grid)
    solver.evaluate(solution)


puzzle = convert_puz(puzzle_file)
crossword = Crossword(puzzle)
solve(crossword)
