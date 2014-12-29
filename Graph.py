"""
Part II: Take the data we just parsed and visualize it using
Python math libraries.
"""
from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np
import Parse

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def visualize_days():
    """Visualize data by the day of week"""

    # get the parsed data from Parse.py
    data_file = Parse.parse(MY_FILE, ",")

    # variable counter iterates through each line
    # of data in parsed data, and counts how many
    # incidents occured in each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # seperate the counter to order it when plotting
    # dicionaries do no preserve order but lists do
    data_list = [
                 counter["Monday"],
                 counter["Tuesday"],
                 counter["Wednesday"],
                 counter["Thursday"],
                 counter["Friday"],
                 counter["Saturday"],
                 counter["Sunday"]
                 ]
    # plt.xticks() only accepts tuples for labeling x-axis
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # assign the y-axis data to a matplotlib plot instance
    plt.plot(data_list)

    # assigning labels to the plot
    plt.xticks(range(len(day_tuple)), day_tuple)

    # save the plot
    plt.savefig("Days.png")
    #close figure
    plt.clf()

def visualize_type():
    """Visualize data by category in a bar graph"""

    # get parsed data
    data_file = Parse.parse(MY_FILE, ",")

    # returns a dict with the sum of the total incidents per Category
    counter = Counter(item["Category"] for item in data_file)

    # set labels based on the keys of counter
    # order does not matter
    labels = tuple(counter.keys())

    # set where the labels hit the x-axis
    xlocations = np.array(range(len(labels))) +0.5

    # width of each bar
    width = 0.5

    # assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)

    # assign labels and tick locations to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # provide spacing to prevent labels being cut off on graph
    plt.subplots_adjust(bottom=0.4)

    # create graph size
    plt.rcParams['figure.figsize'] = 12, 8

    #save the plot
    plt.savefig("Type.png")
    # close figure
    plt.clf()




def main():
    visualize_type()

if __name__ == "__main__":
    main()
