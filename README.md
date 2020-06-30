### TicTacToeAI

There are two modules to search for potential TicTacToe moves for either player - Naive Search and Simulation Search

#### Naive Search

Search for all potential moves(states) up to all end states in a brute force way and see which next move gives the highest win to loss ratio

```
python naive_search.py
```

#### Simulation Search

Simulate moves(states) up to potential end states upto a certain number of iterations and see which next move gives the highest win to loss ratio

```
python simulation_search.py
```

#### How to use the TicTacToe environment

```python
from tictactoe import TicTacToe

env = TicTacToe() # Declare the environment
completed, winner = env.move(0) # Move of player 1
completed, winner = env.move(2) # Move of player 2
env.render() # Show current state of the board
```
