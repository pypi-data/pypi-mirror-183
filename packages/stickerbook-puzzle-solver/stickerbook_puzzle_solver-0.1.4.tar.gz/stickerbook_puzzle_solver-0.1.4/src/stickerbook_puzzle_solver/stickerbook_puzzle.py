import itertools
import numpy as np

from typing import List, Union

from .equation_lhs import RowOrColumn


class StickerbookPuzzleSolver:
    def __init__(self, puzzle_string: str):
        self._puzzle_string = puzzle_string
        self._puzzle = None
        self._solution = None

    def solve(self) -> str:
        """
        Takes in the string describing the puzzle and outputs
        the solution, showing where to put the digits 1-9.
        puzzle_string: string specifying puzzle
        return: string giving the solution
        """
        self._puzzle = self.read_string()
        solution = self.seek_solution()

        return solution

    def read_string(self) -> List[List[Union[str, float]]]:
        """
        Read string describing puzzle,
        converting it into a form the solver can understand.
        puzzle_string: string specifying puzzle
        return: array of numbers and operations for each row and column
        """
        puzzle = [
            part.split(' ')
            for part
            in self._puzzle_string.split('\n')
        ]

        puzzle = [
            row[:2] + [float(row[2])]
            for row
            in puzzle
            if len(row) == 3
        ]

        return puzzle

    def seek_solution(self) -> str:
        """
        Build up the six simultaneous equations, find the positions
        of the nine digits by brute force and print them as a string.
        puzzle: array of numbers and operations for each row and column
        return: str with digits that should go into the boxes
        """
        perms = itertools.permutations(range(1, 10), r=None)

        for perm in perms:
            a, b, c, d, e, f, g, h, i = perm

            row1 = RowOrColumn().build_equation(a, self._puzzle[0][0], b, self._puzzle[0][1], c, self._puzzle[0][2])
            row2 = RowOrColumn().build_equation(d, self._puzzle[1][0], e, self._puzzle[1][1], f, self._puzzle[1][2])
            row3 = RowOrColumn().build_equation(g, self._puzzle[2][0], h, self._puzzle[2][1], i, self._puzzle[2][2])

            col1 = RowOrColumn().build_equation(a, self._puzzle[3][0], d, self._puzzle[3][1], g, self._puzzle[3][2])
            col2 = RowOrColumn().build_equation(b, self._puzzle[4][0], e, self._puzzle[4][1], h, self._puzzle[4][2])
            col3 = RowOrColumn().build_equation(c, self._puzzle[5][0], f, self._puzzle[5][1], i, self._puzzle[5][2])

            if all([row1, row2, row3, col1, col2, col3]):
                self._solution = np.array(perm).reshape((3, 3))
                return self.solution_array_to_string()

    def solution_array_to_string(self) -> str:
        """
        Print the solution array as a string
        solution:
        return: string showing where to put the digits 1-9
        """
        sol_string = '\n'.join(
            ' '.join(
                [
                    str(num)
                    for num
                    in row
                ]
            )
            for row
            in self._solution
        )
        return sol_string
