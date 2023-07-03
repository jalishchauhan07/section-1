    # Problem-3:  With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]

    # Output: (examples)
    #     1) input a = 1, then output : 1
    #     2) input a = 2, then output : 1
    #     3) input a = 3, then output : 1, 3, 5
    #     4) input a = 4, then output : 1, 3, 5
    #     5) input a = 5, then output : 1, 3, 5, 7, 9
    #     6) input a = 6, then output : 1, 3, 5, 7, 9

x=int(input("Enter No:"),10);
temp=1;
for i in range(0,x):
    if(temp=1 or temp==2):
        print(1,end=" ")
    else:
        s=temp+i
        print(s,end=" ")
    temp=temp+1
