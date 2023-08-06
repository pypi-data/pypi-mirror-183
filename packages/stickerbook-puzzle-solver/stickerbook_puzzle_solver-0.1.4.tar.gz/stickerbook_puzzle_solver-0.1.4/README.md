# Sticker book puzzle solver
Aim: automate the process of solving puzzles like this one:

<img src="./attachments/puzzle.png" width="200" height="200" />

## About the family of puzzles
The digits 1 to 9 need to be put in the boxes exactly once so that the six calculations are correct. The calculations are read left to right and top to bottom. Moreover, you should ignore the usual order of operations, so no BODMAS here.

### Example

For

4 + 3 x 2,

you should apply the + first, then the x afterwards. So we obtain

(4 + 3) x 2 = 7 x 2 = 14.

### Where can I find more puzzles like this one?

Many of them were posted by Matthew Scroggs in the Puzzle Village puzzles from his Big Internet Math-Off Stickerbook webpage, so this family of puzzles will be referred to as **stickerbook puzzles**. It is now defunct, but the link used to be at http://mathoffstickerbook.com

He still provides these puzzles elsewhere, e.g.:
- Chalkdust Magazine, usually on the puzzle section; the puzzle in the above photo is from Issue 14, page 43
- mscroggs.co.uk Advent calendar, e.g. https://www.mscroggs.co.uk/puzzles/advent2022/17

## The package
This package features a class called StickerbookPuzzleSolver; it takes in the puzzle as a string. Currently, the class outputs the answer as a string to print in the terminal.

### Package installation

Using pip:
```pip install stickerbook-puzzle-solver```

Using poetry:
```poetry add stickerbook-puzzle-solver```

Note that dashes `-` must be used in the package name when installing it, while underscores `_` are used when importing it in python

### Inputting the desired puzzle
Enter the 3 rows and 3 columns in your txt file e.g. "+ + 11" for a row or column saying: ? + ? + ? = 11

So the puzzle in the above image would be saved as follows in a txt file:
```
+ + 22
+ - 8
/ * 8
+ + 16
+ - 8
/ * 48
```

### Using the class to solve the puzzle
E.g. if the puzzle txt is at `./puzzle/input.txt`, the StickerbookPuzzleSolver class can be used as follows:

```python
from stickerbook_puzzle_solver.stickerbook_puzzle import StickerbookPuzzleSolver

puzzle_path = "./puzzle/input.txt"

with open(puzzle_path, 'r') as reader:
    puzzle_string = reader.read()

puzzle = StickerbookPuzzleSolver(puzzle_string)

solved_puzzle = puzzle.solve()

print(solved_puzzle)
```

#### Output
The solve method outputs a string; the result from ```print(solved_puzzle)``` would look something like:
```
5 9 8
7 2 1
4 3 6
```
which tells you how to arrange the digits 1-9 to make all six equations in the puzzle correct. For this example, the digits would be filled in as follows:

<img src="./attachments/puzzle_solved.png" width="200" height="200" />

## Repo demonstration
A demo script called ```scripts\main.py``` is included, showing how the class could be used in a simple CLI app.

### Setting the demo up
Run the following commands in the terminal:
```shell
git clone https://github.com/SmokyFurby/stickerbook.git
cd stickerbook
poetry install
./scripts/main.py --puzzle_path=./puzzle/input.txt
```

The output should be:
```
Inputted puzzle:
+ + 22
+ - 8
/ * 8
+ + 16
+ - 8
/ * 48
The solution is:
5 9 8
7 2 1
4 3 6
```
The `Inputted puzzle` section repeats the contents of the puzzle txt, while the numbers underneath `The solution is` shows how to arrange the numbers 1-9 in the puzzle grid to make all six calculations work.