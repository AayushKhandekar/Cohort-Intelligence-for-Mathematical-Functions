import math
import CI

def recursion(matrix, bounds, plotMatrix, iteration):

    if iteration < 500:
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
        bounds = boundsReduction(bounds, reductionFactor)

        # Updating Sampling Intervals
        reducedMatrixBounds = updateSamplingIntervals(bounds, resMatrix)

        # Generating new martix for the next learning attempt from the bounds obtained from the previous learning attempt
        matrix = CI.randomMatrixGeneration(reducedMatrixBounds, numberOfCandidates, numberOfVariables)

        recursion(matrix, bounds, plotMatrix, iteration = iteration + 1)

    return 0

def updateSamplingIntervals(bounds, resMatrix):
    
    x = -5
    y = 10
    a = 0
    b = 15
    reducedMatrixBounds = []

    # Updating Sampling Intervals
    for i in range(len(resMatrix)):
        temppList = []
        for j in range(len(resMatrix[0])):
            tempList = []
            
            # for x1
            if(resMatrix[i][j] + bounds[0][0] < x):
                tempList.append(x)
            elif(resMatrix[i][j] + bounds[0][0] > x and resMatrix[i][j] + bounds[0][0] < y):
                tempList.append(resMatrix[i][j] + bounds[0][0])
                
            if(resMatrix[i][j] + bounds[0][1] > y):
                tempList.append(y)
            elif(resMatrix[i][j] + bounds[0][1] > y and resMatrix[i][j] + bounds[0][1] < x):
                tempList.append(resMatrix[i][j] + bounds[0][1])
            
            # for x2
            if(resMatrix[i][j] + bounds[1][0] < a):
                tempList.append(a)
            elif(resMatrix[i][j] + bounds[1][0] > a and resMatrix[i][j] + bounds[1][0] < b):
                tempList.append(resMatrix[i][j] + bounds[1][0])
    
            if(resMatrix[i][j] + bounds[1][1] > b):
                tempList.append(b)
            elif(resMatrix[i][j] + bounds[1][1] > b and resMatrix[i][j] + bounds[1][1] < a):
                tempList.append(resMatrix[i][j] + bounds[1][1])

            temppList.append(tempList)
        reducedMatrixBounds.append(temppList)

    return reducedMatrixBounds

def boundsReduction(bounds, reductionFactor):

    for i in range(len(bounds)):
        for j in range(2):
            bounds[i][j] = bounds[i][j] * reductionFactor
    return bounds

def fx(matrix, numberOfCandidates, numberOfVariables):

    fXValues = []
    for i in range(numberOfCandidates):
        res = 0
        for j in range(numberOfVariables):
            res = (1 * (matrix[i][1] - ((5.1 / (4 * 3.14 * 3.14)) * (matrix[i][0] ** 2)) + ((5 / 3.14) * (matrix[i][0])) - 6) ** 2) + (10 * (1 - (1 / (8 * 3.14))) * math.cos(matrix[i][0])) + 10
        fXValues.append(res)
    return fXValues

if __name__ == "__main__":

    iteration = 0
    bounds = [[-5, 10], [0, 15]]
    reductionFactor = 0.9
    matrix = [[-5, 0], [10, 5], [0, 15]]
    fXValues = []
    probabilityValues = []
    plotMatrix = []    
    numberOfCandidates = 3
    numberOfVariables = 2

    for i in range(numberOfCandidates):
        templist = []
        plotMatrix.append(templist)
    
    # Recursion
    recursion(matrix, bounds, plotMatrix, iteration)

    CI.plot(plotMatrix, numberOfCandidates)
