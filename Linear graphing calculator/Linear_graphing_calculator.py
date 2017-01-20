## Author: Boris Chan
## Date: 28/12/2016
## Purpose: using linear regresssion to find line of best fit from user defined data

import os
import matplotlib.pyplot as plt


def Clear():
    os.system('cls')

def Menu():
    print("""Menu:
  1. input data
  2. plot data
  3. find line of best fit
  4. plot data with LOBF
  5. quit program""")

    user_input = input("")
    if user_input == "1":
        Clear()
        Input()
    elif user_input == "2":
        Clear()
        Plot_Data()
    elif user_input == "3":
        Clear()
        Find_LOFT()
    elif user_input == "4":
        Clear()
        Plot_LOFT()
    elif user_input == "5":
        exit()

def Input():
    file = open('dataset.txt', 'w')
    print("""Input x-value, space, then y-value
Input "save" when done""")
    print ("x    y")
        
    not_done = True
    while not_done:
        point = input()
        if point != "save":
            file.write(point + "\n")
        else:
            not_done = False
    file.close()

    Clear()
    Menu()

def Plot_Data():
    data = open('dataset.txt', 'r')
    xs = []
    ys = []
    for point in data:
        point = point.rstrip('\n')
        point = point.split(' ')
        xs.append(point[0])
        ys.append(point[1])

    plt.scatter(xs,ys)
    plt.show()

    Clear()
    Menu()

def Find_LOFT():
    data = open('dataset.txt', 'r')
    xs = []
    ys = []
    for point in data:
        point = point.rstrip('\n')
        point = point.split(' ')
        xs.append(float(point[0]))
        ys.append(float(point[1]))
        
    m = (((Mean(xs)*Mean(ys)) - Mean(Mult_list(xs,ys))) /
         ((Mean(xs)**2) - Mean(Mult_list(xs, xs))))
    b = Mean(ys) - m * Mean(xs)

    print("y = %sx + %s" % (str(m), str(b)))
    input("press any key to continue...")
    
    Clear()
    Menu()    

def Mult_list(lst1, lst2):
    lst = []
    for i in range(len(lst1)):
        lst.append(lst1[i]*lst2[i])
    return lst

def Mean(lst):
    return sum(lst) / len(lst)

def Plot_LOFT():
    data = open('dataset.txt', 'r')
    xs = []
    ys = []
    for point in data:
        point = point.rstrip('\n')
        point = point.split(' ')
        xs.append(float(point[0]))
        ys.append(float(point[1]))
        
    m = (((Mean(xs)*Mean(ys)) - Mean(Mult_list(xs,ys))) /
         ((Mean(xs)**2) - Mean(Mult_list(xs, xs))))
    b = Mean(ys) - m * Mean(xs)

    regression_line = [m*x+b for x in xs]
    plt.scatter(xs,ys)
    plt.plot(xs, regression_line)
    plt.show()

    Clear()
    Menu()
    
Menu()

         
