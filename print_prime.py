def primenumber(fp,lp):
    number = fp

    while(number <= lp):
        count = 0
        i = 2
    
        while(i <= number//2):
            if(number % i == 0):
                count = count + 1
                break
            i = i + 1

        if (count == 0 and number != 1):
            print(" %d" %number, end = '  ')
        number = number  + 1

fp1 = int(input(" Please enter the first limit: "))
lp1 = int(input(" Please enter the last limit: "))
primenumber(fp1,lp1)
