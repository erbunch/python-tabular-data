#!/usr/bin/env python

'''
this script finds different species of irises and creates separate files of the
data from each flower then creates plots of the petal length X the sepal length
and labels the axes accordingly. For each of the plots there will be different
color coordinate labels and a regression line that will be denoted in the
legend.
'''
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def make_plot(x_var, y_var, name, color):
    plot = plt.scatter(x_var, y_var, label = name, color = color)
    plt.legend()
    return plot

def make_line(xcoor, ycoor, name, color):
    line = stats.linregress(xcoor, ycoor)
    slope = line.slope
    inter = line.intercept
    plt.plot(xcoor, slope * xcoor + inter, label = name + " line", color = color)
    plt.legend()
    return

def create_labels(xax, yax):
    plt.xlabel(xax)
    plt.ylabel(yax)
    return

def main():
    data = pd.read_csv('iris.csv')
    xcoor_versi = data[data.species == "Iris_versicolor"]["petal_length_cm"]
    ycoor_versi = data[data.species == "Iris_versicolor"]["sepal_length_cm"]
    xcoor_virg = data[data.species == "Iris_virginica"]["petal_length_cm"]
    ycoor_virg = data[data.species == "Iris_virginica"]["sepal_length_cm"]
    xcoor_seto = data[data.species == "Iris_setosa"]["petal_length_cm"]
    ycoor_seto = data[data.species == "Iris_setosa"]["sepal_length_cm"]
    make_plot(xcoor_versi, ycoor_versi, "Versicolor", "blue")
    make_plot(xcoor_virg, ycoor_virg, "Virginica", "red")
    make_plot(xcoor_seto, ycoor_seto, "Setosa", "green")
    make_line(xcoor_versi, ycoor_versi, "Versicolor", "blue")
    make_line(xcoor_virg, ycoor_virg, "Virginica", "red")
    make_line(xcoor_seto, ycoor_seto, "Setosa", "green")
    create_labels("Petal Length (cm)", "Sepal Length (cm)")
    plt.savefig("petal_v_sepal_for_3.png")
    return

if __name__ == "__main__":
    #data = pd.read_csv('iris.csv')
    #print(data)
    #xcoor_seto = data[data.species == "Iris_setos"]["petal_length_cm"]
    #print(xcoor_seto)
    main()
