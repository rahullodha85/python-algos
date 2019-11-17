class GeneratePascalsTriangle:

    def generate(self, numRows: int):

        return_list = []

        for index1 in range(0, numRows):
            row = []
            for index2 in range(0, index1+1):
                if index2 == 0 or index2 == index1:
                    row.insert(index2, 1)
                else:
                    row.insert(index2, return_list[index1-1][index2-1] + return_list[index1-1][index2])
            return_list.append(row)
        return return_list

    def getRow(self, rowIndex: int):
        return_list = []

        for index1 in range(0, rowIndex + 1):
            row = []
            for index2 in range(0, index1 + 1):
                if index2 == 0 or index2 == index1:
                    row.insert(index2, 1)
                else:
                    row.insert(index2, return_list[index1 - 1][index2 - 1] + return_list[index1 - 1][index2])
            return_list.append(row)
        return return_list[rowIndex]
print(GeneratePascalsTriangle().generate(5))