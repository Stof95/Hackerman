# HEURISTIEKEN
# Project: Amstelhaegen
# Autors: Tim Jansen, Jaap Meesters, Christoffel Doorman

# import files
from helpers import h_build, b_build, m_build, calculate_score
import visualisation

# import modules
import matplotlib.pyplot as plt
import random
import pdb
import numpy as np
import locale
import timeit
import math
import copy

X_DIMENSION = 360
Y_DIMENSION = 320

def main(total_houses, iterations):

    best_iteration = 0

    for i in range(iterations):

        # create buildings array
        buildings = []
        
        # set number of each building type
        h_number = 0.6 * total_houses
        b_number = 0.25 * total_houses
        m_number = 0.15 * total_houses

        # create counters to count number of each building
        h_counter, b_counter, m_counter = 0, 0, 0

        # build houses until maximum is reached
        while len(buildings) < total_houses:

	        # choose random building type
            building_type = random.randint(1, 3)

            if building_type == 1 and h_counter < h_number:
                buildings, h_counter = h_build(buildings, h_counter)

            if building_type == 2 and b_counter < b_number:
                buildings, b_counter = b_build(buildings, b_counter)

            if building_type == 3 and m_counter < m_number:
                buildings, m_counter = m_build(buildings, m_counter)

        # calculate closest distance to buildings
        total_value = calculate_score(buildings)
        print total_value

        if (total_value > best_iteration):
            best_buildings = copy.deepcopy(buildings)
            best_iteration = total_value

	# stop = timeit.default_timer()
	# print "De tijd is: ", stop - start

    return best_buildings, best_iteration