'''
Contains the np based evolutionary search class
with flexible variable inputs and built-in value checks
to assure speedy by default and customization as needed

Justin Slattery
June 2023
'''

import numpy as np

class EvoSearch:
    def __init__(self,evo_params):
        '''
        Initialize evolutionary search
        ARGS:
        evo_params: dict
            required keys -
                pop_size: int - population size,
                genotype_size: int - genotype_size,
                fitness_function: function - a user-defined function that takes a genotype as arg and returns a float fitness value
                elitist_fraction: float - fraction of top performing individuals to retain for next generation
                mutation_variance: float - variance of the gaussian distribution used for mutation noise
            optional keys -
                fitness_args: list-like - optional additional arguments to pass while calling fitness function
                                           list such that len(list) == 1 or len(list) == pop_size
        '''
        # check for required keys
        required_keys = ['pop_size','genotype_size','fitness_function','elitist_fraction','mutation_variance']
        for key in required_keys:
            if key not in evo_params.keys():
                raise Exception('Argument evo_params does not contain the following required key: '+key)

            # checked for all required keys
        self.pop_size = evo_params['pop_size']
        self.genotype_size = evo_params['genotype_size']
        self.fitness_function = evo_params['fitness_function']
        self.elitist_fraction = evo_params['elitist_fraction']
        self.mutation_variance = evo_params['mutation_variance']

        # # validating fitness function
        # assert self.fitness_function,"Invalid fitness_function"
        # rand_genotype = np.random.rand(self.genotype_size)
        # rand_genotype_fitness = self.fitness_function(rand_genotype)
        # assert type(rand_genotype_fitness) == type(0.) or type(rand_genotype_fitness) in np.sctypes['float'],\
        #        "Invalid return type for fitness_function. Should be float or np.dtype('np.float*')"

        # # create other required data
        # self.num_processes = evo_params.get('num_processes',None)
        # self.pop = np.random.rand(self.pop_size,self.genotype_size)
        # self.fitness = np.zeros(self.pop_size)
        # self.num_batches = int(self.pop_size/self.num_processes)
        # self.num_remainder = int(self.pop_size%self.num_processes)

        # # check for fitness function kwargs
        # if 'fitness_args' in evo_params.keys():
        #     optional_args = evo_params['fitness_args']
        #     assert len(optional_args) == 1 or len(optional_args) == self.pop_size,\
        #             "fitness args should be length 1 or pop_size."
        #     self.optional_args = optional_args
        # else:
        #     self.optional_args = None

        # Steps to fill out
        # 1. Pull in the fitness function; identify object
        # 2. Find most fit individual
        # 3. If elitism is selected, slice elites
        # 4. If mutation is selected, select and mutate agents/objects
        # 5. Step through generations
        # 6. Track fitness, best individuals, fitness variance, etc.
        # 7. At gen_end, get max fitness and best individual