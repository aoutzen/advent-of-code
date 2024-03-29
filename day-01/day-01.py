# --- Day 1: The Tyranny of the Rocket Equation ---

# Santa has become stranded at the edge of the Solar System while delivering presents to other 
# planets! To accurately calculate his position in space, safely align his warp drive, and 
# return to Earth in time to save Christmas, he needs you to bring him measurements from 
# fifty stars.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent 
# calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star.
# Good luck!

# The Elves quickly load you into a spacecraft and prepare to launch.

# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't
# determined the amount of fuel required yet.

# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel
# required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:

#     For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
#     For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel 
#     required is also 2.
#     For a mass of 1969, the fuel required is 654.
#     For a mass of 100756, the fuel required is 33583.

# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually
# calculate the fuel needed for the mass of each module (your puzzle input), then add together
# all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?

import os

def open_file_from_same_directory(filename):
    cur_dir = os.path.dirname(__file__)
    input_path = os.path.join(cur_dir, filename)
    input_file = open(input_path)
    return input_file

def calculate_fuel_req_rec(mass):
    curr_mass_fuel_req = int(mass / 3) - 2
    if curr_mass_fuel_req <= 0:
        return 0
    else:
        return curr_mass_fuel_req + calculate_fuel_req_rec(curr_mass_fuel_req)

def calculate_total_fuel_req(input_file_name):
    input_file = open_file_from_same_directory(input_file_name)
    total_fuel = 0
    for line in input_file:
        mass = float(line.strip())
        total_fuel += calculate_fuel_req_rec(mass)
    
    return total_fuel

print("Total inputs for the Fuel Counter-Upper: " + str(calculate_total_fuel_req("day-01-input.txt")))