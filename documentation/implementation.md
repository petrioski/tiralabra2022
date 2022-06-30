# Implementation

This is a rock, paper, scissors game where user can play against computer or let computer play against itself with different settings.

## Algorithm description

Rock, paper, scissors algorithm is implemented as multiAi computer player, which can utilize up to 10 different Markov chains for predicting winning moves and one random generator. Each individual Markov chain uses past $n$ moves of the opponent to make prediction of the next move. Given the past $n$ moves Markov chain uses transition table to deduct most probable next selection and then it will choose object, which beats the expected object. Each won round yields 1 point, loss -1 poit and draw 0 points.

MultiAi manages the group of individual Markov chains and tries to favor the best performing Ai for making next prediction. MultiAi has a so called focus length of $i$. The focus length defines how many previous rounds are taken into consideration when calculating best performing Markov chain. From the last $i$ rounds points are summed up and MultiAi selects the ai with highest points to make next prediction. If human player is succesfully playing against multiAi and all Markov chains are show weak performance as last resource it has a random generator to bring in some unpredictability.

Before any new game user needs to set parameters for AI. One can define the highest degree of Markov chains, focus length and number of rounds to be played. In addition, user can choose if inner logic of multiAi will be shown as printouts.

### Example of multiAi with maximum degree Markov chains

|AI|Example of Past states used|Type|
|--|--|--|
|1|R|Markov Chain (MC) 1. degree|
|2|RP|MC 2. degree|
|3|RPS|MC 3. degree|
|4|RPS R|MC 4. degree|
|5|RPS RP|MC 5. degree|
|6|RPS RPS|MC 6. degree|
|7|RPS RPS R|MC 7. degree|
|8|RPS RPS RP|MC 8. degree|
|9|RPS RPS RPS|MC 9. degree|
|10|RPS RPS RPS R|MC 10. degree|
|11|-|Random selector|

## Program structure

The program is organinized in following folders.

* src
  * ui - holds user interface, user input handling and printouts
  * resources - game rules, artefacts and instructions
  * engine - game engine, handling of rounds and players
  * tests - unittests

### High level class diagram of the program

![class diagram](/documentation/graphs/class_diagram.svg)

## Time and space complexity

* Initialisation of multiAi takes time $O(n^2)$ as all possible compinations are initilized
* The use of game is rather fast as size of dictionary used as transition matrix is rather small, for past moves we collect history in $O(1)$ and loop history for all Markov chains in multiAi in $O(n)$ time, but as $n$ is small (11 at highest) we can say the game playing works basically in $O(1)$ time.

## Imperfections and suggestions for improvement

The future improvements are:

* Voting for equal AIs: if multiple Markov chains have same points, there could voting mechanism for prediction between MCs
* Taking opponent moves into consideration. There could be included Markov chains for taking both own and opponent choice compositions into consideration
* Extension to more complex games. For example, the can be extended to inclded spock, lizard, but I didn't have time to make tests during this sprint (i.e. course deadline). However, project is designed so that new objects can be added to resourses and engine will utilize them automatically.
* Project structure clean up. One could refactor all computer logic (multiAi, markovRPS, simpleRPS) to distinct folder called as logic or ai - for example.

## Links

Here is the link from course pages to the [original introduction of multi AI idea](https://arxiv.org/pdf/2003.06769.pdf)
