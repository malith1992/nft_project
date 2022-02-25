import random
from pprint import pprint
from pandas import *
import numpy as np
import pathway_creator
import building_creator
#import building_counter

import itertools

"""
"horizontal_road" = "hrd"
"vertical_road" = "vrd"
"horizontal_river" = "hrv"
"vertical_river" = "vrv"
"horizontal metro" = "hmt"
"vertical metro" = "vmt"

"horizontal_bridge" = "hbd"
"vertical_bridge" = "vbd"
"river_cross" = "rvc"
"road cross" = "rdc"
"metro cross" = "mtc"
 """
# [identifier,columns,rows] = a32 = building a with 3 columns and 2 row (3x2)
# [identifier,columns,rows] = a12 = building a with 1 column and 2 rows (1x2)

one_by_one = ["a11", "b11", "c11", "d11", "e11", "f11", "g11", "h11", "i11", "j11", "k11", "l11", "m11", "n11", "o11",
              "p11", "q11", "r11", "s11", "t11", "u11", "v11", "w11", "x11", "y11", "z11"]
weights1 = [100, 100, 100, 100, 100, 80, 80, 80, 80, 80, 50, 50, 50, 50, 50,
            30, 30, 30, 30, 30, 20, 20, 20, 20, 20, 20]
one_by_two = ["a12", "b12", "c12", "d12", "e12", "f12", "g12", "h12", "i12", "j12", "k12", "l12", "m12", "n12", "o12"]
weights2 = [70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 50, 50, 50, 50, 50]
two_by_one = ["a21", "b21", "c21", "d21", "e21", "f21", "g21", "h21", "i21", "j21", "k21", "l21", "m21", "n21", "o21"]
weights3 = [70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 50, 50, 50, 50, 50]
two_by_two = ["a22", "b22", "c22", "d22", "e22"]
weights4 = [50, 50, 50, 50, 50]
two_by_three = ["a23", "b23", "c23", "d23", "e23"]
weights5 = [20, 20, 20, 20, 20]
three_by_two = ["a32", "b32", "c32", "d32", "e32"]
weights6 = [20, 20, 20, 20, 20]

buildings = one_by_one + one_by_two + two_by_one + two_by_two + two_by_three + three_by_two
building_weights = weights1 + weights2 + weights3 + weights4 + weights5 + weights6

number = [0, 1, 2, 3, 4, 5, 6, 7]
number_weights = [10, 10, 10, 10, 10, 10, 10, 10]

side = ["column", "row"]
side_weights = [50, 50]

pathway = ["road", "river", "metro"]
pathway_weights = [30, 30, 30]


# grid = np.indices((8, 8))[0]

def create_new_grid(duplicate_count):
    grid = [
        ["000", "000", "000", "000", "000", "000", "000", "000"],
        ["000", "000", "000", "000", "000", "000", "000", "000"],
        ["000", "000", "000", "000", "000", "000", "000", "000"],
        ["000", "000", "000", "000", "000", "000", "000", "000"],
        ["000", "000", "000", "000", "000", "000", "000", "000"],
        ["000", "000", "000", "000", "000", "000", "000", "000"],
        ["000", "000", "000", "000", "000", "000", "000", "000"],
        ["000", "000", "000", "000", "000", "000", "000", "000"]
    ]

    buildings = one_by_one + one_by_two + two_by_one + two_by_two + two_by_three + three_by_two
    building_weights = weights1 + weights2 + weights3 + weights4 + weights5 + weights6

    grid = DataFrame(grid)
    # print(grid)

    pathway_creator_obj = pathway_creator.PathwayCreator()
    building_creator_obj = building_creator.BuildingCreator()

    # first round
    random_side = random.choices(side, side_weights)
    first_side = random_side[0]

    random_number = random.choices(number, number_weights)
    random_number = random_number[0]

    random_pathway = random.choices(pathway, pathway_weights)
    random_pathway = random_pathway[0]

    # print(first_side, random_pathway, random_number)

    if random_pathway == "road":
        grid = pathway_creator_obj.first_road(first_side, grid, random_number)
    elif random_pathway == "river":
        grid = pathway_creator_obj.first_river(first_side, grid, random_number)
    elif random_pathway == "metro":
        grid = pathway_creator_obj.first_metro(first_side, grid, random_number)

    # second round
    second_side = [x for x in side if x != first_side][0]

    random_number = random.choices(number, number_weights)
    random_number = random_number[0]

    random_pathway = random.choices(pathway, pathway_weights)
    random_pathway = random_pathway[0]

    # print(second_side, random_pathway, random_number)

    if random_pathway == "road":
        grid = pathway_creator_obj.second_road(second_side, grid, random_number)
    elif random_pathway == "river":
        grid = pathway_creator_obj.second_river(second_side, grid, random_number)
    elif random_pathway == "metro":
        grid = pathway_creator_obj.second_metro(second_side, grid, random_number)

    grid = building_creator_obj.building_creator(grid, buildings, building_weights)

    if True in [grid.equals(x) for x in all_grids]:
        print("Duplicate grid")
        duplicate_count = duplicate_count + 1
        # duplicate_index = all_grids.index(grid)
        # print(DataFrame(grid))
        # print(DataFrame(all_grids[duplicate_index]))
        return create_new_grid(duplicate_count)

    else:
        return grid, duplicate_count


all_grids = []
duplicate_count = 0
for i in range(100):
    try:
        new_grid, duplicate_count = create_new_grid(duplicate_count)
        all_grids.append(new_grid)
        print(len(all_grids))
    except:
        continue

    """finally:
        print("Total unique grids", len(all_grids))
        print("Duplicate Counted ", duplicate_count)"""

for i in range(10):
    dp = DataFrame(all_grids[i])
    print(dp)
# print(dp.loc[0].at[0])
print(dp.iat[0, 3])

print("All grid count ", len(all_grids))
print("Duplicate Counted ", duplicate_count)


#flat_grids = list(itertools.chain.from_iterable(all_grids))
#building_counter.building_counter(all_grids)
pprint(all_grids[0].values.tolist())
print(all_grids[0].values.tolist().count("d11"))
