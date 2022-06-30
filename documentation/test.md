# Test document

## Unit testing

Unit tests are implemented with unittest module in python and reporting with coverage module. Currently the testing coverage is 97%, down from 100% after most recent refactoring and new features.

```text
Name                        Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------
engine/ai.py                  103      0     40      0   100%
engine/game.py                 58      0     22      0   100%
engine/player.py               34      0     12      0   100%
engine/round.py                33      0     12      0   100%
resources/instructions.py       8      0      2      0   100%
resources/rules.py             15      0      8      0   100%
resources/selections.py         7      0      2      0   100%
-----------------------------------------------------------------------
TOTAL                         258      0     98      0   100%
```

Tests can be reproduced with running the `coverage run --branch -m unittest && coverage report -m` commands in src folder.

## Testing single markov chaing algorithm correctness

Unittests also cover the correct functioning of Markov chains. These tests can are in [test_ai_markov_rps.py](/src/tests/test_engine/test_ai_markov_rps.py) file.

First order Markov chain user input of "R P R S R S R" we have latest observation pair of "R" and the most likely choice next round is scissors, so algorithm needs to select object that wins it, correct answer is rock. Test runs successfully.

For instance with second order Markov chain user input of "S R P S R P S R R S R" we have latest observation pair of "S R" and with that combination paper is the most likely choice next round, so algorithm needs to select object that wins paper. Correct answer is rock. Test runs successfully.

## Testing multiAi algorithm correctness

Users can repeat the test by running the program and using show statistics setting, which turns on printing of internal logic of multiAI, such as score keeping, object prediction of each Markov chain and selection of best performing AI.

For this illustration I have used the following settings:

- Game mode is 1 - human player against computer
- Maximum order of Markov chains is 5
- Focus length of 5 for past rounds and determining best performing AI
- Game is played for 35 rounds
- Human moves are input as follows: "RRR RRR RRR RRS RRS RRS RRS RRS RRS RRS RRS RR"

In sum, first we train computer that user selects only rocks. This pattern is easy to learn also for lower order Markov chains. MultiAi is will select ai#0, which is Markov chain using single last move. After first 11 moves we switch strategy to choose RRS repeatedly. Thus, the lower order Markov chains have hard time to predict next move, as rock and scissors same probability for after first rock selection. However, higher order Markov chains, and also MultiAi, should be able to detect the pattern and make switch to higher order markov chains. In practice, we can observe that multiAi switches from initial ai#0 to ai#2, i.e. third order Markov chain, which uses last three moves to predict next object.

### First phase learned, RRR

```text
Round 7 begins, good luck!
Choose object: r
>>> ai #0 - points 3 - object chosen PAPER
>>> ai #1 - points 2 - object chosen PAPER
>>> ai #2 - points 0 - object chosen PAPER
>>> ai #3 - points -1 - object chosen PAPER
>>> ai #4 - points 0 - object chosen PAPER
>>> ai #5 - points -2 - object chosen PAPER
> ai #0 chosen
Objects chosen: ROCK - PAPER
Computer wins the round!
1 - 4
Computer leads by 3 points
```

```text
Round 8 begins, good luck!
Choose object: r
>>> ai #0 - points 5 - object chosen PAPER
>>> ai #1 - points 4 - object chosen PAPER
>>> ai #2 - points 1 - object chosen PAPER
>>> ai #3 - points 1 - object chosen PAPER
>>> ai #4 - points 0 - object chosen PAPER
>>> ai #5 - points -1 - object chosen ROCK
> ai #0 chosen
Objects chosen: ROCK - PAPER
Computer wins the round!
1 -
5
Computer leads by 4 points
```

```text
Round 9 begins, good luck!
Choose object: r
>>> ai #0 - points 5 - object chosen PAPER
>>> ai #1 - points 5 - object chosen PAPER
>>> ai #2 - points 3 - object chosen PAPER
>>> ai #3 - points 3 - object chosen PAPER
>>> ai #4 - points 1 - object chosen PAPER
>>> ai #5 - points 0 - object chosen PAPER
> ai #0 chosen
Objects chosen: ROCK - PAPER
Computer wins the round!
1 - 6
Computer leads by 5 points
```

### Strategy shift to RRS

```text
Round 12 begins, good luck!
Choose object: s
>>> ai #0 - points 5 - object chosen PAPER
>>> ai #1 - points 5 - object chosen PAPER
>>> ai #2 - points 5 - object chosen PAPER
>>> ai #3 - points 5 - object chosen PAPER
>>> ai #4 - points 5 - object chosen PAPER
>>> ai #5 - points 4 - object chosen PAPER
> ai #0 chosen
Objects chosen: SCISSORS - PAPER
Player 1 wins the round!
2 - 8
Computer leads by 6 points
```

### All Markov chains start losing points

