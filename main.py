from hill_climbing_deterministic import HillClimbingDeterministic
from hill_climbing_first_choice import HillClimbingFirstChoice
from simulated_annealing import SimulatedAnnealing
from genetic_algorithm import GeneticAlgorithm
import random
from matplotlib import pyplot

random_numbers_list = []
target_sum = 5000
iterations = 100

for i in range(1000):
    random_number = random.randint(-1000, 1000)
    random_numbers_list.append(random_number)


hill_deter = HillClimbingDeterministic(target_sum, iterations, random_numbers_list)
hill_first_choice = HillClimbingFirstChoice(target_sum, iterations, random_numbers_list)
simulated_annealing = SimulatedAnnealing(target_sum, iterations, random_numbers_list)
genetic_alg = GeneticAlgorithm(target_sum, iterations, random_numbers_list, 8)

hill_dtr_time = hill_deter.execution_time()
hill_first_time = hill_first_choice.execution_time()
simulated_ann_time = simulated_annealing.execution_time()
genetic_time = genetic_alg.execution_time()

execution_time = [float(hill_dtr_time), float(hill_first_time), float(simulated_ann_time), float(genetic_time)]
algorithms = ["hill climbing deterministic", "hill climbing first choice", "simulated annealing", "genetic algorithm"]

print(f'{algorithms[0]}: {execution_time[0]}sec')
print(f'{algorithms[1]}: {execution_time[1]}sec')
print(f'{algorithms[2]}: {execution_time[2]}sec')
print(f'{algorithms[3]}: {execution_time[3]}sec')
print()

hill_dtr_solution_sum = sum(hill_deter.search_solution())
hill_first_solution_sum = sum(hill_first_choice.search_solution())
simulated_annealing_solution_sum = sum(simulated_annealing.search_solution())
genetic_solution_sum = sum(genetic_alg.search_for_best_individual())

solutions_sum = [hill_dtr_solution_sum, hill_first_solution_sum, simulated_annealing_solution_sum, genetic_solution_sum]
print(f'{algorithms[0]} sum of the found solution: {hill_dtr_solution_sum}')
print(f'{algorithms[1]} sum of the found solution: {hill_first_solution_sum}')
print(f'{algorithms[2]} sum of the found solution: {simulated_annealing_solution_sum}')
print(f'{algorithms[3]} sum of the found solution: {genetic_solution_sum}')

pyplot.bar(algorithms, execution_time, width=0.4)
pyplot.xticks(rotation=15)
pyplot.ylabel("execution time (sec)")
pyplot.show()


pyplot.bar(algorithms, solutions_sum, width=0.4)
pyplot.xticks(rotation=15)
pyplot.ylabel("sum of best found set")
pyplot.show()





