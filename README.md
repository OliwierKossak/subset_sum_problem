# Implementation of space search algorithms to find a solution to the subset sum problem. 

## Subset sum problem definiton:

The **SUBSET-SUM** problem involves determining whether or not a subset from a list of integers can sum to a target value. For example, consider the list of nums = [1, 2, 3, 4]. If the target = 7, there are two subsets that achieve this sum: {3, 4} and {1, 2, 4}. If target = 11, there are no solutions.

### Algorithms used to find solution:

1. Hill climbing deterministic - Hill climbing is a local search algorithm that starts with an arbitrary solution to a problem and iteratively makes small moves toward a better solution. In the deterministic version of hill climbing, the algorithm always chooses the best available move.
   
2. Hill climbing first choice - Hill climbing with the first-choice strategy is a variation of the basic hill climbing algorithm. In this strategy, instead of examining all neighboring solutions and then selecting the best one, the algorithm selects the first neighboring solution that improves upon the current solution.
   
3. Simulated annealing - Simulated Annealing is a probabilistic optimization algorithm inspired by the annealing process in metallurgy, where a material is heated to a high temperature and then gradually cooled to remove defects, reducing its energy and increasing its overall quality. In optimization, it's used to find an approximate solution to an optimization problem, particularly in cases where a global optimum is sought, and the search space is complex.
   
4. Genetic algorithm - A Genetic Algorithm (GA) is a heuristic optimization algorithm inspired by the process of natural selection and genetics. It's often used for optimization and search problems where traditional algorithms may be impractical. The algorithm works by maintaining a population of potential solutions and evolving them over successive generations.

### Starting the program:

**input data:**
the sum of the set that are being searched for = 5000
number of algorithm iterations = 100
the size of the starting set that is searched for in order to find a solution = 1000 of numbers generate in range -1000 to 1000
* genetic algoritm population size = 8 individuals

### Result of running the program:

**time of execution:**

hill climbing deterministic: 6.666187286sec

hill climbing first choice: 0.020288706sec

simulated annealing: 0.022834539sec

genetic algorithm: 0.629482269sec

![untitled](https://github.com/OliwierKossak/subset_sum_problem/assets/138603416/a67dfece-6313-410f-a531-ed3cc3ab4fc8)

**sum of numbers in best found set:**

hill climbing deterministic sum of the found solution: 5001

hill climbing first choice sum of the found solution: 5002

simulated annealing sum of the found solution: 5000

genetic algorithm sum of the found solution: 5761

![untitled(1)](https://github.com/OliwierKossak/subset_sum_problem/assets/138603416/8889b8db-294d-4dc8-ba93-b3782a8b22c5)

### Conclusions:
Hill climbing deterministic is algorithm with highest time of execution. Considering the execution time of other algorithms, using this solution does not seem to be a good idea however, the provided solution is very good, only one value away from the one are looking for. In my opinion, taking into account the execution time and the solution found, I would choose simulated annealing  as the most optimal.


