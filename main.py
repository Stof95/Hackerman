import random_algoritm
import expanding_universe


if __name__ == "__main__":

    total_houses = input("Total number of houses?: ")
    algoritm = raw_input("Which algoritm?: ")

    if algoritm == "random":
        iterations = input("How many iterations?: ")

        buildings = random_algoritm.main(total_houses, iterations)

    elif algoritm == "expanding universe":

        expanding_universe.main(total_houses)
