#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: November 2019
# This program calculates the area of a triangle when given height and radius
# (pi)r^2h


import math


def calculate(radius, height):
    # find the area with the given inputs and prints the output
    volume = math.pi*radius**2*height

    return volume


def main():
    numcheck_1 = input("enter radius (cm): ")
    numcheck_2 = input("enter height (cm): ")
    try:
        number_1 = int(numcheck_1)
        number_2 = int(numcheck_2)
        if number_1 >= 0 and number_2 >= 0:
            volume = calculate(height=number_2, radius=number_1)
            print("volume = {0:,.2f}³".format(volume))
        else:
            print("invalid input")
    except ValueError:
        print("invalid input")


if __name__ == "__main__":
    main()
