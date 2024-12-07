def raisepower(basenum, powtime):
    result=1
    for i in range(0,powtime):
        result*=basenum

    print(result)     

raisepower(2,5)