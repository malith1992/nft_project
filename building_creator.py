from pandas import *
import random


class BuildingCreator:

    def building_creator(self, grid, buildings, building_weights):

        while ("000" in grid.values):
            for y in range(8):
                for x in range(8):
                    if grid.iat[y, x] == "000":
                        random_building = random.choices(buildings, building_weights)[0]
                        building_code = random_building[1:]
                        if building_code == "11":
                            grid.iat[y, x] = random_building
                            building_index = buildings.index(random_building)
                            del buildings[building_index]
                            del building_weights[building_index]

                        elif building_code == "12":
                            if y <= 6 and grid.iat[y + 1, x] == "000":
                                grid.iat[y, x] = random_building
                                grid.iat[y + 1, x] = random_building
                                building_index = buildings.index(random_building)
                                del buildings[building_index]
                                del building_weights[building_index]
                            else:
                                continue

                        elif building_code == "21":
                            if x <= 6 and grid.iat[y, x + 1] == "000":
                                grid.iat[y, x] = random_building
                                grid.iat[y, x + 1] = random_building
                                building_index = buildings.index(random_building)
                                del buildings[building_index]
                                del building_weights[building_index]
                            else:
                                continue

                        elif building_code == "22":
                            if x <= 6 and grid.iat[y, x + 1] == "000" and y <= 6 and grid.iat[y + 1, x] == "000" \
                                    and grid.iat[y + 1, x + 1] == "000":
                                grid.iat[y, x] = random_building
                                grid.iat[y, x + 1] = random_building
                                grid.iat[y + 1, x + 1] = random_building
                                grid.iat[y + 1, x] = random_building
                                building_index = buildings.index(random_building)
                                del buildings[building_index]
                                del building_weights[building_index]
                            else:
                                continue

                        elif building_code == "23":
                            if x <= 6 and grid.iat[y, x + 1] == "000" and y <= 5 and grid.iat[y + 1, x] == "000" \
                                    and grid.iat[y + 1, x + 1] == "000" and grid.iat[y + 2, x] == "000" \
                                    and grid.iat[y + 2, x + 1] == "000":

                                grid.iat[y, x] = random_building
                                grid.iat[y, x + 1] = random_building
                                grid.iat[y + 1, x + 1] = random_building
                                grid.iat[y + 1, x] = random_building
                                grid.iat[y + 2, x] = random_building
                                grid.iat[y + 2, x + 1] = random_building
                                building_index = buildings.index(random_building)
                                del buildings[building_index]
                                del building_weights[building_index]
                            else:
                                continue
                        elif building_code == "32":
                            if x <= 5 and grid.iat[y, x + 1] == "000" and y <= 6 and grid.iat[y + 1, x] == "000" \
                                    and grid.iat[y + 1, x + 1] == "000" and grid.iat[y, x + 2] == "000" \
                                    and grid.iat[y + 1, x + 2] == "000":
                                grid.iat[y, x] = random_building
                                grid.iat[y, x + 1] = random_building
                                grid.iat[y + 1, x + 1] = random_building
                                grid.iat[y + 1, x] = random_building
                                grid.iat[y, x + 2] = random_building
                                grid.iat[y + 1, x + 2] = random_building
                                building_index = buildings.index(random_building)
                                del buildings[building_index]
                                del building_weights[building_index]
        return grid

        # print(grid)
        # print("success")
