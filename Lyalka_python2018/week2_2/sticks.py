def makeMove(sticks):
    import random
    if sticks > 7:
        return random.randint(1,3)
    elif 5 <= sticks <= 7:
        return (sticks - 4)
    elif 1 <= sticks <= 3:
        return sticks
    else:        
        return "Robot lost"
    
print(makeMove(7))