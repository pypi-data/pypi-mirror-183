# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['stickerbook_puzzle_solver']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1', 'numpy>=1.22']

setup_kwargs = {
    'name': 'stickerbook-puzzle-solver',
    'version': '0.1.5',
    'description': 'Solving a family of puzzles seen on mathoffstickerbook.com',
    'long_description': '# Sticker book puzzle solver\nAim: automate the process of solving puzzles like this one:\n\n<img src="https://raw.githubusercontent.com/SmokyFurby/stickerbook/main/attachments/puzzle.png" width="200" height="200" />\n\n## About the family of puzzles\nThe digits 1 to 9 need to be put in the boxes exactly once so that the six calculations are correct. The calculations are read left to right and top to bottom. Moreover, you should ignore the usual order of operations, so no BODMAS here.\n\n### Example\n\nFor\n\n4 + 3 x 2,\n\nyou should apply the + first, then the x afterwards. So we obtain\n\n(4 + 3) x 2 = 7 x 2 = 14.\n\n### Where can I find more puzzles like this one?\n\nMany of them were posted by Matthew Scroggs in the Puzzle Village puzzles from his Big Internet Math-Off Stickerbook webpage, so this family of puzzles will be referred to as **stickerbook puzzles**. It is now defunct, but the link used to be at http://mathoffstickerbook.com\n\nHe still provides these puzzles elsewhere, e.g.:\n- Chalkdust Magazine, usually on the puzzle section; the puzzle in the above photo is from Issue 14, page 43\n- mscroggs.co.uk Advent calendar, e.g. https://www.mscroggs.co.uk/puzzles/advent2022/17\n\n## The package\nThis package features a class called StickerbookPuzzleSolver; it takes in the puzzle as a string. Currently, the class outputs the answer as a string to print in the terminal.\n\n### Package installation\n\nUsing pip:\n```pip install stickerbook-puzzle-solver```\n\nUsing poetry:\n```poetry add stickerbook-puzzle-solver```\n\nNote that dashes `-` must be used in the package name when installing it, while underscores `_` are used when importing it in python\n\n### Inputting the desired puzzle\nEnter the 3 rows and 3 columns in your txt file e.g. "+ + 11" for a row or column saying: ? + ? + ? = 11\n\nSo the puzzle in the above image would be saved as follows in a txt file:\n```\n+ + 22\n+ - 8\n/ * 8\n+ + 16\n+ - 8\n/ * 48\n```\n\n### Using the class to solve the puzzle\nE.g. if the puzzle txt is at `./puzzle/input.txt`, the StickerbookPuzzleSolver class can be used as follows:\n\n```python\nfrom stickerbook_puzzle_solver.stickerbook_puzzle import StickerbookPuzzleSolver\n\npuzzle_path = "./puzzle/input.txt"\n\nwith open(puzzle_path, \'r\') as reader:\n    puzzle_string = reader.read()\n\npuzzle = StickerbookPuzzleSolver(puzzle_string)\n\nsolved_puzzle = puzzle.solve()\n\nprint(solved_puzzle)\n```\n\n#### Output\nThe solve method outputs a string; the result from ```print(solved_puzzle)``` would look something like:\n```\n5 9 8\n7 2 1\n4 3 6\n```\nwhich tells you how to arrange the digits 1-9 to make all six equations in the puzzle correct. For this example, the digits would be filled in as follows:\n\n<img src="https://raw.githubusercontent.com/SmokyFurby/stickerbook/main/attachments/puzzle_solved.png" width="200" height="200" />\n\n## Repo demonstration\nA demo script called ```scripts\\main.py``` is included, showing how the class could be used in a simple CLI app.\n\n### Setting the demo up\nRun the following commands in the terminal:\n```shell\ngit clone https://github.com/SmokyFurby/stickerbook.git\ncd stickerbook\npoetry install\n./scripts/main.py --puzzle_path=./puzzle/input.txt\n```\n\nThe output should be:\n```\nInputted puzzle:\n+ + 22\n+ - 8\n/ * 8\n+ + 16\n+ - 8\n/ * 48\nThe solution is:\n5 9 8\n7 2 1\n4 3 6\n```\nThe `Inputted puzzle` section repeats the contents of the puzzle txt, while the numbers underneath `The solution is` shows how to arrange the numbers 1-9 in the puzzle grid to make all six calculations work.',
    'author': 'Belgin Seymenoglu',
    'author_email': 'belgin.seymenoglu.10@ucl.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SmokyFurby/stickerbook',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.10',
}


setup(**setup_kwargs)
