import random

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
