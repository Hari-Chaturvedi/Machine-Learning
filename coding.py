def consRev(n, input):
    pro1=1
    pro2=1
    input=list(map(int, input.split()))
    if n<=2:
        raise ValueError("Invalid Input")
    else:
        if n%2==0:
            for i in range(0,n):
                if i<n/2:
                    pro1= pro1*input[i]
                else:
                    pro2=pro2*input[i]
                    
        else:
            for i in range(0,n+1):
                if i<(n+1)/2:
                    pro1= pro1*input[i]
                else:
                    pro2=pro2*input[(i-1)]
    input2=[]
    if pro1<pro2:
        for i in range(0,len(input)):
            input2.append(input[-i-1])
    
    output2=" ".join(map(str, input2))
    if len(output2)==0:
        output2="Condition not satisfied"
    print(n)
    return output2


print(consRev(6,"1 2 3 4 5 6"))
print(consRev(5,"1 2 3 4 5"))
print(consRev(6,"6 5 4 3 2 1"))
print(consRev(5, "5 4 3 2 1"))