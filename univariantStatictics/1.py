#Statistics with python

import statistics
from statistics import median
from statistics import mode
Li = [1,2,3,4,5,6,7,8,5,6,7,9]
#measure of central Tendacy
#mean
print ("Average = " + str(statistics.mean(Li)))
#median
print("Median = "+ str((median(Li))))
#medianLow
print("Low Median = " + str(statistics.median_low(Li)))
#medianHigh
print("Median High =" + str(statistics.median_high(Li)))
#mode
print("Mode = " + str(mode(Li)))


#Measure of of dispersion 
#variance
print("Variance = " +str(statistics.variance(Li)))
#standard diviation 
print("Standard Deviation = " + str(statistics.stdev(Li)))


#Measure of Relationship
#covariance measure degree of relation between two variables
print("Covariance = " + str(statistics.covariance(Li)))

#corelation measure strength and direction of the linear relationship between two variables 