```text
Round 13 begins, good luck!
Choose object: r
>>> ai #0 - points 3 - object chosen PAPER
>>> ai #1 - points 3 - object chosenPAPER
>>> ai #2 - points 3 - object chosen PAPER
>>> ai #3 - points 3 - object chosen PAPER
>>> ai #4 - points 3 - object chosen PAPER
>>> ai #5 - points 2 - object chosen PAPER
> ai #0 chosen
Objects chosen: ROCK - PAPER
Computer wins the round!
2 - 9
Computer leads by 7 points
```

### Third order Markov chain is picking pattern up and multiAI switches ai

```text
Round 17 begins, good luck!
Choose object: r
>>> ai #0 - points 0 - object chosen ROCK
>>> ai #1 - points -1 - object chosen PAPER
>>> ai #2 - points 1 - object chosen PAPER
>>> ai #3 - points -1 - object chosen PAPER
>>> ai #4 - points -1 - object chosen ROCK
>>> ai #5 - points 0 - object chosen ROCK
> ai #2 chosen
Objects chosen: ROCK - PAPER
Computer wins the round!
3 - 11
```

### Third order Markov chain starts improving performance as past losses are replaced by new wins

```text
Computer leads by 8 points
==================================================
Round 18 begins, good luck!
Choose object: s
>>> ai #0 - points 1 - object chosen PAPER
>>> ai #1 - points 1 - object chosen ROCK
>>> ai #2 - points 3 - object chosen ROCK
>>> ai #3 - points 1 - object chosen ROCK
>>> ai #4 - points 0 - object chosen ROCK
>>> ai #5 - points 1 - object chosen PAPER
> ai #2 chosen
Objects chosen: SCISSORS - ROCK
Computer wins the round!
3 - 12
Computer leads by 9 points
==================================================
Round 19 begins, good luck!
Choose object: r
>>> ai #0 - points -1 - object chosen PAPER
>>> ai #1 - points 1 - object chosen PAPER
>>> ai #2 - points 3 - object chosen PAPER
>>> ai #3 - points 1 - object chosen PAPER
>>> ai #4 - points 0 - object chosen PAPER
>>> ai #5 - points -1 - object chosen PAPER
> ai #2 chosen
Objects chosen: ROCK - PAPER
Computer wins the round!
3 - 13
Computer leads by 10 points
==================================================
Round 20 begins, good luck!
Choose object: r
>>> ai #0 - points 0 - object chosen ROCK
>>> ai #1 - points 3 - object chosen PAPER
>>> ai #2 - points 4 - object chosen PAPER
>>> ai #3 - points 3 - object chosen PAPER
>>> ai #4 - points 2 - object chosen PAPER
>>> ai #5 - points 0 - object chosen PAPER
> ai #2 chosen
Objects chosen: ROCK - PAPER
Computer wins the round!
3 - 14
Computer leads by 11 points
```

### Also other higher order Markov chains are improving their win streaks

```text
Round 22 begins, good luck!
Choose object: r
>>> ai #0 - points -1 - object chosen PAPER
>>> ai #1 - points 3 - object chosen PAPER
>>> ai #2 - points 5 - object chosen PAPER
>>> ai #3 - points 5 - object chosen PAPER
>>> ai #4 - points 4 - object chosen PAPER
>>> ai #5 - points 0 - object chosen ROCK
> ai #2 chosen
Objects chosen: ROCK - PAPER
Computer wins the round!
4 - 15
Computer leads by 11 points
```

```text
Round 26 begins, good luck!
Choose object: r
>>> ai #0 - points 0 - object chosen PAPER
>>> ai #1 - points 3 - object chosen PAPER
>>> ai #2 - points 5 - object chosen PAPER
>>> ai #3 - points 5 - object chosen PAPER
>>> ai #4 - points 5 - object chosen PAPER
>>> ai #5 - points 0 - object chosen SCISSORS
> ai #2 chosen
Objects chosen: ROCK - PAPER
Computer wins the round!
4 - 19
Computer leads by 15 points
```

### Higher order Markov chains are keeping up with good scores while lower order chains are struggling with predictions

```text
Round 34 begins, good luck!
Choose object: r
>>> ai #0 - points 2 - object chosen PAPER
>>> ai #1 - points 1 - object chosen PAPER
>>> ai #2 - points 5 - object chosen PAPER
>>> ai #3 - points 5 - object chosen PAPER
>>> ai #4 - points 5 - object chosen PAPER
>>> ai #5 - points 1 - object chosen SCISSORS
> ai #2 chosen
Objects chosen: ROCK - PAPER
Computer wins the round!
5 - 26
Computer leads by 21 points
==================================================
Round 35 begins, good luck!
Choose object: r
>>> ai #0 - points 2 - object chosen ROCK
>>> ai #1 - points 1 - object chosen PAPER
>>> ai #2 - points 5 - object chosen PAPER
>>> ai #3 - points 5 - object chosen PAPER
>>> ai #4 - points 5 - object chosen PAPER
>>> ai #5 - points 0 - object chosen SCISSORS
Objects chosen: ROCK - PAPER
Computer wins the round!
5 - 27
Computer leads by 22 points
5 - 27
Computer wins by 22 points
```
