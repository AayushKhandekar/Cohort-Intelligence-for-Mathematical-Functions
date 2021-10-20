import random
import matplotlib.pyplot as plt

def plot(plotMatrix, numberOfCandidates):

    for i in range(numberOfCandidates):
        plt.plot(plotMatrix[i])

    plt.ylabel('f (x)') #set the label for y axis
    plt.xlabel('Iteration') #set the label for x-axis
    plt.title("Convergence Plot") #set the title of the graph
    plt.show()

    return 0

def randomMatrixGeneration(bounds, numberOfCandidates, numberOfVariables):

    newMatrix = []
    for i in range(numberOfCandidates):
        tempList = []
        for j in range(numberOfVariables):
            x = bounds[i][j][0]
            y = bounds[i][j][1]
            tempList.append(random.uniform(x, y))
        newMatrix.append(tempList)
    return newMatrix

def updateSamplingIntervals(bounds, resMatrix):
    
    # x = bounds[0]
    # y = bounds[1]
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

def boundsReduction(bounds, reductionFactor):

    # print(bounds)

    # Reducing Bounds
    for i in range(len(bounds)):
        bounds[i] = bounds[i] * reductionFactor
    
    return bounds

def newMatrix(allotment, matrix):

    resMatrix = []
    count = 0
    for i in allotment:
        resMatrix.append(matrix[i])
        count += 1
    return resMatrix

def rouletteAllocation(probabilityValues):

    randomValues = []
    ranges = []
    allotment = []
    sum = 0

    for i in range(len(probabilityValues)):
        
        # Generating random values for each candidate for roulette approach
        num = random.randrange(0,100) / 100
        randomValues.append(num)

        # Calculating ranges to check which candidate fits in what range
        sum = sum + probabilityValues[i]
        ranges.append(sum)

    # New Allocations to the candidates
    for i in range(len(probabilityValues)):
        countJ = []
        for j in range(len(probabilityValues)): 
            if(randomValues[i] < ranges[j]):
                countJ.append(j)
                break
            else: 
                pass
        allotment.append(countJ[0])
    return allotment
        
def probability(fXValues):

    probabilityValues = []
    sum = 0
    for i in fXValues:
        sum = sum + 1 / i
    for i in fXValues:
        probabilityValues.append((1 / i) / sum)
    # print(probabilityValues)
    return probabilityValues

def plotMatrixFunction(plotMatrix, fxValues, numberOfCandidates):

    for i in range(numberOfCandidates):
        plotMatrix[i].append(fxValues[i])
    
    return plotMatrix