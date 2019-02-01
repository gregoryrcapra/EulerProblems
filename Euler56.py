# wrapper function
def maxDigitalSum(limit):
    maxSum = 0
    for baseNum in range(limit-1,0,-1):
        maxSum = max(maxSum,geometricSum(baseNum,limit))
    return maxSum


# fast way to compute a^b
def geometricSum(baseNum,exponentLimit):
    currentGeoSum = 0
    maxDigSum = 0
    for exponentNum in range(exponentLimit):
        if exponentNum == 0:
            newSum = 1
        elif baseNum == 1:
            newSum = 1
        else:
            newSum = 1-((1-baseNum)*currentGeoSum)
        currentGeoSum += newSum
        maxDigSum = max(maxDigSum,digitSum(newSum))
    return maxDigSum


# generic function to compute digit sum of number
def digitSum(num):
    sumOfDigits = 0
    for char in str(num):
        sumOfDigits += int(char)
    return sumOfDigits

# main entry point of program
if __name__ == '__main__':
    import time

    maxParam = 100
    start = time.time()
    print('Max Digital Sum < {0}: {1}'.format(maxParam,maxDigitalSum(maxParam)))
    end = time.time()
    print('Total Time: {0}'.format(end-start))
