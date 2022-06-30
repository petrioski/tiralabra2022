# User guide

## Installing, running program and test

### Installation

```bash
python venv venv
source venv/bin/activate
python -m pip install requirements.txt
```

### Running the program

```bash
cd src
python start.py
```

### Running the test and re-produce test coverage report

Make sure you are in src directory

```bash
coverage run --branch -m unittest && coverage report -m
```

## Playing the game

The game is played with text user interface. Player can play against the computer or let computer play against itself.

### User defined settings

- Rounds: user can define how many rounds the game will last (input as integers)
- Stats: user can choose if statistics of multiAi logic will be shown (input as 'Y' or 'N')
- Focus length: user can determine number of previous games that will determine choosing the next AI (input as integers)
- max degree of Markov chain used in multiAi (input as integers)

### User game object selection

User can input selection with first letter of each available object:

- R/r -> Rock
- P/p -> Paper
- S/s -> Scissors

User repeat the instruction during the game or quit the game:

- H/h -> Repeat instructions
- Q/q -> Exit the game and print out the current score
