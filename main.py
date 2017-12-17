# Minor programmeren: heuristieken
# Group: H@ckerman
# Assignment: Amsterlhaegen
# Authors: Tim Jansen, Jaap Meesters, Christoffel Doorman
#
# This file runs all the algoritms, from input of user

from algorithms import *
from helpers import calculate_score
import visualisation.canvas_visualisation as visualisation

if __name__ == "__main__":

    total_houses = input("Total number of houses?: ")
    water_type = input("Choose your water type? [0: no water], [1: one big pool], [2: two horizontal strokes], [3: two horizontal and two vertical strokes]")

    while total_houses < 7:
        total_houses = input("Choose an integer number greater than 7: ")

    algorithm_choice = input("Which algorithm? [1: random], [2: hillclimber], [3: expanding universe], [4: greedy algorithm], [5: re-using], [6: collapsing universe]: ")

    if algorithm_choice == 1:
        algorithm = "random"
        iterations = input("How many iterations?: ")

        best_district, best_iteration, end_time = random_algorithm.main(total_houses, iterations, water_type)
        visualisation.main(best_district, algorithm, total_houses, best_iteration, end_time, iterations, 0, 0)

    elif algorithm_choice == 2:
        algorithm = "hillclimber"

        choice = input("Which hillclimber method do you want: [1: random], [2: systematic], [3: Move, rotate, swap]")

        iterations = input("How many iterations random first?: ")

        iterations_hill = input("How many iterations for hillclimber: ")

        best_district_random, best_iteration, end_time = random_algorithm.main(total_houses, iterations, water_type)

        if choice == 1:
            variation = "random"

            visualisation.main(best_district_random, algorithm, total_houses, best_iteration, end_time, iterations, variation, "randomfirst")

            best_district_hill, best_map_score, end_time = hillclimber_random.main(iterations_hill, best_district_random, best_iteration, water_type)

        elif choice == 2:
            variation = "systematic"

            visualisation.main(best_district_random, algorithm, total_houses, best_iteration, end_time, iterations, variation, "randomfirst")

            best_district_hill, best_map_score, end_time = hillclimber_algorithm.main(iterations_hill, best_district_random, best_iteration, water_type)

        elif choice == 3:
            variation = "Move_rotate_swap"

            visualisation.main(best_district_random, algorithm, total_houses, best_iteration, end_time, iterations, variation, "randomfirst")

            best_district_hill, best_map_score, end_time = hillclimber_rotate_move_swap.main(iterations_hill, best_district_random, best_iteration, water_type)
            # print best_district_hill.buildings

        visualisation.main(best_district_hill, algorithm, total_houses, best_map_score, end_time, iterations_hill, variation, "result")

    elif algorithm_choice == 3:
        algorithm = "expanding_universe"

        district = expanding_universe.main(total_houses)

        map_score = calculate_score(district.buildings)

        iterations_hill = input("How many iterations for hillclimber: ")

        best_district, total_score, end_time = hillclimber_random.main(iterations_hill, district, map_score, water_type)

        # visualisation.main(buildings, algorithm, total_houses, map_score, False)
        visualisation.main(best_district, algorithm, total_houses, total_score, end_time, iterations_hill, 0, "exp with hill")
        # visualisation.main(buildings, algorithm, total_houses, best_iteration, end_time, iterations)

    elif algorithm_choice == 4:

        algorithm = "try_greedy"

        try_greedy.main(total_houses)

    elif algorithm_choice == 5:

        buildings, value = printen.main()

        choice = input("Which hillclimber method do you want: [1: random], [2: systematic], [3: Move, rotate, swap]")

        iterations_hill = input("How many iterations for hillclimber: ")

        if choice == 1:
            variation = "random"

            best_district_hill, best_map_score, end_time = hillclimber_random.main(iterations_hill, buildings, value)

        elif choice == 2:
            variation = "systematic"

            best_district_hill, best_map_score, end_time = hillclimber_algorithm.main(iterations_hill, buildings, value)

        elif choice == 3:
            variation = "Move_rotate_swap"

            best_district_hill, best_map_score, end_time = hillclimber_rotate_move_swap.main(iterations_hill, buildings, value)

        visualisation.main(best_district_hill.buildings, algorithm, total_houses, best_map_score, end_time, iterations_hill, variation, "result")


    elif algorithm_choice == 6:

        algorithm = "collapsing_universe"

        district = collapsing_universe.main(total_houses)

        map_score = calculate_score(district.buildings)

        iterations_hill = input("How many iterations for hillclimber: ")

        best_district, total_score, end_time = hillclimber_random.main(iterations_hill, district, map_score, 0)

        # visualisation.main(buildings, algorithm, total_houses, map_score, False)
        visualisation.main(best_district, algorithm, total_houses, total_score, end_time, iterations_hill, 0, "collaps with hill")
