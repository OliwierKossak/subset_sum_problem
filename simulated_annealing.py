from  subset_creator import _SubsetCreator
import random
import time
import math

class SimulatedAnnealing(_SubsetCreator):
    """Simulated Annealing is a probabilistic optimization algorithm inspired by the annealing process in metallurgy."""

    def __init__(self, target_sum, iterations, set_numbers, temperature = 1000, display_steps = False, max_neighbor_iterations = 100):
        """
        :param target_sum: Searched sum of numbers.
        :type target_sum: int
        :param iterations: Number of algorithm executions.
        :type iterations: int
        :param set_numbers: Initial set, from which we create subsets, which we search in order to find a solution.
        :type set_numbers: set
        :param temperature: The initial temperature of annealing process,
                            controlling probability of accepting worse solution.
        :type temperature: int
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
        self.temperature = temperature

    def _generate_random_neighbor(self, subset):
        """The function that generate random neighboring solution.

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
        global_best_solution = best_solution.copy()
        global_best_solution_points = best_solution_points
        iter_count = 1
        neighboring_generator_count = 1
        runing_main_loop = True
        temperature_change = lambda t: self.temperature / t

        if self.display_steps:
                    print(f"Iter: {iter_count} first neighboring subset: {neighboring_solution}, first neighboring subset points: "
                            f"{neighboring_points}, first subset points: {best_solution_points}, "
                            f"first subset: {best_solution}")

        while runing_main_loop:
            runing = True
            while runing:
                number_between_zero_one = random.uniform(0, 1)

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
                elif number_between_zero_one < math.exp(-abs(neighboring_points - best_solution_points)/
                                                        temperature_change(iter_count)):
                    best_solution = neighboring_solution
                    best_solution_points = neighboring_points
                    neighboring_generator_count = 1
                    iter_count += 1
                    neighboring_solution = self._generate_random_neighbor(best_solution)
                    neighboring_points = self.goal_function(neighboring_solution)
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

                if global_best_solution_points > best_solution_points:
                    global_best_solution_points = best_solution_points
                    global_best_solution = best_solution


        if self.display_steps:
            print("\n")

        global_best_solution_converted = self.convert_subset_into_decimal(global_best_solution)

        return global_best_solution_converted



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
        The function that display information how hill climbing deterministic version works for subset sum problem
        """
        pass