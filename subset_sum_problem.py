import random

class HillClimbingDeterministic:
    """A hill climbing algorithm deterministic version."""

    def __init__(self, sum, iterations, set, display_steps = False):
        """

        :param sum: sum of numbers to find.
        :type sum: int
        :param set: initial set from which we create subsets.
        :type set: set
        :param iterations: number of algorithm executions
        :type iterations: int
        :param display_steps: allows you to display the steps that the algorithm performs in order to find the best
        possible solution. Not recommended due to the huge amount of displayed information
        :type display_steps: bool
        """
        self.sum = sum
        self.iterations = iterations
        self.set = set
        self.display_steps = display_steps

    def _create_start_subset(self):
        """
        The function that creates the subset from which start search, subset contains 0 and 1 numbers

        :return: subset which contains 0 and 1 numbers.
        :rtype: list
        """

        start_subset = []
        for i in range(len(self.set)):
            zero_or_one = random.randint(0,1)
            start_subset.append(zero_or_one)

        return  start_subset

    def _sum_of_subset(self, subset):
        """The function that return sum of numbers from subset

        :param subset: subset that elements will be summed
        :type subset: list
        :return: sum of numbers in subset
        :rtype: int
        """
        subset_sum = 0
        main_set_to_list = list(self.set)
        for element in range(len(self.set)):
            if subset[element] == 1:
                subset_sum += main_set_to_list[element]
        return subset_sum


    def _create_neighbours_for_subset(self, subset):
        """ The function which create neighbours for subset

        :param subset: subset from which we create neighbors
        :type subset: list
        :return: nested list with neighbours and current subset
        :rtype: nested list
        """

        neighbours = []
        neighbours.append(subset)

        for i in range(len(self.set)):

            new_neighbor = subset.copy()
            if new_neighbor[i] == 0:
                new_neighbor[i] = 1
            else:
                new_neighbor[i] = 0

            neighbours.append(new_neighbor)

        return neighbours

    def _goal_function(self, subset):
        """ The function that evaluates the quality of a given solution (subset)

        :param subset: evaluated susbset
        :type subset: list
        :return: solution quality points
        :rtype: int
        """
        sum_of_subset = self._sum_of_subset(subset)
        points = abs(self.sum - sum_of_subset)
        return points

    def _convert_subset_into_decimal(self, subset):
        """The function that convert subset binary numbers into decimal list

        :param subset: subset that will be converted
        :type subset: list
        :return: converted subset
        :rtype: list
        """

        decimal_numbers = []
        main_set_to_list = list(self.set)
        for element in range(len(self.set)):
            if subset[element] == 1:
                decimal_numbers.append(main_set_to_list[element])

        return  decimal_numbers

    def find_solution(self):
        """The function that search for best solution

        :return: best found solution
        :rtype: list
        """

        start_subset = self._create_start_subset()
        iter_count = 1
        current_subset_points = 0
        best_subset_points = self._goal_function(start_subset)
        best_subset = start_subset.copy()

        while iter_count <= self.iterations:
            neighbors = self._create_neighbours_for_subset(best_subset)

            for neighbor in neighbors:
                current_subset_points = self._goal_function(neighbor)
                if current_subset_points <= best_subset_points:
                    best_subset = neighbor
                    best_subset_points = current_subset_points
                if self.display_steps:
                    print(f"Iter: {iter_count} current subset: {neighbor}, current subset points: {current_subset_points}, best_subset points: {best_subset_points}, best subset: {best_subset}")

            iter_count += 1
            if self.display_steps:
                print("\n")

        best_solution = self._convert_subset_into_decimal(best_subset)
        return best_solution







set = {1,2,3,4,5,6,-2,7,-10}

hill = HillClimbingDeterministic(4, 8, set, True)
print(hill.find_solution())

