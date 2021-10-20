import CI

def recursion(matrix, bounds, plotMatrix, iteration):

    if iteration < 50:
        # Calculate f(x) values
        fXValues = fx(matrix, numberOfCandidates, numberOfVariables)

        # Creating Plot Matrix
        plotMatrix = CI.plotMatrixFunction(plotMatrix, fXValues, numberOfCandidates)

        # Calculate probability
        probabilityValues = CI.probability(fXValues)

        # Roulette Allocation
        allotment = CI.rouletteAllocation(probabilityValues)

        # New matrix generation
        resMatrix = CI.newMatrix(allotment, matrix)

        # Bounds Reduction
        bounds = CI.boundsReduction(bounds, reductionFactor)

        # Updating Sampling Intervals
        reducedMatrixBounds = updateSamplingIntervals(bounds, resMatrix)

        # Generating new martix for the next learning attempt from the bounds obtained from the previous learning attempt
        matrix = CI.randomMatrixGeneration(reducedMatrixBounds, numberOfCandidates, numberOfVariables)

        recursion(matrix, bounds, plotMatrix, iteration = iteration + 1)

    return 0

def updateSamplingIntervals(bounds, resMatrix):
    
    # x = bounds[0]
    # y = bounds[1]
    x = -10
    y = 10
    reducedMatrixBounds = []

    # Updating Sampling Intervals
    for i in range(len(resMatrix)):
        temppList = []
        for j in range(len(resMatrix[0])):
            tempList = []
            if(resMatrix[i][j] + bounds[0] < x):
                tempList.append(x)
            else:
                tempList.append(resMatrix[i][j] + bounds[0])

            if(resMatrix[i][j] + bounds[1] > y):
                tempList.append(y)
            else:
                tempList.append(resMatrix[i][j] + bounds[1])
            temppList.append(tempList)
        reducedMatrixBounds.append(temppList)

    return reducedMatrixBounds

def fx(matrix, numberOfCandidates, numberOfVariables):

    fXValues = []
    for i in range(numberOfCandidates):
        res = 0
        for j in range(numberOfVariables):
            res = 100 * (((matrix[i][0] ** 2) - matrix[i][1]) ** 2) + ((matrix[i][0] - 1) ** 2) + ((matrix[i][2] - 1) ** 2) + (90 * ((matrix[i][2] ** 2) - matrix[i][3]) ** 2) + (10 * ((matrix[i][0] - 1) ** 2) + (matrix[i][3] - 1) ** 2) + (19.8 * (matrix[i][1] - 1) * (matrix[i][3] - 1))
        fXValues.append(res)
    return fXValues

if __name__ == "__main__":

    iteration = 0
    bounds = [-10, 10]
    reductionFactor = 0.9
    matrix = [[0.5, 10, -9.9, 2], [-9, -4, 2.3, 10], [2,10,-2, 4.8]]
    fXValues = []
    probabilityValues = []
    plotMatrix = []    
    numberOfCandidates = 3
    numberOfVariables = 4

    for i in range(numberOfCandidates):
        templist = []
        plotMatrix.append(templist)
    
    # Recursion
    recursion(matrix, bounds, plotMatrix, iteration)

    CI.plot(plotMatrix, numberOfCandidates)