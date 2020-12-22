import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab
import scipy.stats
from scipy.stats import norm
from scipy.stats import expon
from scipy.optimize import curve_fit


# Number of Monte Carlo simulations to perform
simulation_number = 1000000
# Initialize all the digit numbers to zero in the ybins list. These bins represent a nine bin histogram, each bin represents one of the nine digits. 
ybins = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# Main loop in the code. Each loop is one simulation.
# Each simulation yields one number.
# The first digit of this number will be recorded 
# All recorded numbers should end up creating a Benford Distribution.
for m in range(0, simulation_number):
    # Generate a random number from a range with an initial maximum limit of 1 billion
    # The new maximum limit will have a 1/9 chance of starting with any of the digits. 
    maxlimit = np.random.randint(1, high=1000000000)
    # The second determination of the maximum limit randomizes the upper limit even further.
    # This second randomization is necessary because the first randomization doesn't truly randomize the upper limit.
    # i.e., the upper limit has a 1/9 chance of starting with any of the nine digits. 
    maxlimit = np.random.randint(1, high=maxlimit+1)
    # Now that the second randomization truly randomized the upper limit, a value can be selected for the distribution
    # Every further maximum limit determination from here on out just makes the distribution even more accurate.
    # i.e., the next three max limit determinations make the dataset a truly "natural" dataset that more closely adheres to the Benford distribution.
    maxlimit = np.random.randint(1, high=maxlimit+1) 
    maxlimit = np.random.randint(1, high=maxlimit+1)
    maxlimit = np.random.randint(1, high=maxlimit+1)
    maxlimit = np.random.randint(1, high=maxlimit+1)
    # This selects the final number. The first digit of this number will be checked and recorded. 
    o = np.random.randint(1, high=maxlimit+1)
    # Converts the number to a string so that it can be indexed and checked for equality to each of the nine digits.
    if str(o)[0] == '1':
        ybins[0] += 1
    elif str(o)[0] == '2':
        ybins[1] += 1
    elif str(o)[0] == '3':
        ybins[2] += 1
    elif str(o)[0] == '4':
        ybins[3] += 1
    elif str(o)[0] == '5':
        ybins[4] += 1
    elif str(o)[0] == '6':
        ybins[5] += 1
    elif str(o)[0] == '7':
        ybins[6] += 1
    elif str(o)[0] == '8':
        ybins[7] += 1
    elif str(o)[0] == '9':
        ybins[8] += 1
# Print out the results of the Monte Carlo sim
print(ybins)
# Plot the results as a histogram. 
plt.bar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9], height=ybins, width=0.90)
xbins = [301030, 176090, 124940, 96910, 79180, 66950, 57990, 51150, 45760]
plt.bar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9], height=xbins,
        width=0.90, alpha=0.5, color='firebrick')
plt.xlabel("First Digit", fontsize=20)
plt.ylabel("Occurrences", fontsize=20)
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.ylim(0, (simulation_number/10)*3.5)
plt.yticks([(simulation_number/10)*3, (simulation_number/10) *
            2, (simulation_number/10)*1], ('30%', '20%', '10%'))

plt.annotate('{:.1%}'.format(
    ybins[0]/(simulation_number)), xy=(0.6, ybins[0]+10000), fontsize=14)
plt.annotate('{:.1%}'.format(
    ybins[1]/(simulation_number)), xy=(1.6, ybins[1]+10000), fontsize=14)
plt.annotate('{:.1%}'.format(
    ybins[2]/(simulation_number)), xy=(2.6, ybins[2]+10000), fontsize=14)
plt.annotate('{:.1%}'.format(
    ybins[3]/(simulation_number)), xy=(3.6, ybins[3]+10000), fontsize=14)
plt.annotate('{:.1%}'.format(
    ybins[4]/(simulation_number)), xy=(4.6, ybins[4]+10000), fontsize=14)
plt.annotate('{:.1%}'.format(
    ybins[5]/(simulation_number)), xy=(5.6, ybins[5]+10000), fontsize=14)
plt.annotate('{:.1%}'.format(
    ybins[6]/(simulation_number)), xy=(6.6, ybins[6]+10000), fontsize=14)
plt.annotate('{:.1%}'.format(
    ybins[7]/(simulation_number)), xy=(7.6, ybins[7]+10000), fontsize=14)
plt.annotate('{:.1%}'.format(
    ybins[8]/(simulation_number)), xy=(8.6, ybins[8]+10000), fontsize=14)

plt.title("Benford Distribution", fontsize=20)
plt.show()


print(np.sum(ybins))
print(ybins)
xbins = [301030, 176090, 124940, 96910, 79180, 66950, 57990, 51150, 45760]
plt.plot(ybins, 'b-', lw=1)
plt.plot(xbins, 'm-', lw=1)
plt.show()
