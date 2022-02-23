import random
from pprint import pprint
from pandas import *
import numpy as np
import pathway_creator

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

road_tiles_normal = ["1", "2"]
road_tiles_bridge = ["3", "4"]
river_tiles = ["5", "6"]

number = [0, 1, 2, 3, 4, 5, 6, 7]
number_weights = [10, 10, 10, 10, 10, 10, 10, 10]

side = ["column", "row"]
side_weights = [50, 50]

pathway = ["road", "river", "metro"]
pathway_weights = [60, 30, 10]


# grid = np.indices((8, 8))[0]

def create_new_grid(duplicate_count):
    grid = [
        [["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"]],
        [["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"]],
        [["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"]],
        [["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"]],
        [["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"]],
        [["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"]],
        [["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"]],
        [["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"], ["000"]]
    ]

    pathway_creator_obj = pathway_creator.PathwayCreator()

    # first round
    random_side = random.choices(side, side_weights)
    first_side = random_side[0]

    random_number = random.choices(number, number_weights)
    random_number = random_number[0]

    random_pathway = random.choices(pathway, pathway_weights)
    random_pathway = random_pathway[0]

    #print(first_side, random_pathway, random_number)

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

    #print(second_side, random_pathway, random_number)

    if random_pathway == "road":
        grid = pathway_creator_obj.second_road(second_side, grid, random_number)
    elif random_pathway == "river":
        grid = pathway_creator_obj.second_river(second_side, grid, random_number)
    elif random_pathway == "metro":
        grid = pathway_creator_obj.second_metro(second_side, grid, random_number)

    if grid in all_grids:
        print("Duplicate grid")
        duplicate_count = duplicate_count + 1
        duplicate_index = all_grids.index(grid)
        #print(DataFrame(grid))
        #print(DataFrame(all_grids[duplicate_index]))
        return create_new_grid(duplicate_count)
    else:
        #print(DataFrame(grid))
        return grid, duplicate_count


all_grids = []
duplicate_count = 0
for i in range(500):
    new_grid,duplicate_count = create_new_grid(duplicate_count)

    all_grids.append(new_grid)


print("All grid count ", len(all_grids))
print("Duplicate Counted ",duplicate_count)
