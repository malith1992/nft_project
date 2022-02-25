import random


class PathwayCreator:

    def first_river(self, side, grid, random_number):

        if side == "column":
            grid.iat[0,random_number] = "vrv"
            for i in range(1, 8):
                grid.iat[i,random_number] = "vrv"

        elif side == "row":
            grid.iat[random_number] = "hrv"
            for i in range(1, 8):
                grid.iat[random_number,i] = "hrv"
        return grid

    def second_river(self, side, grid, random_number):

        if side == "column":
            for j in range(0, 8):
                if grid.iat[j,random_number] == "000":
                    grid.iat[j,random_number] = "vrv"
                elif grid.iat[j,random_number] == "hrd":  # road river cross
                    grid.iat[j,random_number] = "hbd"
                elif grid.iat[j,random_number] == "hrv":  # river cross
                    grid.iat[j,random_number] = "rvc"

        elif side == "row":
            for j in range(0, 8):
                if grid.iat[random_number,j] == "000":
                    grid.iat[random_number,j] = "hrv"
                elif grid.iat[random_number,j] == "vrd":  # road river cross
                    grid.iat[random_number,j] = "vbd"
                elif grid.iat[random_number,j] == "vrv":  # river cross
                    grid.iat[random_number,j] = "rvc"
        return grid

    def first_road(self, side, grid, random_number):
        if side == "column":
            grid.iat[0,random_number] = "vrd"
            for i in range(1, 8):
                grid.iat[i,random_number] = "vrd"

        elif side == "row":
            grid.iat[random_number,0] = "hrd"
            for i in range(1, 8):
                grid.iat[random_number,i] = "hrd"
        return grid

    def second_road(self, side, grid, random_number):

        if side == "column":
            for j in range(0, 8):
                if grid.iat[j,random_number] == "000":
                    grid.iat[j,random_number] = "vrd"
                elif grid.iat[j,random_number] == "hrv":  # river road cross
                    grid.iat[j,random_number] = "vbd"
                elif grid.iat[j,random_number] == "hrd":  # road cross
                    grid.iat[j,random_number] = "rdc"

        elif side == "row":
            for j in range(0, 8):
                if grid.iat[random_number,j] == "000":
                    grid.iat[random_number,j] = "hrd"
                elif grid.iat[random_number,j] == "vrv":  # river road cross
                    grid.iat[random_number,j] = "hbd"
                elif grid.iat[random_number,j] == "vrd":  # road cross
                    grid.iat[random_number,j] = "rdc"
        return grid

    def first_metro(self, side, grid, random_number):

        if side == "column":
            grid.iat[0,random_number] = "vmt"
            for i in range(1, 8):
                grid.iat[i,random_number] = "vmt"

        elif side == "row":
            grid.iat[random_number,0] = "hmt"
            for i in range(1, 8):
                grid.iat[random_number,i] = "hmt"
        return grid

    def second_metro(self, side, grid, random_number):

        if side == "column":
            for j in range(0, 8):
                if grid.iat[j,random_number] == "000":
                    grid.iat[j,random_number] = "vmt"
                elif grid.iat[j,random_number] == "hmt":  # metro cross
                    grid.iat[j,random_number] = "mtc"

        elif side == "row":
            for j in range(0, 8):
                if grid.iat[random_number,j] == "000":
                    grid.iat[random_number,j] = "hmt"
                elif grid.iat[random_number,j] == "vmt":  # metro cross
                    grid.iat[random_number,j] = "mtc"
        return grid
