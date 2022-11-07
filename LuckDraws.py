# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:34:13 2019

@author: turkf
"""
import matplotlib.pyplot as plt
import numpy as np


def headortails(amount, printer=1, load=0, load_n=0, graph=1):
    """Simulates a given number of head or tail throws.\n
        amount  ->  How many times will it be simulated \n
        printer ->  0 to not print information to console , 1 to print information\n
        load and load_n are for another function.\n
        graph   ->  0 to now show a graph , 1 to show a graph"""

    global tail
    global head

    tail_list = []
    head_list = []

    tail=0
    head=0
    
    for i in range(amount+1):
        
        a = np.random.randint(0, 2)
        
        if a == 0:
            tail += 1
            
        else:
            head += 1

        tail_list.append(tail)
        head_list.append(head)
    
    if head == 0:
        h_t_rate    =   1
    
    else:
        h_t_rate = tail/head
    

    
    
    if printer == 1:
        print("Total : ", amount)
        print("TAIL - HEAD : {0}  /  {1}".format(tail, head))
        
        #Gives the closeness to the actual mathematical probability.
        if head > tail:
            print("Correctness Rate   : {0} - ({1})".format(round(h_t_rate, 5), h_t_rate))
            print("Incorrectness Rate : {0} - ({1})".format(round(1-h_t_rate, 5), 1-h_t_rate))
        else:
            print("Correctness Rate   : {0} - ({1})".format(round(1/h_t_rate, 5), 1/h_t_rate))
            print("Incorrectness Rate : {0} - ({1})".format(round(1-1/h_t_rate, 5), 1-1/h_t_rate))
            

        print("Tail Rate     : ", tail/amount)
        print("Head Rate     : ", head/amount)
        print("Rounded up probability : {0}   ---   {1}".format(round(tail/amount, 1), round(head/amount, 1)))
    
    if load == 1:
        try:
            print(amount/load_n, "%")
        except:
            raise TypeError("to use load option you should enter load_n")
        
    if graph == 1:
        plt.plot(tail_list, c = "red", label = "YAZI")
        plt.plot(head_list, c = "blue", label = "TURA")
        plt.title("TAIL/HEAD")
        plt.xlabel("Event index")
        plt.ylabel("Happened event count")
        plt.legend()
        plt.show()
        

def headortails_failrate(start, stop, freq=20):
    """Iterates through different amounts of head or tails simulations and shows the distance to actual mathematical probability changing\n
        Used to show the accuracy of hacker statistics changing by event count\n
        start   ->  Starting amount of simulations\n
        stop    ->  Ending amount of simulations\n
        freq    ->  Amount to increase per each iteration."""

    global tail
    global head

    error_s = []

    for i in range(start,stop,freq):
        headortails(i, printer=0, load=1, load_n=stop, graph=0)
        if tail > head:
            error_s.append(1 - head/tail)
        else:
            error_s.append(1 - tail/head)   
    
    plt.plot(range(start,stop,freq), error_s)
    plt.title("TAILS-HEAD FAIL RATE")
    plt.xlabel("Simulation amount")
    plt.ylabel("Fail Rate")
    plt.show()
    
    

def roulette(color, bet, budget, amount=100, m_graph =0):
    """Simulation of roulette playing with a budget, profit and loss\n
        color   ->  color to play each round, choose r, g or b. r for red, g for green, b for black.\n
        bet     ->  amount of money to play each round.
        amount  ->  simulation count
        m_graph ->  0 to not print a graph, 1 for printing a graph"""

    R = [i for i in range(2, 37, 2)]
    B = [i for i in range(1, 36, 2)]
    G = [0]
    
    if m_graph == True:
        Bu_list = [budget]
    
    if color != "r" and color != "g" and color != "b":
        raise ValueError("choose r, g, b for color")
        
    for i in range(amount):
        budget -= bet
        a = np.random.randint(0,37)
        
        
        if (a in R) and color == "r":
            
            budget += bet*2
        
        elif a in B and color == "b":
            
            budget += bet*2
        
        elif a in G and color == "g":
            
            budget += bet*18
        
        if m_graph == True:
            Bu_list.append(budget)
            
    
    if m_graph == True:
        plt.plot(range(1, len(Bu_list)+1), Bu_list, label="Money")
        plt.title("Budget")
        plt.xlabel("Round")
        plt.ylabel("Money")
        plt.legend()
        plt.show()
            
    return budget

def Dice(count):
    """Simulation of dice throwing.\n
       count    ->  The amount of simulations """

    one_l = []
    two_l = []
    three_l = []
    four_l = []
    five_l = []
    six_l = []

    one = 0
    two = 0
    three = 0 
    four = 0
    five = 0
    six = 0
    
    for i in range(count+1):
        a = np.random.randint(1,7)
        
        if a == 1:
            one +=1
        elif a == 2:
            two +=1
        elif a == 3:
            three +=1
        elif a == 4:
            four +=1
        elif a == 5:
            five +=1
        elif a ==6:
            six +=1
        
        one_l.append(one)
        two_l.append(two)
        three_l.append(three)
        four_l.append(four)
        five_l.append(five)
        six_l.append(six)
    
    x = range(len(one_l))
    
    print("Rounded up probability : {0} - {1} - {2} - {3} - {4} - {5}".format(round(one/count, 3), round(two/count, 3), round(three/count, 3), round(four/count, 3), round(five/count, 3), round(six/count, 3)))
    
    plt.plot(x, one_l, label="One")
    plt.plot(x, two_l, label="Two")
    plt.plot(x, three_l, label="Three")
    plt.plot(x, four_l, label="Four")
    plt.plot(x, five_l, label="Five")
    plt.plot(x, six_l, label="Six")
    plt.xlabel("Throw count")
    plt.ylabel("Number of dice times")
    plt.title("Dice")
    plt.legend()
    plt.show()        
    

#You can change the numbers to your taste
headortails(100)
headortails_failrate(0, 200)
roulette("r", 100, 1000, m_graph=1)
Dice(100)