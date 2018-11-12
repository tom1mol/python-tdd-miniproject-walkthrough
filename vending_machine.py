from byotest import *       #import byotest framework  from byotest.py

def get_change(amount):     #function get_change with amount(argument)
    if amount == 0:                                                     #if statement protects existing tests
        return []               #return empty list

    if amount in [100, 50, 20, 10, 5, 2, 1]:
        return [amount]
        
    change = []                         #empty list called change
    for coin in [100,50,20,10,5,2,1]:
        if coin <= amount:              #if change <= value we pass in
            amount -= coin              # deduct amount of coin..from amount sent in
            change.append(coin)         #add that on to our change
            
    return change
    
    
test_are_equal(get_change(0),[])  #amount of change = 0...no coins back. done using test_are_equal calling_get change function
                                    #0 change then get empty list back
test_are_equal(get_change(1),[1])   #expect 1 to be returned    
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2,1])
test_are_equal(get_change(7), [5, 2])


print("All tests pass!")    #create all tests pass message
