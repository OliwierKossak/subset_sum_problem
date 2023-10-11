from hill_climbing_deterministic import HillClimbingDeterministic
from hill_climbing_first_choice import HillClimbingFirstChoice
from simulated_annealing import SimulatedAnnealing
import random
from matplotlib import pyplot

random_numbers_list = []

for i in range(1000):
    random_number = random.randint(-1000, 1000)
    random_numbers_list.append(random_number)


hill_deter = HillClimbingDeterministic(5020, 200, random_numbers_list)
hill_first_choice = HillClimbingFirstChoice(5020, 200, random_numbers_list)
simulated_annealing = SimulatedAnnealing(5020, 200, random_numbers_list)

x = hill_deter.execution_time()
y = hill_first_choice.execution_time()
z = simulated_annealing.execution_time()

print(x)
print(y)
print(z)

execution_time = [float(x), float(y), float(z)]
algorithms = ["hill climbing deterministic", "hill climbing first choice", "simulated annealing"]


pyplot.bar(algorithms, execution_time, width=0.4)
pyplot.ylabel("execution time (sec)")
pyplot.show()



