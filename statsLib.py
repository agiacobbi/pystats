import math
import sys
import csv

e = 2.718281

# IN PROGRESS
def getSet(fileName):
    myData = []
    with open(fileName, 'r') as fin:
        for line in fin:
            myData.append(float(line))

    return myData

# calculates sample mean of a dataset
# dataSet is list of integers or floats
# returns a float
def sMean(dataSet):
    mean = 0.0

    for item in dataSet:
        mean += item

    return (mean / len(dataSet))

# calculates the median of a dataset
# dataSet is a list of integers or floats
# returns a float
def median(dataSet):
    dataSet.sort()
    if (len(dataSet) % 2 == 0):
        return (sMean([float(dataSet[len(dataSet) / 2]), float(dataSet[len(dataSet) / 2 - 1])]))
    return dataSet[len(dataSet) / 2]

# calculates the sample variance of a dataset using formula
#   sVar = sum((x - xBar) ^ 2) / n - 1
# dataSet is a list of integers or floats
# returns a float
def sampleVariance(dataSet):
    mean = sMean(dataSet)
    aSum = 0.0

    for item in dataSet:
        aSum += ((item - mean) ** 2)
    
    return (aSum / (len(dataSet) - 1))

# calculates the sample standard deviation of a dataset
# dataset is a list of integers or floats
# returns a float
def sampleStdDev(dataSet):
    sVar = sampleVariance(dataSet)

    return math.sqrt(sVar)

# calculates a permuation
# n and k are integers
# returns an integer
def permutation(n, k):
    return (math.factorial(n) / math.factorial(n - k))

# calculates a combination
# n and k are integers
# returns and integer
def combination(n, k):
    return (permutation(n, k) / math.factorial(k))

# returns binomial probability of x successes given n trials and p probability
# x and n are integers where x <= n and 0 <= p <= 1
# returns a float
def binProb(x, n, p):
    return (math.factorial(n) / (math.factorial(n - x) * math.factorial(x)) * 
           (p ** x) * ((1 - p) ** (n - x)))

# returns cumulative binomial probability of x successes given n trials
# x and n are integers where x <= n and 0 <= p <= 1
# returns a float
def cumBinProb(x, n, p):
    cumProb = 0.0
    for i in range(int(x + 1)):
        cumProb += binProb(i, n, p)
    return cumProb

# returns poisson probability of y occurrences given mu m
# y is an integer and m is a float
# returns a float
def poissonProb(m, y):
    return ((e ** (-m) * m ** (y)) / (math.factorial(y)))

# returns cumulative poisson probability of y occurrences given mu m
# y is an integer and m is a float
# returns a float
def cumPoissonProb(m, y):
    cumProb = 0.0
    for i in range(int(y + 1)):
        cumProb += poissonProb(m, i)
    return cumProb

def xToZ(x, m, s):
    return ((x - m) / s)

'''
def main():
    #script calculations here
    
main()
'''