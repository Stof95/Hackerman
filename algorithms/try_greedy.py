# import files
from helpers import h_build, b_build, m_build, calculate_score
import visualisation
import visualisation.canvas_visualisation as visualisation

# import modules
import matplotlib.pyplot as plt
import random
import pdb
import numpy as np
import locale
import timeit
import math
import copy
import classes
import time
import helpers

X_DIMENSION = 360
Y_DIMENSION = 320

def main(total_houses):
    buildings = []

    # set number of each building type
    h_number = 0.6 * total_houses
    b_number = 0.25 * total_houses
    m_number = 0.15 * total_houses

    m_counter = 1
    b_counter, h_counter = 0, 0

    top_value = 0
    best_x = 0
    best_y = 0


    # bouw het eerste huis random, een maison wat die heeft de meeste waarde
    buildings, m_counter = m_build(buildings, m_counter)

    plaatje(buildings)


    while (m_counter < m_number):
        top_value = 0
        best_x = 0
        best_y = 0

        print("Maison:{}".format(m_counter + 1))
        print("")

        maison, buildings = build(buildings, classes.Maison)
        top_value, best_x, best_y = walk_check(maison, buildings, top_value, best_x, best_y)
        move_to_best(maison, best_x, best_y)
        m_counter += 1
        plaatje(buildings)

        print("best: {}: {},{}".format(top_value, best_x, best_y))
        print("")

    while (b_counter < b_number):
        top_value = 0
        best_x = 0
        best_y = 0

        print("Bungalow:{}".format(b_counter + 1))
        print("")

        bungalow, buildings = build(buildings, classes.Bungalow)
        top_value, best_x, best_y = walk_check(bungalow, buildings, top_value, best_x, best_y)
        move_to_best(bungalow, best_x, best_y)
        b_counter += 1
        plaatje(buildings)

        print("best: {}: {},{}".format(top_value, best_x, best_y))
        print("")

    plaatje(buildings)


def plaatje(buildings):
    visualisation.print_canvas(buildings, 'try_greedy')

def check_value(buildings, edifice, top_value, best_x, best_y):

    for building in buildings:
        overlapping = helpers.overlap(edifice,building)

        if overlapping:
            print("overlapping {},{} : {},{}".format(edifice.left_bottom[0], edifice.left_bottom[1], building.left_bottom[0], building.left_bottom[0]))
            return top_value, best_x, best_y
            break

        if not overlapping:
            print("NOT         {},{} : {},{}".format(edifice.left_bottom[0], edifice.left_bottom[1], building.left_bottom[0], building.left_bottom[0]))
            value = helpers.calculate_score(buildings)

            if value > top_value:
                top_value = value
                best_x = edifice.left_bottom[0]
                best_y = edifice.left_bottom[1]
                #print top_value, best_x, best_y

    return top_value, best_x, best_y

def build(buildings, edifice):
    # bouw het huis in de linker onderhoek,
    edifice = edifice(0,0)
    buildings.append(edifice)

    return edifice, buildings

def walk_check(edifice, buildings, top_value, best_x, best_y):

    # zet direction op: naar rechts lopen
    direction = '1'

    # begin met lopen
    while True:
        helpers.move(edifice, direction, 1)
        top_value, best_x, best_y = check_value(buildings, edifice, top_value, best_x, best_y)

        if edifice.right_top[0] == 360:
            helpers.move(edifice, '2', 1)
            top_value, best_x, best_y = check_value(buildings, edifice, top_value, best_x, best_y)
            helpers.move(edifice, '-1', 1)
            top_value, best_x, best_y = check_value(buildings, edifice, top_value, best_x, best_y)
            direction = '-1'

        if edifice.left_bottom[0] == 0:
            helpers.move(edifice, '2', 1)
            top_value, best_x, best_y = check_value(buildings, edifice, top_value, best_x, best_y)
            helpers.move(edifice, '1', 1)
            top_value, best_x, best_y = check_value(buildings, edifice, top_value, best_x, best_y)
            direction = '1'

        # bij 360, pakt hij hem niet. Later naar kijken, voor nu 359
        if edifice.left_top[1] == 320 and edifice.right_bottom[0] == 359:
            break

    return top_value, best_x, best_y

def move_to_best(edifice, best_x, best_y):
    edifice.left_bottom[0] = best_x
    edifice.left_bottom[1] = best_y
