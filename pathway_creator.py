import random


class PathwayCreator:

    def first_river(self, side, grid, random_number):

        if side == "column":
            grid[0][random_number][0] = "vrv"
            for i in range(1, 8):
                grid[i][random_number][0] = "vrv"

        elif side == "row":
            grid[random_number][0][0] = "hrv"
            for i in range(1, 8):
                grid[random_number][i][0] = "hrv"
        return grid

    def second_river(self, side, grid, random_number):

        if side == "column":
            for j in range(0, 8):
                if grid[j][random_number][0] == "000":
                    grid[j][random_number][0] = "vrv"
                elif grid[j][random_number][0] == "hrd":  # road river cross
                    grid[j][random_number][0] = "hbd"
                elif grid[j][random_number][0] == "hrv":  # river cross
                    grid[j][random_number][0] = "rvc"

        elif side == "row":
            for j in range(0, 8):
                if grid[random_number][j][0] == "000":
                    grid[random_number][j][0] = "hrv"
                elif grid[random_number][j][0] == "vrd":  # road river cross
                    grid[random_number][j][0] = "vbd"
                elif grid[random_number][j][0] == "vrv":  # river cross
                    grid[random_number][j][0] = "rvc"
        return grid

    def first_road(self, side, grid, random_number):

        if side == "column":
            grid[0][random_number][0] = "vrd"
            for i in range(1, 8):
                grid[i][random_number][0] = "vrd"

        elif side == "row":
            grid[random_number][0][0] = "hrd"
            for i in range(1, 8):
                grid[random_number][i][0] = "hrd"
        return grid

    def second_road(self, side, grid, random_number):

        if side == "column":
            for j in range(0, 8):
                if grid[j][random_number][0] == "000":
                    grid[j][random_number][0] = "vrd"
                elif grid[j][random_number][0] == "hrv":  # river road cross
                    grid[j][random_number][0] = "vbd"
                elif grid[j][random_number][0] == "hrd":  # road cross
                    grid[j][random_number][0] = "rdc"

        elif side == "row":
            for j in range(0, 8):
                if grid[random_number][j][0] == "000":
                    grid[random_number][j][0] = "hrd"
                elif grid[random_number][j][0] == "vrv":  # river road cross
                    grid[random_number][j][0] = "hbd"
                elif grid[random_number][j][0] == "vrd":  # road cross
                    grid[random_number][j][0] = "rdc"
        return grid

    def first_metro(self, side, grid, random_number):

        if side == "column":
            grid[0][random_number][0] = "vmt"
            for i in range(1, 8):
                grid[i][random_number][0] = "vmt"

        elif side == "row":
            grid[random_number][0][0] = "hmt"
            for i in range(1, 8):
                grid[random_number][i][0] = "mt"
        return grid

    def second_metro(self, side, grid, random_number):

        if side == "column":
            for j in range(0, 8):
                if grid[j][random_number][0] == "000":
                    grid[j][random_number][0] = "vmt"
                elif grid[j][random_number][0] == "hmt":  # metro cross
                    grid[j][random_number][0] = "mtc"

        elif side == "row":
            for j in range(0, 8):
                if grid[random_number][j][0] == "000":
                    grid[random_number][j][0] = "hmt"
                elif grid[random_number][j][0] == "vmt":  # road cross
                    grid[random_number][j][0] = "mtc"
        return grid
