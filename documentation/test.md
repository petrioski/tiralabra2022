# Test document

Unit tests are implemented with unittest module in python and reporting with coverage module. Currently the testing [coverage is 100%](coverage/coverage.txt).

Tests can be reproduced with running the `coverage run --branch -m unittest && coverage report -m` commands in src folder.

Unittests also cover the correct function of algorithm.

First level Markov chain user input of "R P R S R S R" we have latest observation pair of "R" and the most likely choice next round is scissors, so algorithm needs to select object that wins it, correct answer is rock. Test runs successfully.

For instance with second level Markov chain user input of "S R P S R P S R R S R" we have latest observation pair of "S R" and with that combination paper is the most likely choice next round, so algorithm needs to select object that wins paper. Correct answer is rock. Test runs successfully.

TODO: Add few more higher level tests and create simulation runs between different levels. Expectation is that higher level chains should be able to beat lower levels systematicly.
