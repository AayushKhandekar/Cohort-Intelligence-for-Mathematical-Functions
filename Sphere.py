import CI

def recursion(matrix, bounds, plotMatrix, iteration):

    if iteration < 50:
        # Calculate f(x) values
        fXValues = fX(matrix, numberOfCandidates, numberOfVariables)

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
        # print(bounds)

        # Updating Sampling Intervals
        reducedMatrixBounds = updateSamplingIntervals(bounds, resMatrix)

        # Generating new martix for the next learning attempt from the bounds obtained from the previous learning attempt
        matrix = CI.randomMatrixGeneration(reducedMatrixBounds, numberOfCandidates, numberOfVariables)

        recursion(matrix, bounds, plotMatrix, iteration = iteration + 1)

    return 0

def updateSamplingIntervals(bounds, resMatrix):
    
    x = -5.12
    y = 5.12
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

def fX(matrix, numberOfCandidates, numberOfVariables):
    
    fXValues = []
    for i in range(numberOfCandidates):
        res = 0
        for j in range(numberOfVariables):
            res = res + matrix[i][j]**2
        fXValues.append(res)
    return fXValues

if __name__ == "__main__":

    iteration = 0
    bounds = [-5.12, 5.12]
    reductionFactor = 0.9
    matrix = [[0.5, 1], [-1, 2], [1, -2]]
    fXValues = [] 
    probabilityValues = []
    plotMatrix = []
    numberOfCandidates = 3
    numberOfVariables = 2       

    # Adding candidate f(x) values into plotMatrix to plot the Convergence Plot
    for i in range(numberOfCandidates):
        templist = []
        plotMatrix.append(templist)

    # Recursion
    recursion(matrix, bounds, plotMatrix, iteration)

    CI.plot(plotMatrix, numberOfCandidates)

    

