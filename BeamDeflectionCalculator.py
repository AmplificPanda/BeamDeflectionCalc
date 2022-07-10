#!/usr/bin/python3
#Credits to Stormpug/RTTGOD (creator)

#Beam deflection formula calculation

#menu function
def Menu():
 option1="Enter 1 to Run Experiment"
 option2="Enter 2 to Exit \n\n"

 print(option1)
 print(option2)
 print("please enter your selection: ")
 try:
     option=int(input("Enter number: "))
     while (option==1):
         RunExperiment()
     else:
         print("exitted")
 except:
     print("Exception incurred")
     Menu()
     
def RunExperiment():
    W=float(input("enter weight value in lbs: "))
    X=float(input("enter distance from datum point value in inches: "))
    L=float(input("enter beam length in inches: "))

    #pass to part 1
    part1Ans=part1(W,X,L)
    #print(part1Ans)

    #get values and pass to part 2
    E=float(input("enter elasticity value: "))
    I=float(input("enter inertia value: "))

    #pass to part 2
    part2Ans=part2(E,I,L)

    #pass to part 3
    part3Ans=part3(L,X)

    #send to the last function, to calculate deflection amount
    final=deflection(part1Ans,part2Ans,part3Ans)
    print("The deflection at given point x={:} is {:.3f} \n\n".format(X,final))
    Menu()

def part1(W,X,L):
    answer1=W*X*(L-X)
    return answer1

def part2(E,I,L):
    answer2=24*E*I*L
    return answer2

def part3(L,X):
    answer3=(L**2)+X*(L-X)
    return answer3


def deflection(part1Ans,part2Ans,part3Ans):
    y=(part1Ans/part2Ans)*part3Ans
    return y




Menu()
