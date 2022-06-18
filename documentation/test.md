# Test document

## Unit testing

Unit tests are implemented with unittest module in python and reporting with coverage module. Currently the testing coverage is 97%, down from 100% after most recent refactoring and new features.

```
Name                        Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------
engine/ai.py                   54      1     20      0    99%   32
engine/game.py                 68      3     28      2    93%   106-107, 131
engine/player.py               34      1     12      1    96%   27
engine/round.py                33      0     12      0   100%
resources/instructions.py       8      0      2      0   100%
resources/rules.py             15      0      8      0   100%
resources/selections.py         7      0      2      0   100%
-----------------------------------------------------------------------
TOTAL                         219      5     84      3    97%
```

Tests can be reproduced with running the `coverage run --branch -m unittest && coverage report -m` commands in src folder.

Unittests also cover the correct function of algorithm.

First level Markov chain user input of "R P R S R S R" we have latest observation pair of "R" and the most likely choice next round is scissors, so algorithm needs to select object that wins it, correct answer is rock. Test runs successfully.

For instance with second level Markov chain user input of "S R P S R P S R R S R" we have latest observation pair of "S R" and with that combination paper is the most likely choice next round, so algorithm needs to select object that wins paper. Correct answer is rock. Test runs successfully.

## Other testing

Markov chain functionality have been tested with ai versus ai simulation. In each simulation two AIs play 10 times 100 rounds. In each simulation higher level Markov chain is able to beat lower level. However, the win margin is rather low. Each higher level Markov chain beats opponent by roughly 53% vs. 47%.

![lvl2](/documentation/graphs/L2_vs_L1.png)
![lvl3](/documentation/graphs/L3_vs_L1.png)
![lvl4](/documentation/graphs/L4_vs_L1.png)
![lvl4](/documentation/graphs/L4_vs_L2.png)
