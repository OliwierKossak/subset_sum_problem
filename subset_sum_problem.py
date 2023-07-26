import math
import random
import time

class _SubsetCreator:
    """A class contains functions which that are using to modifying solutions."""

    def __init__(self, target_sum, iterations, set_numbers):
        """

        :param target_sum: Searched sum of numbers.
        :type target_sum: int
        :param set_numbers: Initial set, from which are creating first subsets,
                            which we search in order to find a solution.
        :type set_numbers: set
        :param iterations: Number of algorithm executions.
        :type iterations: int
        """

        self.target_sum = target_sum
        self.iterations = iterations
        self.set_numbers = set_numbers

    def remove_duplicates(self):
        """
        The function that remove duplicate numbers from main set.
        """

        type_of_set = type(self.set_numbers).__name__

        if type_of_set != 'set':
            new_list = []
            try:
                for i in self.set_numbers:
                    if i not in new_list:
                        new_list.append(i)
            except TypeError:
                print("TypeError: incorrect type for 'set_numbers' ")
                self.set_numbers = new_list.copy()


    def create_start_subset(self):
        """
        The function that creates the subset from which start search, subset contains 0 and 1 numbers.

        :return: Subset which contains 0 and 1 numbers.
        :rtype: list
        """

        self.remove_duplicates()
        start_subset = []
        for i in range(len(self.set_numbers)):
            zero_or_one = random.randint(0,1)
            start_subset.append(zero_or_one)

        return start_subset

    def sum_of_subset(self, subset):
        """
        The function that return sum of numbers from subset.

        :param subset: Subset whose elements will be summed.
        :type subset: list
        :return: Sum of numbers of subset.
        :rtype: int
        """

        subset_sum = 0
        main_set_to_list = list(self.set_numbers)
        error_exists = False
        for element in range(len(self.set_numbers)):
            if subset[element] == 1:
                try:
                    subset_sum += main_set_to_list[element]
                except TypeError as e:
                    error_exists = True
                    print("TypeError: incorrect type for 'set_numbers' ")

        if error_exists:
            return None
        else:
            return subset_sum


    def create_neighbours_for_subset(self, subset):
        """
        The function which create neighboring solutions for subset.

        :param subset: Subset from which are creating neighboring solutions
        :type subset: list
        :return: Nested list with neighbouring solutions and current subset
        :rtype: list
        """

        neighbours = []
        neighbours.append(subset)

        for i in range(len(self.set_numbers)):

            new_neighbor = subset.copy()
            if new_neighbor[i] == 0:
                new_neighbor[i] = 1
            else:
                new_neighbor[i] = 0

            neighbours.append(new_neighbor)

        return neighbours

    def goal_function(self, subset):
        """
        The function that evaluates the quality of a given solution (subset).

        :param subset: Evaluated subset.
        :type subset: list
        :return: Solution quality points.
        :rtype: int
        """

        sum_of_subset = self.sum_of_subset(subset)
        try:
            points = abs(self.target_sum - sum_of_subset)
        except TypeError:
            print("TypeError: incorrect type of parameter for HillClimbingDeterministic()")
        else:
            return points

    def convert_subset_into_decimal(self, subset):
        """
        The function that convert binary numbers in subset into decimal numbers.

        :param subset: Subset that will be converted.
        :type subset: list
        :return: Converted subset.
        :rtype: list
        """


        decimal_numbers = []
        main_set_to_list = list(self.set_numbers)
        for element in range(len(self.set_numbers)):
            if subset[element] == 1:
                decimal_numbers.append(main_set_to_list[element])

        return  decimal_numbers

    def display_search_solution_steps(self, iterations, current_subset, current_subset_points,
                                      best_subset, best_subset_points):
        """
        The function that display steps of searching for best solution.

        :param iterations: Loop iterations
        :type iterations: int
        :param current_subset: Neighboring solution that is check
        :type current_subset: list
        :param current_subset_points: Points of current subset
        :type current_subset_points: int
        :param best_subset: Best found solution
        :type best_subset: list
        :param best_subset_points: Points of the best solution
        :type best_subset_points: list
        """
        print(f"Iter: {iterations} current subset: {current_subset}, current subset points: "
                                f"{current_subset_points}, best_subset points: {best_subset_points}, "
                                f"best subset: {best_subset}")



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
        The function that return execution time for search of solution.

        :return: Time execution of search of solution.
        :rtype: str
        """

        start_time = time.time()
        self.search_solution()
        formatted_time = "{:.9f}".format(time.time() - start_time)
        return formatted_time + " sec"

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

class HillClimbingFirstChoice(_SubsetCreator):
    """First-Choice Hill Climbing is an optimization algorithm used to find approximate solutions to optimization
    problems. It is a variant of the traditional hill climbing algorithm that introduces randomness to explore a wider
    search space and avoid getting trapped in local optima. The algorithm starts from random initial solutions
    and iteratively moves towards better solutions, making the first improving move it encounters."""

    def __init__(self, sum_to_find, iterations, set_numbers, display_steps = False, max_neighbor_iterations = 100):
        """

        :param sum: sum of numbers to find.
        :type sum: int
        :param set: initial set from which we create subsets.
        :type set: set
        :param iterations: number of algorithm executions.
        :type iterations: int
        :param display_steps: allows you to display the steps that the algorithm performs in order to find the best.
        possible solution. Not recommended due to the huge amount of displayed information.
        :type display_steps: bool
        :param max_neighbor_iterations: limit the number of attempts for generating neighboring solution.
        :type max_neighbor_iterations: int
        """
        super().__init__(sum_to_find, iterations, set_numbers)
        self.display_steps = display_steps
        self.max_neighbor_iterations = max_neighbor_iterations
        self.is_error = bool

    def _generate_random_neighbor(self, subset):
        """The function that generate random neighboring solution.

        :param subset: subset from which we create neighboring solutions.
        :type subset: list
        :return: random neighboring solution.
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

        :return: best found solution
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
                    print(f"Iter: {iter_count} first neighboring subset: {neighboring_solution}, first neighboring subset points: "
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
                    runing =False
                    break

                if iter_count >= self.iterations:
                    runing_main_loop = False
                    runing = False
                    break

            best_solution = self.convert_subset_into_decimal(best_solution)

        if self.display_steps:
            print("\n")

        return best_solution



    def execution_time(self):
        """
        The function that return execution time of search solution

        :return: time execution of search solution
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

        2. When we have subset [0, 1, 0, 1, 1] , we can create neighbours (amount of neighbours is always same as length
           of subset).
           Neighbor is a subset that have one change of 0 or 1 number from subset 
           (in this case we will change subset [0, 1, 0, 1, 1] ). 

           So first neighbor for [0, 1, 0, 1, 1] is [1, 1, 0, 1, 1], because we change 0 (on x postion [x, 1, 0, 1, 1])
           from [0, 1, 0, 1, 1] to 1 

           The second neighbor is change on next postion from [0, 1, 0, 1, 1], so next neighbor change is:
                [0, 1, 0, 1, 1] -> [0, 0, 0, 1, 1]

                all neighbors for [0, 1, 0, 1, 1]:
                                  [1, 1, 0, 1, 1] -> {5, 1, 3, 4}
                                  [0, 0, 0, 1, 1] -> {3, 4}
                                  [0, 1, 1, 1, 1] -> {1, 2, 3, 4}
                                  [0, 1, 0, 0, 1] -> {1, 4}
                                  [0, 1, 0, 1, 0] -> {1, 3}

           so we have nested list which that contain all neighbors  

        3. Now we search for best solution in our list of neighbors.
           Every neighbor must be rated, to do it we use formula:
           points = abs(sum_to_find - sum_of_current_neighbor) 


        """)

