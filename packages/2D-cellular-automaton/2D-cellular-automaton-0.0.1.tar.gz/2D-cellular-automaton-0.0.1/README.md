# 2D Cellular Automaton

This project was inspired by discussions in MATH 340 Mathematical Excursions. While we visualized multiple starting indicies for 2D cellular automata in Excel, I knew a Python script would allow greater functioniality and easier usage.

I came across a respository on GitHub by Zhiming Wang titled [rule30](https://github.com/zmwangx/rule30). Nearly all the code is borrowed from there and made it unnecessary for me to start from scratch. All the functionalities from Wang's solution exist in this project, with the only additions being supporting multiple starting indicies.

# Table of Contents
1. [Installation](#Installation)
2. [Usage](#Usage)
4. [Credit](#Credit)
5. [License](License)

## Installation
`pip install 2DCellularAutomaton`

## Usage
```python
from CellularAutomaton import Automaton

rows = 100 #Any positive number
rule = 30 #From 1-256. More can be seen here https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
starting_indicies = [20, 60] #Note this refers to the columns and columns = 2 * rows - 1, which is why rows - 1 yields center.
block_size = 1

automata = Automaton(rows=rows, rule=rule, starting_indicies=starting_indicies)
image = automata.image(block_size=block_size)
image.save('Rule 30 | Column 20 and 60.jpeg')
```

Output

<img src="image.jpeg" alt="drawing" width="600"/>

## Credit
1. Zhiming Wang's [rule30](https://github.com/zmwangx/rule30)

## License 
MIT