# import files
from helpers import calculate_score, move, overlap
from algorithms import *

# import files
import random
import copy
import time

# import modules
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import copy

# create map class as distr

X_DIMENSION = 360
Y_DIMENSION = 320

def main(iterations, buildings, map_score):

    best_direction = None
    total_score = map_score
    best_buildings = None

    start_time = time.time()
    print "begin score: ", map_score

    for i in range(iterations):

        building = random.choice(buildings)

        direction = random.randint(-2, 2)

        possible, move_score = check_move(building, buildings, direction)

        if possible and move_score > map_score:
            print 'move score: ', move_score
            map_score = move_score
            best_buildings = copy.deepcopy(buildings)
        else:
            move(building, -direction, 0.5)


    print "%s seconds" % (time.time() - start_time)
    return best_buildings, map_score


def check_move(building, buildings, direction):

    move(building, direction, 0.5)

    if (building.left_bottom[0] < 0) or (building.left_bottom[1] < 0) or (building.right_top[0] > X_DIMENSION) or (building.right_top[1] > Y_DIMENSION):
        return False, 0

    olap = True
    for build in buildings:

        if build == building:
            continue

        olap = overlap(build, building)

        if olap:
            helpers.move(building, -direction, 0.5)
            return False, 0

    if not olap:
        score = calculate_score(buildings)
        return True, score