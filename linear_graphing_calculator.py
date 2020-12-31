## Author: Boris Chan
## Date: 28/12/2016
## Purpose: using linear regresssion to find line of best fit from user defined data

import os
import matplotlib.pyplot as plt

menu_text = """Menu:
  1. input data
  2. plot data
  3. find line of best fit
  4. plot data with LOBF
  5. quit program
"""

def clear():
    os.system('clear')

def input_data():
    print("Input x-value, space, then y-value")
    print("Type \"save\" when done")
    print ("x    y")

    with open('dataset.txt', 'w') as file:
        while True:
            text = input()
            if text == "save":
                break
            else:
                file.write(text + "\n")

def plot_data():
    xs = []
    ys = []
    with open('dataset.txt', 'r') as data:
        for point in data:
            point = point.rstrip('\n')
            point = point.split(' ')
            xs.append(float(point[0]))
            ys.append(float(point[1]))
    plt.scatter(xs,ys)
    plt.show()

def find_loft():
    xs = []
    ys = []
    with open('dataset.txt', 'r') as data:
        for point in data:
            point = point.rstrip('\n')
            point = point.split(' ')
            xs.append(float(point[0]))
            ys.append(float(point[1]))        
    m = (((mean(xs)*mean(ys)) - mean(mult_list(xs,ys))) /
         ((mean(xs)**2) - mean(mult_list(xs, xs))))
    b = mean(ys) - m * mean(xs)

    print("y = %sx + %s" % (str(m), str(b)))
    input("press any key to continue...")
    
def mult_list(lst1, lst2):
    lst = []
    for i in range(len(lst1)):
        lst.append(lst1[i]*lst2[i])
    return lst

def mean(lst):
    return sum(lst) / len(lst)

def plot_loft():
    xs = []
    ys = []
    with open('dataset.txt', 'r') as data:
        for point in data:
            point = point.rstrip('\n')
            point = point.split(' ')
            xs.append(float(point[0]))
            ys.append(float(point[1]))        
    m = (((mean(xs)*mean(ys)) - mean(mult_list(xs,ys))) /
         ((mean(xs)**2) - mean(mult_list(xs, xs))))
    b = mean(ys) - m * mean(xs)

    regression_line = [m*x+b for x in xs]
    plt.scatter(xs,ys)
    plt.plot(xs, regression_line)
    plt.show()
    
def main():
    while True:
        clear()
        print(menu_text)
        user_input = input("Your input: ")        
        if user_input == "1":
            input_data()
        elif user_input == "2":
            plot_data()
        elif user_input == "3":
            find_loft()
        elif user_input == "4":
            plot_loft()
        elif user_input == "5":
            exit()

main()
