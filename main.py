'''
Packagifying and importing evo_search classes

Justin Slattery
June 2023
'''
from es import EvoSearch
import numpy as np

# Test Array for Evo Search
test_arr = np.zeros((2,2))
print(test_arr)

# Need to set up the functions so that they can either:
# 1. take a preset data structure or
# 2. take an ambiguous structure and parse it (list, np array, dict?)
# 3. take a preset data structure with agents with genotypes


def fitness_function(obj):
    pass

evo_params = {
        'pop_size' : 100,    # population size
        'genotype_size': 10, # dimensionality of solution
        'fitness_function': fitness_function, # custom function defined to evaluate fitness of a solution
        'elitist_fraction': 0.04, # fraction of population retained as is between generations
        'mutation_variance': 0.05 # mutation noise added to offspring.
    }

es = EvoSearch(evo_params)

