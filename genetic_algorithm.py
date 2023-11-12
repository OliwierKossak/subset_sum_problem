import random
import time
from subset_creator import _SubsetCreator

class GeneticAlgorithm(_SubsetCreator):

    def __init__(self, target_sum, iterations, set_numbers, start_population_size):
        super().__init__(target_sum, iterations, set_numbers)
        self.start_population_size = start_population_size


    def create_start_population(self):
        population = []
        for i in range(self.start_population_size):
            individual = self.create_start_subset()
            population.append(individual)

        return population

    def fitness(self, population):
        rating = []
        for i in range(len(population)):
            sum = 0
            points = 0
            for j in range(len(population[i])):
                if population[i][j] == 1:
                    sum += self.set_numbers[j]

            points = abs(sum - self.target_sum)
            rating.append(points)

        return rating

    def rescaling_rating(self, rating):
        sum_rating = sum(rating)
        new_rating = []
        for i in range(len(rating)):
            new_rating.append(sum_rating-rating[i])

        return new_rating
    def roulette_selection(self, population):
        new_population = []
        rating = self.fitness(population)
        rescaled_rating = self.rescaling_rating(rating)
        population_points = sum(rescaled_rating)

        for i in range(len(population)):
            random_individual_number = random.randint(0, population_points)
            points_sum = 0
            index = 0
            while True:
                points_sum += rescaled_rating[index]
                if 0 <= random_individual_number <= points_sum:
                    new_population.append(population[index])
                    break
                else:
                    index += 1

        return new_population

    def crossbreeding_population(self, new_population):
        crossbreeding_population = []
        for i in range(0, len(new_population), 2):
            first_parent = new_population[i]
            second_parent = new_population[i + 1]
            divider = random.randint(1, len(first_parent)-1)
            first_child = first_parent[:divider] + second_parent[divider:]
            second_child = second_parent[:divider] + first_parent[divider:]
            crossbreeding_population.append(first_child)
            crossbreeding_population.append(second_child)
        return crossbreeding_population

    def mutation(self, population, probability):
        for i in range(len(population)):
            for j in range(len(population[i])):
                number = random.randint(0, probability)
                if number == 0 and population[i][j] == 1:
                    population[i][j] = 0
                elif number == 0 and population[i][j] == 0:
                    population[i][j] = 1

        return population

    def search_solution(self):

        start_population = self.create_start_population()
        selected_population = self.roulette_selection(start_population)
        crossed_population = self.crossbreeding_population(selected_population)
        mutated_population = self.mutation(crossed_population, 100)
        new_population = mutated_population
        for i in range(self.iterations):
            new_selected_population = self.roulette_selection(new_population)
            new_crossed_population = self.crossbreeding_population(new_selected_population)
            new_mutated_population = self.mutation(new_crossed_population, 100)
            new_population = new_mutated_population
        return new_population

    def search_for_best_individual(self):
        population = self.search_solution()
        best_individual_index = 0

        for i in range(len(population) - 1):
            assessment_new = abs(sum(population[i+1]) - self.target_sum)
            assessment_best = abs(sum(population[best_individual_index]) - self.target_sum)
            if assessment_new < assessment_best:
                best_individual_index = i

        return population[i]

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












