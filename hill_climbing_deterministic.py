from  subset_creator import _SubsetCreator
import random
import time
import math

class HillClimbingDeterministic(_SubsetCreator):
    """Hill climbing is a simple optimization algorithm used to find the best possible solution. It always chooses
       the best neighboring solutions."""

    def __init__(self, target_sum, iterations, set_numbers, end_in_optimum = False, display_steps = False):
        """

        :param target_sum: Searched sum of numbers.
        :type target_sum: int
        :param iterations: Number of algorithm executions.
        :type iterations: int
        :param set_numbers: Initial set, from which we create subsets, which we search in order to find a solution.
        :type set_numbers: set
        :param end_in_optimum: The algorithm terminates working when is at the optimum of the function.
        :type end_in_optimum: bool
        :param display_steps: Allows to display the steps that the algorithm performs in order to find
               solutions. Not recommended due to the huge amount of displayed information.
        :type display_steps: bool
        """
        super().__init__(target_sum, iterations, set_numbers)
        self.end_in_optimum = end_in_optimum
        self.display_steps = display_steps

    def search_solution(self):
        """
        The function that search for best solution.

        :return: Best found solution.
        :rtype: list
        """


        start_subset = self.create_start_subset()
        iter_count = 1
        best_subset_points = self.goal_function(start_subset)
        best_solution = []
        best_subset = start_subset.copy()

        if self.display_steps:
                print(f"Iter: {iter_count} start subset: {best_subset} start subset points: "
                      f" {best_subset_points}")

        try:
            while iter_count <= self.iterations:
                best_solution_copy = best_solution.copy()
                neighbors = self.create_neighbours_for_subset(best_subset)
                for neighbor in neighbors:
                    current_subset_points = self.goal_function(neighbor)
                    if current_subset_points <= best_subset_points:
                        best_subset = neighbor
                        best_subset_points = current_subset_points
                    if self.display_steps:
                        print(f"Iter: {iter_count} current subset: {neighbor}, current subset points: "
                                f"{current_subset_points}, best_subset points: {best_subset_points}, "
                                f"best subset: {best_subset}")

                iter_count += 1

                if self.display_steps:
                    print("\n")

                best_solution = self.convert_subset_into_decimal(best_subset)

                if self.end_in_optimum:
                    if best_solution_copy == best_solution:
                        break

            return best_solution

        except TypeError:
            print("TypeError: incorrect type of parameter for HillClimbingDeterministic()")


    def execution_time(self):
        """
        The function that return execution time for search of solution (sec).

        :return: Time execution of search of solution.
        :rtype: str
        """

        start_time = time.time()
        self.search_solution()
        formatted_time = "{:.9f}".format(time.time() - start_time)
        return formatted_time

    def how_algorithm_works(self):
        """
        The function that display description how hill climbing deterministic version works for subset sum problem.
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
        
        2. When we have subset [0, 1, 0, 1, 1] , we can create neighboring solutions 
            (amount of neighbours is always same as length of subset).
           
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
                                  
            so we have nested list which that contains all neighboring solutions.
           
        3. Now we search for best solution in our list of neighbors.
            Every neighbor must be rated, to do it we use formula:
                points = abs(sum_to_find - sum_of_current_neighbor) 
                
            That's mean the best neighboring solution is that with the lowest points (I know it sounds weird).
           
            For example:
            
                Start arguments: main_set = {5, 1, 2, 3, 4} , sum_to_find = 5 
                random subset from which we start the search [0, 1, 0, 1, 1] -> {1, 3, 5} -> points = abs(5 - 9) = 4
                                                             [1, 1, 0, 1, 1] -> {5, 1, 3, 4} -> points = abs(5 - 13) = 8 
                                                             [0, 0, 0, 1, 1] -> {3, 4} -> points = abs(5 - 7) = 2 
                                                             [0, 1, 1, 1, 1] -> {1, 2, 3, 4} -> points = abs(5 - 10) = 5
                                                             [0, 1, 0, 0, 1] -> {1, 4} -> points = abs(5 - 5) = 0 
                                                             [0, 1, 0, 1, 0] -> {1, 3} -> points = abs(5 - 1) = 1 
                                         
                We can see that the best solution is subset with 0 points {1,4} so this is solution, 
                that we exactly needed, so program stops execution.
                
                if we do not find searched solution, is selected neighboring solution with the lowest points
                and we back to point 2 to create new neighboring solution using selected solution.
                The action is performed as many times as we specify iterations.
        """)