# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:34:13 2019

@author: turkf
"""
import matplotlib.pyplot as plt
import numpy as np

yazi = 0
tura = 0

def headortails(x, printer=1, load=0, load_n=0, graph=1):
    global yazi
    global tura
    yazilist = []
    turalist = []
    yazi=0
    tura=0
    
    for i in range(x+1):
        
        a = np.random.randint(0, 2)
        
        if a == 0:
            yazi += 1
            
        else:
            tura += 1
        yazilist.append(yazi)
        turalist.append(tura)
    
    yto = yazi/tura
    

    
    
    if printer == 1:
        print("toplam : ", x)
        print("YAZI  -  TURA : {0}  /  {1}".format(yazi, tura))
        
        if tura > yazi:
            print("D . Oranı : {0} - ({1})".format(round(yto, 5), yto))
            print("Hata Payi : {0} - ({1})".format(round(1-yto, 5), 1-yto))
        else:
            print("D . Oranı : {0} - ({1})".format(round(1/yto, 5), 1/yto))
            print("Hata Payi : {0} - ({1})".format(round(1-1/yto, 5), 1-1/yto))
            
        print("Yazı Yuzdesi : ", yazi/x)
        print("Tura Yuzdesi : ", tura/x)
        print("İhtimaller eşiği : {0}   ---   {1}".format(round(yazi/x, 1), round(tura/x, 1)))
    
    if load == 1:
        try:
            print(x/load_n, "%")
        except:
            raise TypeError("load özelliğini kullanabilmek için load_n de girilmeli")
        
    if graph == 1:
        plt.plot(yazilist, c = "red", label = "YAZI")
        plt.plot(turalist, c = "blue", label = "TURA")
        plt.title("YAZI/TURA")
        plt.xlabel("Olay Sayısı")
        plt.ylabel("Gerçekleşen durum sayısı")
        plt.legend()
        plt.show()
        

def headortails_failrate(start, stop, freq=20):
    global yazi
    global tura
    error_s = []
    for i in range(start,stop,freq):
        headortails(i, printer=0, load=1, load_n=stop, graph=0)
        if yazi > tura:
            error_s.append(1 - tura/yazi)
        else:
            error_s.append(1 - yazi/tura)   
    
    plt.plot(range(start,stop,freq), error_s)
    plt.title("YAZI-TURA HATA ORANI")
    plt.xlabel("Olay Sayısı")
    plt.ylabel("Hata Oranı")
    plt.show()
    
    

def roulette(renk, bahis, butce, atis=1, m_graph =0):
    R = [i for i in range(2, 37, 2)]
    B = [i for i in range(1, 36, 2)]
    G = [0]
    
    if m_graph == True:
        Bu_list = [butce]
    
    if renk != "r" and renk != "g" and renk != "b":
        raise ValueError("renk olarak r , g , b den birini seçiniz")
        
    for i in range(atis):
        butce -= bahis
        a = np.random.randint(0,37)
        
        
        if (a in R) and renk == "r":
            
            butce += bahis*2
        
        elif a in B and renk == "b":
            
            butce += bahis*2
        
        elif a in G and renk == "g":
            
            butce += bahis*36
        
        if m_graph == True:
            Bu_list.append(butce)
            
    
    if m_graph == True:
        plt.plot(range(1, len(Bu_list)+1), Bu_list)
        plt.title("Butce")
        plt.show
            
    
    return butce

def Dice(count):
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
    
    print("İhtimaller eşiği {0} - {1} - {2} - {3} - {4} - {5}".format(round(one/count, 3), round(two/count, 3), round(three/count, 3), round(four/count, 3), round(five/count, 3), round(six/count, 3)))
    
    plt.plot(x, one_l, label="One")
    plt.plot(x, two_l, label="Two")
    plt.plot(x, three_l, label="Three")
    plt.plot(x, four_l, label="Four")
    plt.plot(x, five_l, label="Five")
    plt.plot(x, six_l, label="Six")
    plt.xlabel("Throw count")
    plt.ylabel("Number of dice times")
    plt.title("Zar")
    plt.legend()
    plt.show()        
    
    

print(roulette("g", 10, 1000, m_graph=True))