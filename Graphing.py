'''
APCSPCreateTask.py
Developer: Shreyas Tulsi

'''




#These three lines import all of the necessary modules for this project

from matplotlib import pyplot as plt
from os import system
import csv 
import numpy as np
import math

def statistical_analysis(x,y,z, method_type):
	#Function takes in all of the necessary datasets to get the analytics and then prints the analytics to the change

	#This initial conditional statement determines which graph is being analyzed

	#Analysis for line plot
	if method_type == 'a':
		change_in_y= x[-1]- y[-2]
		change_in_x = x[-1]-y[-2]
		slope = round(change_in_y/change_in_x, 1)
		projectednext_pointx = x[-1] + change_in_x
		projectednext_pointy= y[-1] + change_in_y
	
		plt.text(2, 11, ('Slope:'+str(slope)))
		plt.text(2, 10,'Projected Next X and Y'+ '('+str(projectednext_pointx)+ ','+ str(projectednext_pointy)+')')



	#Analysis for Bar Chart
	elif method_type =='b':
		highest_value_cateogry = ''
		highest_value= 0
		lowest_value = 10000000000000000000
		lowest_value_cateogry = ''
		mean = 0
		counter = 0

	#Determining the highest value of the set and what catgory it belongs to
		for value in y:
			if value > highest_value:
				highest_value = value
				highest_value_cateogry = z[counter]
				counter += 1
			else:
				counter+=1

	#Deteermining lowest valye of the set and what category it belongs to
		counter = 0
		for value in y:
			if value < lowest_value:
				lowest_value = value
				lowest_value_cateogry = z[counter]
				counter += 1
			else:
				counter+=1

		avg = 0
		for value in y:
			avg+= value

		avg = round(avg/(len(y)),2)

		plt.text(0, (highest_value-1), 'Highest Value: '+ str(highest_value_cateogry)+','+ str(highest_value))
		plt.text(0, (highest_value-20), 'Lowest Value: '+ lowest_value_cateogry+','+str(lowest_value))
		plt.text(0, (highest_value-40), 'AVG of the values: '+str(avg))

	#Analysis for histogram
	elif method_type == 'c':
		highest_value = max(y)
		lowest_value = min(y)
		percentage_of_vals= round(len(y)/len(x),2)
		number_in_bin= len(y)

		plt.text(2, 4.0,( "The most frequent range was " + str(lowest_value) + ", "+ str(highest_value)   ))
		plt.text(2, 3.75,( "This range made up " + str(percentage_of_vals*100) + "% " + " of the dataset"  ))
		plt.text(2, 3.5,( "Frequency: "+str(number_in_bin) ))

#Child Algorithms

def line_plot(x_vals, y_vals):

	#Function takes in x and y values, returns a line plot 

	plt.plot(x_vals, y_vals)
	statistical_analysis(x_vals, y_vals, 0,  'a')
	 
def bar_chart(x_vals, y_vals, categories):
	#Function takes in 2 different sets of x and y values, and plots two bar graphs according to these values 
	system('clear')
	plt.bar(x_vals, y_vals, color='gray', width=0.4, align = 'center' )
	statistical_analysis(x_vals, y_vals, categories, 'b')



def histogram(data_vals, bins, most_frequent_bin):
	#Function takes in all of the data value and the bins for this dataaset, to create the histogram
	

	plt.hist(data_vals, bins, histtype='bar')
	statistical_analysis(data_vals, most_frequent_bin, 0, 0)

	

 
def pie_chart(slices, sections, colors):
	#Function takes in all of the slices, section names, and colors in order to create desired bar graph for the user
	plt.pie(slices, labels=sections, colors =colors, startangle=90, autopct='%1.1f%%')



#All of the predifined lists that the user will feed input into
x_values = []
y_values = []
datapoints = []
bins = []
slices = []
categories = []
cols = ['c','m','r','g']

#Clears the screen for user's to see a fresh interface
system('clear')



#Asks the basic input questions that are necessary for any graph
title = input("What is the title of your data: ") 
x_label = input("What is the title of your x-axis: ")
y_label = input("What is the title of your y-axis: ")

#Parent Algorithm
def get_inputs(method_type):

	#This algorithm is used to extract all of the input required for the graphing functions to execute, and then calls graphing functions
	system('clear')
	x_values = []

	#If the user wants a line plot
	if method_type == 'a':
		a = int(input("How many x value's in your dataset: "))
		for x in range(a):
			x_v = int(input("Enter x-value: "))
			x_values.append(x_v)
			y_v = int(input("Enter y-value: "))
			y_values.append(y_v)
		line_plot(x_values, y_values)

	#If user wants a bar chart
	elif method_type == 'b':

		a = int(input("Number of categories: "))
		for x in range (a):
			category = input("Enter category name: ")
			categories.append(category)

			y_v = int(input("Enter corresponding value: "))
			y_values.append(y_v)

		x_values = np.arange(len(categories))
		plt.xticks(x_values, categories)
		bar_chart(x_values, y_values, categories)

	#If user wants a histogram
	elif method_type == 'c':
		most_frequent_bin = []

		bins = int(input("How many bins do you want: "))


		for x in range(bins):
			highest_frequency = len(most_frequent_bin)

			values_in_bin=int(input("How many values do you have in that bin: "))
			if values_in_bin< highest_frequency:

				for y in range(values_in_bin):
					value =int(input("Enter Value: "))
					datapoints.append(value)
			else:

				most_frequent_bin= []
				for y in range(values_in_bin):
					value = int(input("Enter Value: "))
					most_frequent_bin.append(value)
					datapoints.append(value)

		histogram(datapoints, bins, most_frequent_bin)

	#If user wants a pie chart
	elif method_type == 'd':
		a = int(input("How many total slices do you have: "))
		for x in range(a):
			slicename=input("Enter the name of that slice: ")
			categories.append(slicename)
			value = input("Enter the value of that slice: ")
			slices.append(value)

		pie_chart(slices, categories, cols)



#This statement will execute, if user wants to input data from a file
location = input("Do you want to use the data in the user editable text file: [Y]es or [N]o: ").lower()
if location == 'y':
	with open('TestFile.txt', 'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=',')
		for row in plots:
			x_values.append(int(row[0]))
			y_values.append(int(row[1]))
	line_plot(x_values, y_values)
	

#If not the rest of the progam will execute
else:
	system('clear')
	method_type = input("Choose your chart \nA:Line Plot\nB:Bar Chart\nC:Histogram\nD:PieChart\n").lower()
	get_inputs(method_type)
	system('clear')
	



#After all of the points have been plotted, the labels, titles and legend go on, and the image is displayed to the user
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.title(title)
plt.show()

