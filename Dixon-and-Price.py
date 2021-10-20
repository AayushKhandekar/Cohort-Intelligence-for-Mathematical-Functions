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
            res = ((matrix[i][0] - 1)** 2) + numberOfVariables * ((2 * (matrix[i][1] ** 2) - matrix[i][0]) ** 2)

        fXValues.append(res)
    return fXValues

if __name__ == "__main__":

    iteration = 0
    bounds = [-10, 10]
    reductionFactor = 0.9
    matrix = [[0.5, 1], [-1, 2], [1, -2], [-7,8], [3.4, 6.3], [9.4, 1.6], [3.45, 7.54]]
    fXValues = []
    probabilityValues = []
    plotMatrix = []    
    numberOfCandidates = 7
    numberOfVariables = 2

    for i in range(numberOfCandidates):
        templist = []
        plotMatrix.append(templist)
    
    # Recursion
    recursion(matrix, bounds, plotMatrix, iteration)

    CI.plot(plotMatrix, numberOfCandidates)

    