############################################################
# Name: Jonathan Carbonneau
# CS115 HW#
# 
# Pledge: I pledge my honor that i have abbided by the stevens honor system
############################################################

import random
# change finds the least amount of coins to make a money ammount
def change(amount, coins):
    coins.sort(reverse=True) #sorts em big to small
    n = len(coins)
    maxbound = coins[n - 1] * amount + 1# this is the deapest it shold serch
    best = maxbound

    def depthFirstSearch(index, total, level):
        nonlocal best
        if total == amount:
            best = min(best, level)
            return
        for i in range(index, n):# creats 3 new nodes
            coin = coins[i]
            if coin <= amount - total < coin * (best - level):#stops if it is deaper best depth
                depthFirstSearch(i, total + coin, level + 1)
    depthFirstSearch(0, 0, 0)
    if best != maxbound:
        return best
    return -1
#print(change(313,[7,24,42]))


#currency will produce a number long list of random numbers less than 10
def currency(number):
    #genarates a list with random numbers
    listgen = lambda x: listgen(x-1)  + [random.randrange(10)] if x > 1 else [random.randrange(10)]
    #removes dupicates and adds random numbers till it gets to number long
    filterRandomList = lambda randomList: filterRandomList(list(set(randomList)) + [random.randrange(10)]) if len(randomList) > len(set(randomList)) or len(set(randomList)) != number else randomList
    return filterRandomList(listgen(number))

#print(currency(4))

