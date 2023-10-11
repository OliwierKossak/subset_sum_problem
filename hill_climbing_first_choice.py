from  subset_creator import _SubsetCreator
import random
import time
import math

class HillClimbingFirstChoice(_SubsetCreator):
    """First-Choice Hill Climbing is an optimization algorithm used to find approximate solutions to optimization
    problems. It is a variant of the traditional hill climbing algorithm that introduces randomness to explore a wider
    search space and avoid getting trapped in local optima. The algorithm starts from random initial solutions
    and iteratively moves towards better solutions, making the first improving move it encounters."""

    def __init__(self, target_sum, iterations, set_numbers, display_steps = False, max_neighbor_iterations = 100):
        """

        :param target_sum: Searched sum of numbers.
        :type target_sum: int
        :param set_numbers: Initial set, from which we create subsets, which we search in order to find a solution.
        :type set_numbers: set
        :param iterations: Number of algorithm executions.
        :type iterations: int
        :param display_steps: Allows to display the steps that the algorithm performs in order to find
                              solutions. Not recommended due to the huge amount of displayed information.
        :type display_steps: bool
        :param max_neighbor_iterations: Limit the number of attempts for generating neighboring solution.
        :type max_neighbor_iterations: int
        """
        super().__init__(target_sum, iterations, set_numbers)
        self.display_steps = display_steps
        self.max_neighbor_iterations = max_neighbor_iterations
        self.is_error = bool

    def _generate_random_neighbor(self, subset):
        """
        The function that generate random neighboring solution.

        :param subset: Subset from which we create neighboring solutions.
        :type subset: list
        :return: Random neighboring solution.
        :rtype: list
        """

        neighbour_solution = subset.copy()


        change_index = random.randint(0, len(subset)-1)
        if neighbour_solution[change_index] == 0:
           neighbour_solution[change_index] = 1
        else:
            neighbour_solution[change_index] = 0
        return neighbour_solution
    def search_solution(self):
        """
        The function that search for best solution.

        :return: Best found solution.
        :rtype: list
        """


        best_solution = self.create_start_subset()
        best_solution_points = self.goal_function(best_solution)
        neighboring_solution = self._generate_random_neighbor(best_solution)
        neighboring_points = self.goal_function(neighboring_solution)
        iter_count = 1
        neighboring_generator_count = 1
        runing_main_loop = True

        if self.display_steps:
                    print(f"Iter: {iter_count} first neighboring subset: {neighboring_solution}, "
                          f"first neighboring subset points: "
                          f"{neighboring_points}, first subset points: {best_solution_points}, "
                          f"first subset: {best_solution}")

        while runing_main_loop:
            runing = True
            while runing:

                if best_solution_points == 0:
                    runing_main_loop = False
                    break

                elif neighboring_points < best_solution_points:
                    best_solution = neighboring_solution
                    best_solution_points = neighboring_points
                    neighboring_solution = self._generate_random_neighbor(best_solution)
                    neighboring_points = self.goal_function(neighboring_solution)
                    neighboring_generator_count = 1
                    iter_count += 1
                    if self.display_steps:
                        print("\n")

                else:
                    neighboring_solution = self._generate_random_neighbor(best_solution)
                    neighboring_points = self.goal_function(neighboring_solution)
                    neighboring_generator_count += 1

                if self.display_steps:
                    self.display_search_solution_steps(iter_count, neighboring_solution, neighboring_points,
                                                       best_solution, best_solution_points)


                if neighboring_generator_count >= self.max_neighbor_iterations:
                    runing_main_loop = False
                    break

                if iter_count >= self.iterations:
                    runing_main_loop = False
                    break

            best_solution = self.convert_subset_into_decimal(best_solution)

        if self.display_steps:
            print("\n")

        return best_solution



    def execution_time(self):
        """
        The function that return execution time of search for solution (sec).

        :return: Time execution of search of solution.
        :rtype: str
        """
        start_time = time.time()
        self.search_solution()
        formatted_time = "{:.9f}".format(time.time() - start_time)
        return formatted_time

    def how_algorithm_works(self):
        """
        The function that display description how hill climbing first choice works for subset sum problem.

        """
        print("""
        Start arguments: main_set = {5, 1, 2, 3, 4} , sum_to_find = 5
        
        All duplicates of numbers are removing from main set!!!!
        
        1. We create first subset which contains random 0 and 1 numbers, for example [0, 1, 0, 1, 1] 
            (list have always same length as 'main_set').
            [0, 1, 0, 1, 1] is the subset from which the computation will start. 
           
            What does 0 and 1 numbers means ?
           
                1 is information for algorithm that number will be taken for our computation.
                0 is information for algorithm that number will not be taken for our computation.
                That's mean subset [0, 1, 0, 1, 1] contains decimal numbers [1, 3, 4], because:
                
                {5, 1, 2, 3, 4}
                [0, 1, 0, 1, 1]  = [1, 3, 4]
        
        2. When we have subset [0, 1, 0, 1, 1] , we can create random neighboring solution.
           
            Neighboring solution is a subset that have one change of 0 or 1 number from original subset. 
            (in this case we modify subset [0, 1, 0, 1, 1] ). 
           
            So first neighboring solution for [0, 1, 0, 1, 1] is [1, 1, 0, 1, 1], 
            because we change 0 (on x position [x, 1, 0, 1, 1]) from [0, 1, 0, 1, 1] to 1 
           
            The second neighboring solution is change on next position from [0, 1, 0, 1, 1], so next neighbor change is:
                [0, 1, 0, 1, 1] -> [0, 0, 0, 1, 1]
                
                all neighboring solutions for [0, 1, 0, 1, 1]:
                                              [1, 1, 0, 1, 1] -> {5, 1, 3, 4}
                                              [0, 0, 0, 1, 1] -> {3, 4}
                                              [0, 1, 1, 1, 1] -> {1, 2, 3, 4}
                                              [0, 1, 0, 0, 1] -> {1, 4}
                                              [0, 1, 0, 1, 0] -> {1, 3}
                                  
           
        3. Now we check that if the random created solution is better than original solution.
            neighboring solution must be rated, to do it we use formula:
                points = abs(sum_to_find - sum_of_current_neighbor) 
                
            That's mean better neighboring solution is that with lower points than original solution 
            (I know that's sounds weird).
           
            For example:
            
                Start arguments: main_set = {5, 1, 2, 3, 4} , sum_to_find = 5 
                random subset from which we start the search: 
                                                             [0, 1, 0, 1, 1] -> {1, 3, 5} -> points = abs(5 - 9) = 4
                
                First random neighboring solution:
                                                             [1, 1, 0, 1, 1] -> {5, 1, 3, 4} -> points = abs(5 - 13) = 8 
                                                             
                We can see that solution is worse that original solution, so in this case, the neighboring solution
                is created again.
                
                Next neighboring solution:
                                                             [0, 1, 0, 1, 0] -> {1, 3} -> points = abs(5 - 1) = 1 
                             
                We can see that solution is subset with 1 points {1,3} so this is better than solution than before,
                and we back to point 2 to create new neighboring solution using new solution.
                The action is performed as many times as we specify iterations. 
                
                But what if we not find better ?
                    
                    In this case program have default parameter max_neighbor_iterations = 100, that's means
                    program will terminate when in one loop iterations the random solution will be created 100 times. 
        """)