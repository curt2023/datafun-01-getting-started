"""

Purpose: Calculate the area of a circle.

Author: Denise Case

This script illustrates importing modules and using constants.

It illustrates the built-in function round().

When we install Python, it comes with the Python standard library.
Nearly all scripts will import at least one module from the standard library.

We can install additional, third-party modules using pip.
We'll do that later. 

All scripts in this repository use only the standard library.

@uses math module for pi constant

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library

import math

# Use the math module's constant for pi
pi = math.pi

# get the total points from the user - input result is always a string
# Use \n to add a blank new line to the terminal before we ask for input
season1_total_points = input("\nEnter the total points for the first season: ")
season2_total_points = input("\nEnter the total points for the second season: ")
number_of_games = input("\nEnter the number of games played ")

#convert string to a number
season1 = int(season1_total_points)
season2 = int(season2_total_points)
games = int(number_of_games)

#minimum and max value formula
minimum = season1  

if season2 < minimum:
    minimum = season2

maximum = season1

if season2 > maximum:
    maximum = season2

#calulate the 
total_points_scored = season1 + season2
average_total_points = (total_points_scored) / games
lowest_season_total = minimum
highest_season_total = maximum

#round average
average_total_points = round(average_total_points)



# log the results
logger.info(f"The total points scored during the two seasons is {total_points_scored}.")
logger.info(f"The average points scored per game is {average_total_points}.")
logger.info(f"The lowest season total is {lowest_season_total}.")
logger.info(f"The highest season total is {highest_season_total}.")



