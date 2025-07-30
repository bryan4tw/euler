# lattice paths
import timeit
import math

# logic
# go as far right as possible, then go down
# then go x-1 right, then down, and right 1
# then go x-2 right, then down, and right 2
#
# no movement can happen on any of the spaces
# that we've passed over so they can be ignored from the search space.
#
# in a 20x20 grid, there are 40 decisions, but only 20 can be down, and 20 can be right
# This is really a how many ways can you arrange 20 R's and 20 D's
# The answer is 40! / (20! * 20!)

print(
    f"Calculating number of lattice paths in a 20x20 grid...{math.factorial(40) // (math.factorial(20) * math.factorial(20))}"
)
