### Implementation of space search algorithms to find a solution to the subset sum problem. 

## Subset sum problem definiton:
The **SUBSET-SUM** problem involves determining whether or not a subset from a list of integers can sum to a target value. For example, consider the list of nums = [1, 2, 3, 4]. If the target = 7, there are two subsets that achieve this sum: {3, 4} and {1, 2, 4}. If target = 11, there are no solutions.

## Algorithms used to find solution:

1. Hill climbing deterministic - Hill climbing is a local search algorithm that starts with an arbitrary solution to a problem and iteratively makes small moves toward a better solution. In the deterministic version of hill climbing, the algorithm always chooses the best available move.
   
2. Hill climbing first choice - Hill climbing with the first-choice strategy is a variation of the basic hill climbing algorithm. In this strategy, instead of examining all neighboring solutions and then selecting the best one, the algorithm selects the first neighboring solution that improves upon the current solution.
   
3. Simulated annealing - Simulated Annealing is a probabilistic optimization algorithm inspired by the annealing process in metallurgy, where a material is heated to a high temperature and then gradually cooled to remove defects, reducing its energy and increasing its overall quality. In optimization, it's used to find an approximate solution to an optimization problem, particularly in cases where a global optimum is sought, and the search space is complex.
   
4. Genetic algorithm - A Genetic Algorithm (GA) is a heuristic optimization algorithm inspired by the process of natural selection and genetics. It's often used for optimization and search problems where traditional algorithms may be impractical. The algorithm works by maintaining a population of potential solutions and evolving them over successive generations.
               
                                                            