class SimulatedAnnealing(_SubsetCreator):
    """First-Choice Hill Climbing is an optimization algorithm used to find approximate solutions to optimization
    problems. It is a variant of the traditional hill climbing algorithm that introduces randomness to explore a wider
    search space and avoid getting trapped in local optima. The algorithm starts from random initial solutions
    and iteratively moves towards better solutions, making the first improving move it encounters."""

    def __init__(self, sum_to_find, iterations, set_numbers, temperature = 1000, display_steps = False, max_neighbor_iterations = 100):
        """

        :param sum: sum of numbers to find.
        :type sum: int
        :param set: initial set from which we create subsets.
        :type set: set
        :param iterations: number of algorithm executions.
        :type iterations: int
        :param display_steps: allows you to display the steps that the algorithm performs in order to find the best.
        possible solution. Not recommended due to the huge amount of displayed information.
        :type display_steps: bool
        :param max_neighbor_iterations: limit the number of attempts for generating neighboring solution.
        :type max_neighbor_iterations: int
        """
        super().__init__(sum_to_find, iterations, set_numbers)
        self.display_steps = display_steps
        self.max_neighbor_iterations = max_neighbor_iterations
        self.is_error = bool
        self.temperature = temperature

    def _generate_random_neighbor(self, subset):
        """The function that generate random neighboring solution.

        :param subset: subset from which we create neighboring solutions.
        :type subset: list
        :return: random neighboring solution.
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

        :return: best found solution
        :rtype: list
        """


        best_solution = self.create_start_subset()
        best_solution_points = self.goal_function(best_solution)
        neighboring_solution = self._generate_random_neighbor(best_solution)
        neighboring_points = self.goal_function(neighboring_solution)
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
                    runing =False
                    break

                if iter_count >= self.iterations:
                    runing_main_loop = False
                    runing = False
                    break

            best_solution = self.convert_subset_into_decimal(best_solution)

        if self.display_steps:
            print("\n")

        return best_solution



    def execution_time(self):
        """
        The function that return execution time of search solution

        :return: time execution of search solution
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

        2. When we have subset [0, 1, 0, 1, 1] , we can create neighbours (amount of neighbours is always same as length
           of subset).
           Neighbor is a subset that have one change of 0 or 1 number from subset 
           (in this case we will change subset [0, 1, 0, 1, 1] ). 

           So first neighbor for [0, 1, 0, 1, 1] is [1, 1, 0, 1, 1], because we change 0 (on x postion [x, 1, 0, 1, 1])
           from [0, 1, 0, 1, 1] to 1 

           The second neighbor is change on next postion from [0, 1, 0, 1, 1], so next neighbor change is:
                [0, 1, 0, 1, 1] -> [0, 0, 0, 1, 1]

                all neighbors for [0, 1, 0, 1, 1]:
                                  [1, 1, 0, 1, 1] -> {5, 1, 3, 4}
                                  [0, 0, 0, 1, 1] -> {3, 4}
                                  [0, 1, 1, 1, 1] -> {1, 2, 3, 4}
                                  [0, 1, 0, 0, 1] -> {1, 4}
                                  [0, 1, 0, 1, 0] -> {1, 3}

           so we have nested list which that contain all neighbors  

        3. Now we search for best solution in our list of neighbors.
           Every neighbor must be rated, to do it we use formula:
           points = abs(sum_to_find - sum_of_current_neighbor) 


        """)


class SubsetSumChecker:
    """The class is a tool to determine if there is a solution for subset sum problem"""

    def _convert_to_list(self, input_set):
        return list(input_set)
    def _check_solution(self, input_set, target_sum, set_index):
        """

        :param input_set: set of numbers that will be searched
        :type input_set: set
        :param target_sum: searched sum of numbers
        :type target_sum: int
        :param set_index: index of number from input_set
        :type: int
        :return: 'True' if searched sum exists or 'False' if searched sum not exists
        :rtype: bool
        """
        converted_set = self._convert_to_list(input_set)
        if target_sum == 0:
            return True
        if target_sum < 0 or set_index < 0:
            return  False

        return self._check_solution(input_set, target_sum - converted_set[set_index], set_index - 1) or \
               self._check_solution(input_set, target_sum, set_index - 1)

    def subset_sum_exists(self, input_set, target_sum):
        return self._check_solution(input_set, target_sum, len(input_set) - 1)
