from crosswords.crosswordsolver.solver.BPSolver import BPSolver
from crosswords.crosswordsolver.solver.Crossword import Crossword
from crosswords.crosswordsolver.solver.Utils import convert_puz
from crosswords.crosswordsolver.solver.Utils import print_grid
from db.db import uploaded_puzzles
from flask_login import current_user


def cross(puzzle_file):

    def solve(crossword):
        solver = BPSolver(crossword, max_candidates=5000)
        solution = solver.solve(num_iters=5, iterative_improvement_steps=3)
        print("* Solver Output *")
        print(solution)
        print_grid(solution)
        print("* Gold Solution *")
        print_grid(crossword.letter_grid)
        #solver.evaluate(solution)
        return solution

    
 
    puzzle = convert_puz(puzzle_file)
    print(type(puzzle))

    id = uploaded_puzzles.count_documents({}) + 1


  
    puzzle.update({"crosswordid": id  , "uploader": current_user.email})
    print(puzzle)
    result = uploaded_puzzles.insert_one(puzzle)
    crossword = Crossword(puzzle)
    solution = solve(crossword)
    return solution ,puzzle
